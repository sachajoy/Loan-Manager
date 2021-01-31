from django.urls import path

from .views import (address, client_view,
                    emi_views, loan_views,
                    views, reports)

app_name = 'loan'
urlpatterns = [
    path('', views.index, name='index'),
    # DISTRICT
    path('create-district',
         address.DistrictCreateView.as_view(),
         name='create-district'),
    path('update-district/<int:pk>',
         address.DistrictUpdateView.as_view(),
         name='update-district'),
    path('list-district',
         address.DistrictListView.as_view(),
         name='list-district'),
    # TALUKA
    path('create-taluka',
         address.TalukaCreateView.as_view(),
         name='create-taluka'),
    path('update-taluka/<int:pk>',
         address.TalukaUpdateView.as_view(),
         name='update-taluka'),
    path('list-taluka',
         address.TalukaListView.as_view(),
         name='list-taluka'),
    # VILLAGE
    path('create-village',
         address.VillageCreateView.as_view(),
         name='create-village'),
    path('update-village/<int:pk>',
         address.VillageUpdateView.as_view(),
         name='update-village'),
    path('list-village',
         address.VillageListView.as_view(),
         name='list-village'),
    # FALIYA
    path('create-faliya',
         address.FaliyaCreateView.as_view(),
         name='create-faliya'),
    path('update-faliya/<int:pk>',
         address.FaliyaUpadateView.as_view(),
         name='update-faliya'),
    path('list-faliya',
         address.FaliyaListView.as_view(),
         name='list-faliya'),
    # CLIENT
    path('create-client',
         client_view.ClientCreateView.as_view(),
         name='create-client'),
    path('list-client',
         client_view.ClientListView.as_view(),
         name='list-client'),
    path('client-detial/<int:pk>',
         client_view.ClientDetailView.as_view(),
         name='detial-client'),
    # LOAN
    path('client/<int:client_pk>/create-loan',
         loan_views.LoanCreateView.as_view(),
         name='create-loan'),
    path('client/<int:client_pk>/detail-loan/<int:pk>',
         loan_views.LoanDetailView.as_view(),
         name='loan-detail'),
    path('create-firm',
         client_view.FirmCreateView.as_view(),
         name='create-firm'),
    # EMI
    path('client/<int:client_pk>/loan/<int:loan_pk>/emis',
         emi_views.EMIListView.as_view(),
         name='list-emi'),
    path('client/<int:client_pk>/loan/<int:loan_pk>/emi/<int:pk>',
         emi_views.EMIUpadateView.as_view(),
         name='update-emi'),
#     Reports
    path('defaulters',
         reports.FetchDefaultersListView.as_view(),
         name='defaulter'),
    # Vehical
    path('create-vehical',
         address.VehicalCreateView.as_view(),
         name='vehical-create'),
    path('list-vehical',
         address.VehicalListView.as_view(),
         name='vehical-list'),
    path('update-vehical/<int:pk>',
         address.VehicalUpdateView.as_view(),
         name='vehical-update')
]
