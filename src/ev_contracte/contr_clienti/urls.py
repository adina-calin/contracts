from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='acasa'),
    path('contract/<int:pk1>/', views.contract_detalii, name='contract-detail'),
    path('contract/<int:pk1>/upload', views.contract_scan, name='contract-upload'),
    path('contract/<int:pk1>/actaditional/<int:pk2>/', views.actaditional_detalii, name='actaditional-detail'),
    path('contract/new/', views.creeaza_contract, name='contract-nou'),
    path('contract/<int:pk1>/actaditional/new/', views.creeaza_actaditional, name='actaditional-nou'),
    path('contract/<int:pk1>/update/', views.update_contract, name='contract-update'),
    path('contract/<int:pk1>/actaditional/<int:pk2>/update/', views.update_actaditional, name='actaditional-update'),
    path('contract/<int:pk1>/delete/', views.sterge_contract, name='contract-delete'),
    path('contract/<int:pk1>/actaditional/<int:pk2>/delete/', views.sterge_actaditional, name='actaditional-delete'),
    path('contract/<int:pk1>/actaditional/<int:pk2>/upload/', views.actaditional_scan, name='actaditional-upload'),
    path('contract/<int:pk1>/<int:pk3>/deleteupload/', views.sterge_documentc, name='documentc-delete'),
    path('contract/<int:pk1>/actaditional/<int:pk2>/<int:pk3>/deleteupload/', views.sterge_documenta, name='documenta-delete'),
    path('rapoarte/', views.rapoarte, name='rapoarte'),
    path('produs/new/', views.creeaza_produs, name='produs-nou'),
    path('produs/<int:pk9>/update', views.update_produs, name='produs-update'),
    path('serviciu/new/', views.creeaza_serviciu, name='serviciu-nou'),
    path('serviciu/<int:pk10>/update', views.update_serviciu, name='serviciu-update'),
    path('aplicatie/new/', views.creeaza_aplicatie, name='aplicatie-nou'),
    path('aplicatie/<int:pk11>/update', views.update_aplicatie, name='aplicatie-update'),
    path('psa/lista', views.lista_psa, name='psa-lista'),
    path('rapoarte/registruPdf', views.listare_registru, name='registru-pdf'),
    # path('clienti/', views.rapoarte, name='rapoarte'),
    path('client/<int:pk4>/', views.client_detalii, name='client-detail'),
    path('client/new', views.creeaza_client, name='client-nou'),
    path('client/lista', views.lista_clienti, name='clienti-lista'),
    path('client/<int:pk4>/update', views.update_client_detalii, name='client-detail-update'),
    path('client/<int:pk4>/update_dc', views.update_client_date, name='client-date-update'),
    path('client/<int:pk4>/reprezentant/new', views.creeaza_reprezentant, name='reprezentant-nou'),
    path('client/<int:pk4>/reprezentant/<int:pk5>/update/', views.update_reprezentant, name='reprezentant-update'),
    path('client/<int:pk4>/reprezentant/<int:pk5>/delete/', views.sterge_reprezentant, name='reprezentant-delete'),
    path('client/<int:pk4>/persoanacontact/new', views.creeaza_persoanacontact, name='persoanacontact-nou'),
    path('client/<int:pk4>/persoanacontact/<int:pk6>/update/', views.update_persoanacontact, name='persoanacontact-update'),
    path('client/<int:pk4>/persoanacontact/<int:pk6>/delete/', views.sterge_persoanacontact, name='persoanacontact-delete'),
    path('client/<int:pk4>/adresapl/new', views.creeaza_adresapl, name='adresapl-nou'),
    path('client/<int:pk4>/adresapl/<int:pk7>/update/', views.update_adresapl, name='adresapl-update'),
    path('client/<int:pk4>/adresapl/<int:pk7>/delete/', views.sterge_adresapl, name='adresapl-delete'),
    path('client/<int:pk4>/adresass/new', views.creeaza_adresass, name='adresass-nou'),
    path('client/<int:pk4>/adresass/<int:pk8>/update/', views.update_adresass, name='adresass-update'),
    path('client/<int:pk4>/adresass/<int:pk8>/delete/', views.sterge_adresass, name='adresass-delete'),
]
