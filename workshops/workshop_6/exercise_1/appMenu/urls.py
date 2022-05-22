from django.urls import path
from appMenu import views
from django.views.generic import TemplateView

app_name = "appMenu"

urlpatterns = [
 path("", views.index, name="home"),
 path('list_doctores', views.list_doctor, name="list_doctores"), 
 path('registrar_doctor', views.registrar_doctor),
 path('eliminar_doctor/<id>', views.eliminar_doctor), 
 
 
 
 
 path('listpacientes', views.list_pacientes, name="listpacientes"),
 path('listcitas', views.list_citas, name="listcitas"),
 


 path('citas', TemplateView.as_view(template_name="citas.html"), name="citas"),
 path('pacientes', TemplateView.as_view(template_name="pacientes.html"), name="pacientes"),
 path('doctores', TemplateView.as_view(template_name="doctores.html"), name="doctores")
]