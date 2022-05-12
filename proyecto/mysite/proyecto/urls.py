from django.urls import path
from proyecto import views
from django.views.generic import TemplateView

urlpatterns = [    
    path("Listjuegos/", views.listar_juegos), 
    path("", views.index, name="index"),    
    path('juegadores/', TemplateView.as_view(template_name="jugadores.html"), name="jugadores"),
    path('juegos/', TemplateView.as_view(template_name="juegos.html"), name="juegos"),    
]

