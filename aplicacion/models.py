from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Vino(models.Model):
    categoria = models.CharField(max_length=50)
    uva = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.categoria}, {self.uva}"

class Espumante(models.Model):
    categoria = models.CharField(max_length=50)
    varietal = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.categoria}, {self.varietal}, {self.marca} "

class Whisky(models.Model):
    categoria = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.categoria}, {self.marca}"

class Spirit(models.Model):
    categoria = models.CharField(max_length=50)
    producto = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.categoria}, {self.producto}, {self.marca} "

class Cerveza(models.Model):
    estilo = models.CharField(max_length=50)
    color = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.estilo}, {self.color}"

class OurCreator(models.Model):
    about_me = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.about_me}"
    
class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete= models.CASCADE)

    def __str__(self):
        return f"{self.user} [{self.imagen}]"