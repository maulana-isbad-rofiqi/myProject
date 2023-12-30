from django.contrib import admin
from .models import Keranjang, ItemKeranjang

class ItemKeranjangAdmin(admin.ModelAdmin):
    list_display = ('produk', 'jumlah', 'keranjang')
    list_filter = ('produk',)

admin.site.register(Keranjang)
admin.site.register(ItemKeranjang, ItemKeranjangAdmin)
