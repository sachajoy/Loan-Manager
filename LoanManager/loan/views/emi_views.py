from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import (ListView, UpdateView)

from .. import models

class EMIListView(ListView):
    model = models.Emi

    def get_context_data(self, **kwargs):
        context = {}
        context['emis'] = models.Emi.objects.filter(loan_id=self.kwargs.get('loan_pk'))
        context['loan_details'] = models.Loan.objects.get(id=self.kwargs.get('loan_pk'))
        context['client'] = models.Client.objects.get(id=self.kwargs.get('client_pk'))
        return context

class EMIUpadateView(UpdateView):
    model = models.Emi
    template_name = 'loan/emi_update.html'
    fields = (
        'amt', 'due_date', 'paid_date',
        'receipt_no', 'remarks', 'penalty'
    )

    def get_context_data(self, **kwargs):
        context = super(EMIUpadateView, self).get_context_data()
        context['emis'] = models.Emi.objects.filter(loan_id=self.kwargs.get('loan_pk'))
        return context

    def get_success_url(self):
        return reverse_lazy('loan:list-emi',
                            kwargs={
                                'client_pk': self.kwargs.get('client_pk'),
                                'loan_pk': self.kwargs.get('loan_pk')
                            })