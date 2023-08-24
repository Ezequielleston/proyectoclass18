from django.contrib import admin
from .models import Autos, Camionetas, Motos

# Register your models here.
admin.site.register(Autos)
admin.site.register(Camionetas)
admin.site.register(Motos)