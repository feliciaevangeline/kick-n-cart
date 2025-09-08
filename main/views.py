from django.shortcuts import render
from main.models import Product

def show_main(request):
    products = Product.objects.all()  # ambil semua produk dari database
    context = {
        'npm': '2406437054', 
        'name': 'Felicia Evangeline Mubarun',
        'class': 'PBP E',
        'products': products,
    }
    return render(request, "main.html", context)
