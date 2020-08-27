from django.forms.models import ModelForm

from .. import models


class ClientForm(ModelForm):
    class Meta:
        fields = ['firm_id', 'challan_no',
                  'file_no', 'fname',
                  'mname', 'lname',
                  'addr', 'faliya',
                  'mob_no', 'gtr',
                  'gtr_mob_no']
        model = models.Client

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for fields_name, fields in self.fields.items():
                fields.widget.attrs.update(
                    {'class': 'form-control form-control-user'}
                )
