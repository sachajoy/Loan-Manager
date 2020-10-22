from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DetailView, ListView)

from .. import models

class EMIListView(ListView):
    model = models.Emi

    def get_context_data(self, *, object_list=None, **kwargs):
        context = {}
        context['emis'] = models.Emi.objects.filter(loan_id=self.kwargs.get('loan_pk'))
        context['loan_details'] = models.Loan.objects.get(id=self.kwargs.get('loan_pk'))
        context['client'] = models.Client.objects.get(id=self.kwargs.get('client_pk'))
        return context