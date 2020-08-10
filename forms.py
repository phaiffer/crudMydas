from django import forms
from .models import Pais, Estado

class PaisForm(forms.ModelForm):
    class Meta:
        model = Pais
        fields = ['nome','sigla']

class EstadoForm(forms.ModelForm):
    class Meta:
        model = Estado
        fields = ['nome_estado','sigla_estado']