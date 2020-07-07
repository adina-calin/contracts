from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('contract/', views.contract_detalii),
    path('actaditional/', views.actaditional_detalii),
]
