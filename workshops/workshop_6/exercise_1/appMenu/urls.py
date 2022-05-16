from django.urls import path
from appMenu import views
from django.views.generic import TemplateView

app_name = "app"

urlpatterns = [
 path("", views.index, name="index")
]