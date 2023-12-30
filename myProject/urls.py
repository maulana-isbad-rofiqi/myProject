from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from myApp.views import beranda, product, contact, add_to_cart, place_order, checkout, chat, keranjang
from django.contrib.auth.views import LoginView, LogoutView
import requests
from django.http import HttpResponse
from twilio.rest import Client
from django.shortcuts import render


def kirim_pesan_whatsapp(pesan):
    nomorAdmin = '6285236363128'
    url = f"https://api.whatsapp.com/send?phone={nomorAdmin}&text={pesan}"

def beranda(request):
    return render(request, 'myApp/beranda.html')

def product(request):
    return render(request, 'myApp/product.html')

def contact(request):
    return render(request, 'myApp/contact.html')

def checkout(request):
    return render(request, 'checkout.html')

def chat(request):
    return render(request, 'myApp/chat.html')

def keranjang(request):
    return render(request, 'keranjang.html')

def add_to_cart(request):
    pass

def place_order(request):
    pass



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', beranda, name='beranda'),
    path('product/', product, name='product'),
    path('contact/', contact, name='contact'),
    path('checkout/', checkout, name='checkout'),
    path('keranjang/', keranjang, name='keranjang'),
    path('add_to_cart/', add_to_cart, name='add_to_cart'),
    path('place_order/', place_order, name='place_order'),
    path('chat/', chat, name='chat'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),


]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
