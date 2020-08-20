from django.forms.models import ModelForm

from .. import models


class DisrictForm(ModelForm):
    class Meta:
        model = models.District
        fields = ['name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'class': 'form-control form-control-user'}
        )
