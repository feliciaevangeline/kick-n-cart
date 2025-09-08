from django.test import TestCase, Client
from django.urls import reverse
from .models import Product

class MainTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.product = Product.objects.create(
            name="Nike Mercurial",
            price=1999000,
            description="Sepatu bola ringan dan cepat",
            thumbnail="http://example.com/mercurial.jpg",
            category="Shoes",
            is_featured=True,
            stock=5,
            brand="Nike"
        )

    # --- URL & View Test ---
    def test_main_url_is_exist(self):
        """Halaman utama dapat diakses"""
        response = self.client.get(reverse('main:show_main'))
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        """Halaman utama menggunakan template main.html"""
        response = self.client.get(reverse('main:show_main'))
        self.assertTemplateUsed(response, 'main.html')

    def test_nonexistent_page(self):
        """Halaman yang tidak ada harus return 404"""
        response = self.client.get('/halaman_tidak_ada/')
        self.assertEqual(response.status_code, 404)

    # --- Model Test ---
    def test_product_creation(self):
        """Produk berhasil dibuat dengan benar"""
        self.assertEqual(self.product.name, "Nike Mercurial")
        self.assertEqual(self.product.price, 1999000)
        self.assertTrue(self.product.is_featured)
        self.assertEqual(str(self.product), "Nike Mercurial")

    def test_product_default_values(self):
        """Produk baru tanpa is_featured otomatis False"""
        product = Product.objects.create(
            name="Adidas Predator",
            price=2500000,
            description="Sepatu bola premium",
            thumbnail="http://example.com/predator.jpg",
            category="Shoes"
        )
        self.assertFalse(product.is_featured)
        self.assertEqual(product.stock, 0)  # default stock = 0
        self.assertIsNone(product.brand)    # default brand = None

    # --- Context Test ---
    def test_context_contains_identity(self):
        """Context harus berisi identitas mahasiswa"""
        response = self.client.get(reverse('main:show_main'))
        self.assertContains(response, "2406437054")
        self.assertContains(response, "Felicia Evangeline Mubarun")
        self.assertContains(response, "PBP E")

    def test_product_displayed_in_template(self):
        """Produk yang ada di database tampil di halaman utama"""
        response = self.client.get(reverse('main:show_main'))
        self.assertContains(response, "Nike Mercurial")
        self.assertContains(response, "1999000")
        self.assertContains(response, "Shoes")
