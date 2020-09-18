from django import forms
from django.forms.models import ModelForm

from .. import models


class ClientForm(ModelForm):
    class Meta:
        model = models.Client
        fields = ('fname', 'firm_id',
                  'challan_no', 'file_no',
                  'mname', 'lname',
                  'addr', 'faliya',
                  'mob_no', 'gtr',
                  'gtr_mob_no'
                  )
        widgets = {
            'challan_no': forms.TextInput(attrs={'placeholder': 'Challan Number'}),
            'file_no': forms.TextInput(attrs={'placeholder': 'File Number'}),
            'fname': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'mname': forms.TextInput(attrs={'placeholder': 'Middle Name'}),
            'lname': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'addr': forms.TextInput(attrs={'placeholder': 'Address'}),
            'mob_no': forms.TextInput(attrs={'placeholder': 'Mobile Number'}),
            'gtr': forms.TextInput(attrs={'placeholder': 'Grauntor Name'}),
            'gtr_mob_no': forms.TextInput(attrs={'placeholder': 'Grauntor Mob No'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fields_name, fields in self.fields.items():
            fields.widget.attrs.update(
                {'class': 'form-control form-control-user'}
            )
