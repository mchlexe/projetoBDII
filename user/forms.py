from django import forms

class ProfileForm(forms.Form):
    nome = forms.CharField(label='Nome')
    email = forms.EmailField(label='E-mail')
    rua = forms.CharField(label='Rua')
    numero = forms.IntegerField(label='Numero')
    bairro = forms.CharField(label='Bairro')
    cidade = forms.CharField(label='Cidade')
    bio = forms.CharField(label='Bio')
    tecnologias = forms.CharField(label='Tecnologias')
    ativo = forms.BooleanField(label='Perfil visível',required=False)