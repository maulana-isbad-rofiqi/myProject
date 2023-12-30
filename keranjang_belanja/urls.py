from django.urls import path
from . import views

urlpatterns = [
    # ... (paths lainnya)
    path('tambah-ke-keranjang/<int:produk_id>/', views.tambah_ke_keranjang, name='tambah_ke_keranjang'),
    path('keranjang/', views.keranjang, name='keranjang'),
    path('product/keranjang/', views.keranjang, name='keranjang'),


]
