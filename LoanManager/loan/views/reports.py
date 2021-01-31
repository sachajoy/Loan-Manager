from django.views.generic import ListView
# from django.http import HttpResponse
from _datetime import date

from ..models import Emi


class FetchDefaultersListView(ListView):
    model = Emi
    template_name = 'loan/defaulters_list.html'
    context_object_name = 'emis'

    def get_queryset(self):
        if self.request.method == 'GET':
            start_date = self.request.GET.get('start_date')
            end_date = self.request.GET.get('end_date')
            if(start_date == None or end_date == None):
                return Emi.objects.filter(amt__exact=0, due_date__lt=date.today())
            return Emi.objects.filter(due_date__gt=start_date, due_date__lt=end_date, amt__exact=0)
