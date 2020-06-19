from django import forms
from ..models import ConsultaPet

class ConsultaPetForm(forms.ModelForm):
    class Meta:
        model = ConsultaPet
        fields = ['motivo_consulta', ]
        exclude = ['pet', 'data']

