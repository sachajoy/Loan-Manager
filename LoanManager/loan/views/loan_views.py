from django.shortcuts import get_object_or_404
from django.views.generic import (CreateView)

from .. import models
from ..forms import loan_forms


class LoanCreateView(CreateView):
    models = models.Loan
    form_class = loan_forms.LoanForm
    template_name = 'loan/loan_form.html'

    def form_valid(self, form):
        client = get_object_or_404(models.Client, pk=self.kwargs.get('client_pk'))
        form.instance.client_id = client
        return super(LoanCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(LoanCreateView, self).get_context_data(**kwargs)
        context['client'] = models.Client.objects.get(pk=self.kwargs.get('client_pk'))
        return context
