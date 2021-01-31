from django.views.generic import (CreateView, ListView, UpdateView)

from .. import models
from ..forms import model_forms


class DistrictCreateView(CreateView):
    form_class = model_forms.DisrictForm
    model = models.District


class DistrictUpdateView(UpdateView):
    form_class = model_forms.DisrictForm
    model = models.District


class DistrictListView(ListView):
    model = models.District


class TalukaCreateView(CreateView):
    form_class = model_forms.TalukaForm
    model = models.Taluka


class TalukaUpdateView(UpdateView):
    form_class = model_forms.TalukaForm
    model = models.Taluka


class TalukaListView(ListView):
    model = models.Taluka


class VillageCreateView(CreateView):
    form_class = model_forms.VillageForm
    model = models.Village


class VillageUpdateView(UpdateView):
    form_class = model_forms.VillageForm
    model = models.Village


class VillageListView(ListView):
    model = models.Village


class FaliyaCreateView(CreateView):
    form_class = model_forms.FaliyaForm
    model = models.Faliya


class FaliyaUpadateView(UpdateView):
    form_class = model_forms.FaliyaForm
    model = models.Faliya


class FaliyaListView(ListView):
    model = models.Faliya


class VehicalCreateView(CreateView):
    model = models.Vehical
    fields = '__all__'


class VehicalUpdateView(UpdateView):
    model = models.Vehical
    fields = '__all__'



class VehicalListView(ListView):
    model = models.Vehical


