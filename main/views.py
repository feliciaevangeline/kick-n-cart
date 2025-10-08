from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.utils import timezone
from django.utils.html import strip_tags
import datetime

from .models import Product
from .forms import ProductForm


# ======================
# MAIN PAGE
# ======================
@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")

    if filter_type == "my":
        products = Product.objects.filter(user=request.user)
    else:
        products = Product.objects.all()

    context = {
        'npm': '2406437054',
        'name': request.user.username,
        'class': 'PBP E',
        'products': products,
        'last_login': request.COOKIES.get('last_login', 'Never')
    }
    return render(request, "main.html", context)


# ======================
# FORM BIASA (NON-AJAX)
# ======================
@login_required(login_url='/login')
def create_product(request):
    form = ProductForm(request.POST or None)
    if form.is_valid() and request.method == 'POST':
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        messages.success(request, "Product successfully created!")
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product.html", context)


# ======================
# AJAX ADD PRODUCT
# ======================
@login_required(login_url="/login")
@require_POST
def add_product_entry_ajax(request):
    if not request.headers.get("X-Requested-With") == "XMLHttpRequest":
        return JsonResponse({"error": "Invalid request"}, status=400)

    name = request.POST.get("name")
    price = request.POST.get("price")
    description = request.POST.get("description")
    thumbnail = request.POST.get("thumbnail")
    category = request.POST.get("category")
    brand = request.POST.get("brand")
    stock = request.POST.get("stock")
    is_featured = request.POST.get("is_featured") == "true"

    product = Product.objects.create(
        user=request.user,
        name=name,
        price=price,
        description=description,
        thumbnail=thumbnail,
        category=category,
        brand=brand,
        stock=stock,
        is_featured=is_featured,
    )

    return JsonResponse({
        "id": str(product.id),
        "name": product.name,
        "price": product.price,
        "description": product.description,
        "thumbnail": product.thumbnail,
        "category": product.category,
        "brand": product.brand,
        "stock": product.stock,
        "is_featured": product.is_featured,
    })


@login_required(login_url="/login")
def edit_product(request, id):
    product = get_object_or_404(Product, pk=id, user=request.user)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            if request.headers.get("x-requested-with") == "XMLHttpRequest":
                return JsonResponse({"status": "success", "message": "Product updated"})
            messages.success(request, "Product updated successfully!")
            return redirect("main:show_main")
        else:
            if request.headers.get("x-requested-with") == "XMLHttpRequest":
                return JsonResponse({
                    "status": "error",
                    "message": "Invalid form data",
                    "errors": form.errors,
                }, status=400)
    else:
        form = ProductForm(instance=product)
    return render(request, "edit_product.html", {"form": form, "product": product})

@login_required(login_url='/login')
@require_POST
def edit_product_ajax(request, id):
    if not request.headers.get("X-Requested-With") == "XMLHttpRequest":
        return JsonResponse({"error": "Invalid request"}, status=400)

    product = get_object_or_404(Product, pk=id, user=request.user)

    name = request.POST.get("name")
    price = request.POST.get("price")
    description = request.POST.get("description")
    category = request.POST.get("category")
    brand = request.POST.get("brand")
    stock = request.POST.get("stock")
    is_featured = request.POST.get("is_featured", "false") == "true"
    thumbnail = request.POST.get("thumbnail")  # <-- ambil dari POST, bukan FILES

    if not name or not price or not description:
        return JsonResponse({"error": "Invalid form data"}, status=400)

    product.name = name
    product.price = price
    product.description = description
    product.category = category
    product.brand = brand
    product.stock = stock
    product.is_featured = is_featured

    if thumbnail:
        product.thumbnail = thumbnail

    product.save()

    return JsonResponse({
        "status": "success",
        "message": "Product updated successfully",
        "product": {
            "id": str(product.id),
            "name": product.name,
            "price": product.price,
            "description": product.description,
            "thumbnail": product.thumbnail or "",
            "category": product.category,
            "brand": product.brand,
            "stock": product.stock,
            "is_featured": product.is_featured,
        }
    })

# ======================
# DELETE PRODUCT (AJAX)
# ======================
@login_required(login_url='/login')
@require_POST
def delete_product(request, id):
    if not request.user.is_authenticated:
        return JsonResponse({"error": "Unauthorized"}, status=401)

    product = get_object_or_404(Product, pk=id)
    if product.user != request.user:
        return JsonResponse({"error": "Unauthorized"}, status=403)

    product.delete()
    return JsonResponse({"status": "deleted"}, status=200)


# ======================
# PRODUCT DETAIL
# ======================
def show_product(request, id):
    product = get_object_or_404(Product, id=id)
    context = {
        "product": product,
        "seller": product.user.username if product.user else "Unknown",
    }
    return render(request, "product_detail.html", context)


# ======================
# JSON/XML API
# ======================
@login_required(login_url='/login')
def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    product = get_object_or_404(Product, pk=id)
    return HttpResponse(serializers.serialize("json", [product]), content_type="application/json")

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_xml_by_id(request, id):
    product = get_object_or_404(Product, pk=id)
    return HttpResponse(serializers.serialize("xml", [product]), content_type="application/xml")


# ======================
# AUTH
# ======================
def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('main:login')
    return render(request, 'register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            messages.success(request, "Login successful!")
            return response
    else:
        form = AuthenticationForm(request)
    return render(request, 'login.html', {'form': form})

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    messages.success(request, "Logout successful!")
    return response
