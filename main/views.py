from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductForm
from .models import Product
from django.http import HttpResponse
from django.core import serializers

def show_main(request):
    products = Product.objects.all()
    context = {
        'npm': '2406437054',
        'name': 'Felicia Evangeline Mubarun',
        'class': 'PBP E',
        'products': products
    }
    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)
    
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('main:show_main')
    
    context = {'form': form}
    return render(request, "create_product.html", context)

def show_product(request, id):
    product = get_object_or_404(Product, pk=id)
<<<<<<< HEAD
    context = {
        'product': product
        }
=======
    context = {'product': product}
>>>>>>> edda9d5fcb86c9cf7acad07be6a4c4f01b8d5b47
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