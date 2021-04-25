from django import forms


class TechForm(forms.Form):
    tecnologia = forms.CharField(label='Filtre por tecnologia:')

