from django.views.generic import (CreateView, ListView)


from .. import models
from ..forms import model_forms


class DistrictCreateView(CreateView):
    form_class = model_forms.DisrictForm
    model = models.District


class DistrictListView(ListView):
    model = models.District


class TalukaCreateView(CreateView):
    form_class = model_forms.TalukaForm
    model = models.Taluka


class TalukaListView(ListView):
    model = models.Taluka


class VillageCreateView(CreateView):
    form_class = model_forms.VillageForm
    model = models.Village


class VillageListView(ListView):
    model = models.Village


class FaliyaCreateView(CreateView):
    form_class = model_forms.FaliyaForm
    model = models.Faliya


class FaliyaListView(ListView):
    model = models.Faliya