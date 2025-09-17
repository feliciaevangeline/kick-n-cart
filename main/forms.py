<<<<<<< HEAD
=======
# ========= tugas 3 ==========
>>>>>>> edda9d5fcb86c9cf7acad07be6a4c4f01b8d5b47
from django.forms import ModelForm
from .models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
<<<<<<< HEAD
        fields = ["name", "price", "description", "thumbnail", "category", "is_featured", "stock", "brand"]
=======
        fields = [
            'name', 'price', 'description',
            'thumbnail', 'category', 'is_featured',
            'stock', 'brand'
        ]
>>>>>>> edda9d5fcb86c9cf7acad07be6a4c4f01b8d5b47
