from django.test import TestCase
from .models import Produk

class ProdukTestCase(TestCase):

    def setUp(self):
        Produk.objects.create(nama="Laptop")

    def test_produk_nama(self):
        """Tes untuk memastikan nama produk benar"""
        laptop = Produk.objects.get(nama="Laptop")
        self.assertEqual(laptop.nama, 'Laptop')
