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


class TalukaForm(ModelForm):
    class Meta:
        model = models.Taluka
        fields = ['district_id', 'name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fields_name, fields in self.fields.items():
            fields.widget.attrs.update(
                {'class': 'form-control form-control-user'}
            )


class VillageForm(ModelForm):
    class Meta:
        model = models.Village
        fields = ['taluka_id', 'name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fields_name, fields in self.fields.items():
            fields.widget.attrs.update(
                {'class': 'form-control form-control-user'}
            )



class FaliyaForm(ModelForm):
    class Meta:
        model = models.Faliya
        fields = ['village_id', 'name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fields_name, fields in self.fields.items():
            fields.widget.attrs.update(
                {'class': 'form-control form-control-user'}
            )
