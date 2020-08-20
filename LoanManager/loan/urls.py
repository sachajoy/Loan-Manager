from django.urls import path
from .views import views, address

app_name = 'loan'
urlpatterns = [
    path('', views.index, name='index'),
    path('create-district',
         address.DistrictCreateView.as_view(),
         name='create-district'),
    path('list-district',
         address.DistrictListView.as_view(),
         name = 'list-district'),
    path('create-taluka',
         address.TalukaCreateView.as_view(),
         name='create-taluka'),
    path('list-taluka',
         address.TalukaListView.as_view(),
         name='list-taluka'),
]
