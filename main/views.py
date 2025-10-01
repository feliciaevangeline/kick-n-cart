# tugas 3
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductForm
from .models import Product
from django.http import HttpResponse
from django.core import serializers
# tugas 4
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

# tugas 3
# @login_required(login_url='/login')
# def show_main(request):
#     products = Product.objects.all()
#     context = {
#         'npm': '2406437054',
#         'name': 'Felicia Evangeline Mubarun',
#         'class': 'PBP E',
#         'products': products,
#         'last_login': request.COOKIES.get('last_login', 'Never')
#     }
#     return render(request, "main.html", context)

# tugas 4
@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")  # default 'all'

    if filter_type == "all":
        products = Product.objects.all()
    else:
        # filter produk hanya milik user yang sedang login
        products = Product.objects.filter(user=request.user)

    context = {
        'npm': '2406437054',
        'name': request.user.username,
        'class': 'PBP E',
        'products': products,
        'last_login': request.COOKIES.get('last_login', 'Never')
    }
    return render(request, "main.html", context)

# tugas 4
@login_required(login_url='/login')
def create_product(request):
    form = ProductForm(request.POST or None)
    if form.is_valid() and request.method == 'POST':
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return redirect('main:show_main')

    context = {
        'form': form,
        'npm': '2406437054',
        'name': request.user.username if request.user.is_authenticated else '',
        'class': 'PBP E'
    }
    return render(request, "create_product.html", context)

@login_required(login_url='/login') # tugas 4
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)
    context = {
        'product': product,
        'npm': '2406437054',
        'name': request.user.username if request.user.is_authenticated else '',
        'class': 'PBP E'
    }
    return render(request, "product_detail.html", context)

# API JSON
def show_json(request):
    data = Product.objects.all()
    return HttpResponse(
        serializers.serialize("json", data),
        content_type="application/json"
    )

def show_json_by_id(request, id):
    product = get_object_or_404(Product, pk=id)
    return HttpResponse(
        serializers.serialize("json", [product]),
        content_type="application/json"
    )

# API XML
def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(
        serializers.serialize("xml", data),
        content_type="application/xml"
    )

def show_xml_by_id(request, id):
    product = get_object_or_404(Product, pk=id)
    return HttpResponse(
        serializers.serialize("xml", [product]),
        content_type="application/xml"
    )

# tugas 4
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

   else:
    form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
    

# tugas 5
def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {
        'form': form,
        'product': product
    }

    return render(request, "edit_product.html", context)

def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))