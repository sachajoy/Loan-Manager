from django.urls import path, include
from .views import views

urlpatterns = [
    path('', views.index, name='index'),
]
