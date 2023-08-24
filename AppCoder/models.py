from django.db import models

# Create your models here.

class Autos(models.Model):
        marca=models.CharField(max_length=50)
        modelo=models.CharField(max_length=50)


class Motos(models.Model):
        marca=models.CharField(max_length=50)
        modelo=models.CharField(max_length=50)


class Camionetas(models.Model):
        marca=models.CharField(max_length=50)
        modelo=models.CharField(max_length=50)