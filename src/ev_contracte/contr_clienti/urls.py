from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='acasa'),
    path('contract/<int:pk1>/', views.contract_detalii, name='contract-detail'),
    path('contract/<int:pk1>/actaditional/<int:pk2>/', views.actaditional_detalii, name='actaditional-detail'),
    path('contract/new/', views.creeaza_contract, name='contract-nou'),
    path('contract/<int:pk1>/actaditional/new/', views.creeaza_actaditional, name='actaditional-nou'),
    # path('contract/<int:pk>/update/', views.update_contract, name='contract-update'),
    # path('actaditional/<int:pk>/update/', views.update_actaditional, name='actaditional-update'),
    # path('contract/<int:pk>/delete/', ContractDeleteView.as_view(), name='contract-delete'),
    # path('actaditional/<int:pk>/delete/', ActAditionalDeleteView.as_view(), name='actaditional-delete'),
    # path('about/', views.about, name='despre_app'),
]
