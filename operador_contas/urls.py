from django.urls import path
from . import views

urlpatterns = [
    path('', views.Contas.as_view(), name='lista-contas')
]
