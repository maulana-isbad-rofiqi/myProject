from django.db import models
from django.contrib.auth.models import User
from django.db import models


class post(models.Model):
    title = models. CharField(max_length=255)
    body  = models.TextField()

    def __str__(self):
        return "{}".format(self.title)
    
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Pesanan(models.Model):
    nama = models.CharField(max_length=255)
    email = models.EmailField()
    telepon = models.CharField(max_length=15)
    alamat = models.TextField()
