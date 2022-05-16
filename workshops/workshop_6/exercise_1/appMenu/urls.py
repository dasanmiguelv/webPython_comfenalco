from django.urls import path
from appMenu import views
from django.views.generic import TemplateView

app_name = "app"

urlpatterns = [
 path("", views.index, name="index"),
 path('citas', TemplateView.as_view(template_name="citas.html"), name="citas"),
 path('pacientes', TemplateView.as_view(template_name="pacientes.html"), name="pacientes"),
 path('doctores', TemplateView.as_view(template_name="doctores.html"), name="doctores")
]