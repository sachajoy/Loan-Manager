from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('loan/', include('loan.urls', namespace='loan')),
    path('', include('loan.urls', namespace='loan')),
    path('admin/', admin.site.urls),
]
