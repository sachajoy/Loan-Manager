from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('loan/', include('loan.urls', namespace='loan')),
    path('admin/', admin.site.urls),
]
