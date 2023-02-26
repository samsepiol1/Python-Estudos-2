from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url(r'$^',views.cadastrar_usuario),

]