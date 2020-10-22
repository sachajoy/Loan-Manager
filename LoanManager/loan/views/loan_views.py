import calendar
from datetime import date

from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DetailView)

from .. import models
from ..forms import loan_forms


def add_months(sourcedate, months):
    month = sourcedate.month - 1 + months
    year = sourcedate.year + month // 12
    month = month % 12 + 1
    day = min(sourcedate.day, calendar.monthrange(year, month)[1])
    return date(year, month, day)


class LoanCreateView(CreateView):
    models = models.Loan
    form_class = loan_forms.LoanForm
    template_name = 'loan/loan_form.html'

    def form_valid(self, form):
        form.instance.client_id = self.kwargs.get('client_pk')
        self.object = form.save()
        loan = models.Loan.objects.get(pk=self.object.pk)
        client = models.Client.objects.get(pk=self.kwargs.get('client_pk'))
        for i in range(0, loan.months):
            emi = models.Emi()
            emi.loan_id = loan
            emi.client_id = client
            # emi.amt = loan.emi_amt
            emi.due_date = add_months(loan.agrmnt_date, i)
            emi.penalty = 0
            emi.save()

        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super(LoanCreateView, self).get_context_data(**kwargs)
        context['client'] = models.Client.objects.get(pk=self.kwargs.get('client_pk'))
        return context

    def get_success_url(self):
        return reverse_lazy('loan:loan-detail',
                            kwargs={
                                'client_pk': self.kwargs.get('client_pk'),
                                'pk': self.object.pk
                            })


class LoanDetailView(DetailView):
    model = models.Loan
    context_object_name = 'loan_details'

    def get_context_data(self, **kwargs):
        context = super(LoanDetailView, self).get_context_data(**kwargs)
        context['client'] = models.Client.objects.get(pk=self.kwargs.get('client_pk'))
        return context
