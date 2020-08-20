from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import (CreateView, ListView)
from .. import models


class DistrictCreateView(CreateView):
    fields = ['name']
    model = models.District


class DistrictListView(ListView):
    models = models.District