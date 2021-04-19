from django import forms

class MunicipioForm(forms.Form):
    municipio = forms.CharField(label='Informe um municipio')