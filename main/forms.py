from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "name",
            "price",
            "description",
            "thumbnail",
            "category",
            "brand",
            "stock",
            "is_featured",
        ]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 3}),
            "is_featured": forms.CheckboxInput(),
        }
