from django.db import models
from django.contrib.auth.models import User

class Keranjang(models.Model):
    pengguna = models.ForeignKey(User, on_delete=models.CASCADE)
    tanggal_dibuat = models.DateTimeField(auto_now_add=True)

class Produk(models.Model):  # Menambahkan model Produk
    nama = models.CharField(max_length=200)
    # Anda dapat menambahkan field lain yang diperlukan untuk model Produk

class ItemKeranjang(models.Model):
    keranjang = models.ForeignKey(Keranjang, related_name='item_keranjang', on_delete=models.CASCADE)
    produk = models.ForeignKey(Produk, on_delete=models.CASCADE)  # Menggunakan model Produk yang baru didefinisikan
    jumlah = models.PositiveIntegerField(default=1)
