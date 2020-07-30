from django.urls import path, include
from .views import views

app_name = 'loan'
urlpatterns = [
    path('', views.index, name='index'),
]
