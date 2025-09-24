from django.db import models
import uuid
from django.contrib.auth.models import User # tugas 4

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True) # tugas 4
    CATEGORY_CHOICES = [
        ('sepatu', 'Sepatu'),
        ('jersey', 'Jersey'),
        ('bola', 'Bola'),
        ('aksesoris', 'Aksesoris'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)  
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField()
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default='sepatu'
    )

    is_featured = models.BooleanField(default=False)

    # Atribut tambahan
    stock = models.PositiveIntegerField(default=0)
    brand = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name
