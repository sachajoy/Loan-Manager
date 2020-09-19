from django.urls import reverse_lazy
from django.views.generic import (CreateView, DetailView)

from .. import models
from ..forms import loan_forms


class LoanCreateView(CreateView):
    models = models.Loan
    form_class = loan_forms.LoanForm
    template_name = 'loan/loan_form.html'

    def form_valid(self, form):
        client = self.kwargs.get('client_pk')
        form.instance.client_id = client
        return super(LoanCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(LoanCreateView, self).get_context_data(**kwargs)
        context['client'] = models.Client.objects.get(pk=self.kwargs.get('client_pk'))
        return context

    def get_success_url(self):
        return reverse_lazy('loan:loan-detail',
                            kwargs={'client_pk': self.kwargs.get('client_pk'), 'pk': self.object.pk})


class LoanDetailView(DetailView):
    model = models.Loan
    context_object_name = 'loan_details'

    def get_context_data(self, **kwargs):
        context = super(LoanDetailView, self).get_context_data(**kwargs)
        context['client'] = models.Client.objects.get(pk=self.kwargs.get('client_pk'))
        return context
