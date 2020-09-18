from django.contrib import admin

from . import models
# Register your models here.
admin.site.register(models.District)
admin.site.register(models.Taluka)
admin.site.register(models.Village)
admin.site.register(models.Faliya)
admin.site.register(models.Firm)
admin.site.register(models.Client)
admin.site.register(models.Loan)
admin.site.register(models.Emi)

