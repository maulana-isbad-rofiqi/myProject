from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
import requests
from django.http import HttpResponse
from twilio.rest import Client
from django.http import HttpResponseRedirect


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
    if request.method == 'GET':
        fullname = request.GET.get('fullname')
        email = request.GET.get('email')
        phone = request.GET.get('phone')
        address = request.GET.get('address')
        payment_method = request.GET.get('payment_method')

        pesan = f"Detail Pesanan:\nNama Lengkap: {fullname}\nEmail: {email}\nNomor Telepon: {phone}\nAlamat: {address}\nMetode Pembayaran: {payment_method}"
        
        kirim_pesan_whatsapp(pesan)
        

        return HttpResponseRedirect('/path/ke/halaman/sukses/atau/lainnya/')

def chat(request):
    return render(request, 'myApp/chat.html')

def keranjang(request):
    return render(request, 'keranjang.html')

def add_to_cart(request):
    pass

def place_order(request):
    pass

def ringkasan_order(request):
    pass
