from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import (CreateView, ListView)


from .. import models
from ..forms import model_forms


class DistrictCreateView(CreateView):
    form_class = model_forms.DisrictForm
    model = models.District


class DistrictListView(ListView):
    model = models.District


class TalukaCreateView(CreateView):
    fields = ['district_id', 'name']
    model = models.Taluka


class TalukaListView(ListView):
    model = models.Taluka