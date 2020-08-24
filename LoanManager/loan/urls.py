from django.urls import path

from .views import address, views

app_name = 'loan'
urlpatterns = [
    path('', views.index, name='index'),
    path('create-district',
         address.DistrictCreateView.as_view(),
         name='create-district'),
    path('list-district',
         address.DistrictListView.as_view(),
         name='list-district'),
    path('create-taluka',
         address.TalukaCreateView.as_view(),
         name='create-taluka'),
    path('list-taluka',
         address.TalukaListView.as_view(),
         name='list-taluka'),
    path('create-village',
         address.VillageCreateView.as_view(),
         name='create-village'),
    path('list-village',
         address.VillageListView.as_view(),
         name='list-village'),
    path('create-faliya',
         address.FaliyaCreateView.as_view(),
         name='create-faliya'),
    path('list-faliya',
         address.FaliyaListView.as_view(),
         name='list-faliya'),
]
