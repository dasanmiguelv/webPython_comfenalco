from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("proyecto.urls")),
    path("juegos/", views.listar_juegos),
    path('admin/', admin.site.urls),
]

