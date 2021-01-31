from datetime import date

from django.db.models import Sum
from django.shortcuts import render

from .. import models


def index(request):
    days_collection = models.Emi.objects.filter(due_date=date.today()).aggregate(abc=Sum('emi_amt'))
    days_collected = models.Emi.objects.filter(due_date=date.today()).aggregate(abc=Sum('amt'))
    days_rem = models.Emi.objects.filter(due_date=date.today()).aggregate(abc=Sum('emi_amt') - Sum('amt'))
    month_collection = models.Emi.objects.filter(due_date__month=date.today().month, due_date__year=date.today().year).aggregate(abc=Sum('emi_amt'))
    month_collected = models.Emi.objects.filter(due_date__month=date.today().month, due_date__year=date.today().year).aggregate(abc=Sum('amt'))
    month_rem = models.Emi.objects.filter(due_date__month=date.today().month, due_date__year=date.today().year).aggregate(abc=Sum('emi_amt') - Sum('amt'))
    month_per = ((month_collected['abc']) * 100) / (month_collection['abc'])
    print(type(days_rem))
    per = 100
    context = {
        'collection': days_collection,
        'collected': days_collected,
        'rem': days_rem,
        'per':per,
        'month_coll':month_collection,
        'month_due':month_collected,
        'month_rem':month_rem,
        'per_mon':month_per
    }
    return render(request, "loan/template.html", context)
