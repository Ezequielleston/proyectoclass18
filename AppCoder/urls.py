from django.urls import path
from .views import crear_autos, listar_autos, camionetas, motos, autos


urlpatterns = [
    path("crear_autos/", crear_autos),
    path("listar_autos/", listar_autos),
    path("camionetas/", camionetas, name="camionetas"),
    path("motos/", motos, name="motos"),
    path("autos/", autos, name="autos"),

]