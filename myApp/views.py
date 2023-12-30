from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
import requests
from django.http import HttpResponse
from twilio.rest import Client
from django.http import HttpResponseRedirect

# Definisi fungsi kirim_pesan_whatsapp
def kirim_pesan_whatsapp(pesan):
    nomorAdmin = '6285236363128'
    url = f"https://api.whatsapp.com/send?phone={nomorAdmin}&text={pesan}"
    # Anda mungkin ingin menggantikan window.open dengan redirect jika ingin melakukan redirect
    # window.open(url, '_blank')

def beranda(request):
    return render(request, 'myApp/beranda.html')

def product(request):
    return render(request, 'myApp/product.html')

def contact(request):
    return render(request, 'myApp/contact.html')

def checkout(request):
    if request.method == 'GET':
        fullname = request.GET.get('fullname')
        email = request.GET.get('email')
        phone = request.GET.get('phone')
        address = request.GET.get('address')
        payment_method = request.GET.get('payment_method')

        pesan = f"Detail Pesanan:\nNama Lengkap: {fullname}\nEmail: {email}\nNomor Telepon: {phone}\nAlamat: {address}\nMetode Pembayaran: {payment_method}"
        
        kirim_pesan_whatsapp(pesan)
        
        # Redirect atau tampilkan halaman sukses atau lainnya
        return HttpResponseRedirect('/path/ke/halaman/sukses/atau/lainnya/')

def chat(request):
    return render(request, 'myApp/chat.html')

def keranjang(request):
    return render(request, 'keranjang.html')

def add_to_cart(request):
    # Implementasi Anda di sini
    pass

def place_order(request):
    # Implementasi Anda di sini
    pass

def ringkasan_order(request):
    pass
