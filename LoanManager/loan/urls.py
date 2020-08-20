from django.urls import path
from .views import views, address

app_name = 'loan'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/district',
         address.DistrictCreateView.as_view(),
         name='create-district'),
]
