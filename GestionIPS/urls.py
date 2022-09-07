from django.urls import path
from pruebasIni.views import Entidad_saludview



urlpatterns = [
    path('entidades/',Entidad_saludview.as_view(), name='Listar') 
]
