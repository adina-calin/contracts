from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('contract/', views.contract),
    path('actaditional/', views.actaditional),
]
