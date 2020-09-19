from django import forms
from django.forms.models import ModelForm

from .. import models
import datetime

class LoanForm(ModelForm):
    class Meta:
        fields = [
            'vehical', 'reg_no',
            'agrmnt_date', 'chasis_no', 'engine_no',
            'principle_amt', 'intrest_rate', 'emi_amt',
            'months'
        ]
        model = models.Loan
        widgets = {
            # 'client_id': forms.Select(),
            'reg_no': forms.TextInput(attrs={'placeholder': 'Registration Number'}),
            'chasis_no': forms.TextInput(attrs={'placeholder': 'Chasis Number'}),
            'engine_no': forms.TextInput(attrs={'placeholder': 'Engine Number'}),
            'principle_amt': forms.NumberInput(attrs={'placeholder': 'Engine Number'}),
            'agrmnt_date': forms.DateInput(attrs={'type': 'date'}, )
        }

        def __init__(self, *args, **kwargs):
            super.__init__(*args, **kwargs)
            for fields_name, fields in self.fields.items():
                fields.widget.attrs.update(
                    {'class': 'form-control form-control-user'}
                )
