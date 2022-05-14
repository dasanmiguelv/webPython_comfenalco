from django.urls import path
from proyecto import views
from django.views.generic import TemplateView

app_name ="app"

urlpatterns = [    
    path("Listjuegos/", views.listar_juegos), 
    path("", views.index, name="index"),    
    path('jugadores/', TemplateView.as_view(template_name="jugadores.html"), name="jugadores"),
    path('juegos/', TemplateView.as_view(template_name="juegos.html"), name="juegos"),    
    path('italia/', TemplateView.as_view(template_name="itali.html"), name="italia"),
    path('japan/', TemplateView.as_view(template_name="japan.html"), name="japan"),
]

