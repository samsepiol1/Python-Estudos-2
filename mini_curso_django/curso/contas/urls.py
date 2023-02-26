from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path(r'$^',views.pagina_inicial),
    path('admin/', admin.site.urls),
]