from django.views.generic import (CreateView, DetailView, ListView, UpdateView)

from .. import models
from ..forms import client_forms


class FirmCreateView(CreateView):
    fields = ['name', 'abv']
    model = models.Firm


class ClientCreateView(CreateView):
    form_class = client_forms.ClientForm
    model = models.Client


class ClientUpdateView(UpdateView):
    form_class = client_forms.ClientForm
    model = models.Client


class ClientListView(ListView):
    model = models.Client


class ClientDetailView(DetailView):
    model = models.Client
