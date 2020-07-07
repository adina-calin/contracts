from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('contract/<int:pk1>/', views.contract_detalii, name='contract-detail'),
    path('contract/<int:pk1>/actaditional/<int:pk2>/', views.actaditional_detalii, name='actaditional-detail'),
]
