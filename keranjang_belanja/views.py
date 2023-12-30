from django.http import HttpResponseServerError

def keranjang(request):
    try:
        keranjang, _ = Keranjang.objects.get_or_create(pengguna=request.user)
        items = keranjang.item_keranjang.all()
        total = sum(item.produk.harga * item.jumlah for item in items)
        return render(request, 'myApp/keranjang.html', {'items': items, 'total': total})
    except Exception as e:
        return HttpResponseServerError(f"Error: {e}")
