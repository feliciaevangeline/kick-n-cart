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
import requests
import json

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
@login_required
@require_POST
def add_product_entry_ajax(request):
    try:
        name = request.POST.get("name")
        price = request.POST.get("price")
        description = request.POST.get("description")
        thumbnail = request.POST.get("thumbnail")  # URL string
        category = request.POST.get("category")
        brand = request.POST.get("brand")
        stock = request.POST.get("stock")
        is_featured = request.POST.get("is_featured") == "true"

        product = Product.objects.create(
            user=request.user,
            name=name,
            price=price,
            description=description,
            thumbnail=thumbnail,  # langsung simpan string URL
            category=category,
            brand=brand,
            stock=stock,
            is_featured=is_featured,
        )

        return JsonResponse({
            "status": "success",
            "id": str(product.id),
            "name": product.name,
            "price": product.price,
            "description": product.description,
            "thumbnail": product.thumbnail,  # langsung string
            "category": product.category,
            "brand": product.brand,
            "stock": product.stock,
            "is_featured": product.is_featured,
        })
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)})

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

@login_required
@require_POST
def edit_product_ajax(request, id):
    try:
        product = Product.objects.get(id=id, user=request.user)

        # Update field biasa
        product.name = request.POST.get("name")
        product.price = request.POST.get("price")
        product.description = request.POST.get("description")
        product.category = request.POST.get("category")
        product.brand = request.POST.get("brand")
        product.stock = request.POST.get("stock")
        product.is_featured = request.POST.get("is_featured") == "true"

        if "thumbnail" in request.FILES:
            product.thumbnail = request.FILES["thumbnail"]
        else:
            product.thumbnail = product.thumbnail

        product.save()

        return JsonResponse({
    "status": "success",
    "message": "Product updated successfully",
    "product": {
        "id": str(product.id),
        "name": product.name,
        "price": product.price,
        "description": product.description,
        "thumbnail": (
            product.thumbnail.url
            if hasattr(product.thumbnail, "url")
            else product.thumbnail or ""
        ),
        "category": product.category,
        "brand": product.brand,
        "stock": product.stock,
        "is_featured": product.is_featured,
    }
})

    except Product.DoesNotExist:
        return JsonResponse({"status": "error", "message": "Product not found."})
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)})


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

def proxy_image(request):
    image_url = request.GET.get('url')
    if not image_url:
        return HttpResponse('No URL provided', status=400)
    
    try:
        # Fetch image from external source
        response = requests.get(image_url, timeout=10)
        response.raise_for_status()
        
        # Return the image with proper content type
        return HttpResponse(
            response.content,
            content_type=response.headers.get('Content-Type', 'image/jpeg')
        )
    except requests.RequestException as e:
        return HttpResponse(f'Error fetching image: {str(e)}', status=500)
    
@csrf_exempt
def create_product_flutter(request):
    """
    Menerima POST JSON dari Flutter untuk membuat Product baru
    yang terasosiasi dengan user yang sedang login.
    """
    if request.method == 'POST':
        # Pastikan user sudah login (CookieRequest Django)
        if not request.user.is_authenticated:
            return JsonResponse(
                {
                    "status": "error",
                    "message": "User must be authenticated to create a product.",
                },
                status=401,
            )

        try:
            data = json.loads(request.body)

            name = strip_tags(data.get("name", ""))
            description = strip_tags(data.get("description", ""))

            price = data.get("price", 0)
            stock = data.get("stock", 0)

            # Konversi price & stock ke int
            try:
                price = int(price)
            except (ValueError, TypeError):
                price = 0

            try:
                stock = int(stock)
            except (ValueError, TypeError):
                stock = 0

            thumbnail = data.get("thumbnail", "")
            category = data.get("category", "")
            is_featured = data.get("is_featured", False)
            brand = data.get("brand", "")

            new_product = Product(
                user=request.user,
                name=name,
                price=price,
                description=description,
                thumbnail=thumbnail,
                category=category,
                is_featured=is_featured,
                stock=stock,
                brand=brand,
            )
            new_product.save()

            return JsonResponse(
                {
                    "status": "success",
                    "message": "Product created successfully.",
                },
                status=200,
            )

        except json.JSONDecodeError:
            return JsonResponse(
                {
                    "status": "error",
                    "message": "Invalid JSON payload.",
                },
                status=400,
            )

    # Kalau bukan POST
    return JsonResponse(
        {
            "status": "error",
            "message": "Only POST method is allowed.",
        },
        status=405,
    )


@login_required(login_url="/login/")
def show_json(request):
    """
    Endpoint JSON yang hanya mengembalikan produk
    milik user yang sedang login (filter per user).
    Dipakai oleh Flutter di /json/.
    """
    data = Product.objects.filter(user=request.user)
    return HttpResponse(
        serializers.serialize("json", data),
        content_type="application/json",
    )
