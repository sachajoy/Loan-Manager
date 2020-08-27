from django.views.generic import (CreateView, ListView,
                                  UpdateView, DetailView)

from .. import models
from ..forms import client_forms


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
