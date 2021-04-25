from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from pymongo import MongoClient

from user.forms import ProfileForm
from django.shortcuts import render
import sqlite3

mongo_client = MongoClient()
# mongo_client = MongoClient('172.19.0.2', 27017)

class Register(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'


def index(request):
    return redirect('map')


def profile(request):
    form = ProfileForm(request.POST)
    current_user = request.user
    mongodb = mongo_client['LOOKING']

    looking = mongodb.looking

    temPerfil = looking.find({'username': current_user.username})

    if request.method == 'GET':

        if temPerfil:
            for perfil in temPerfil:
                info = {
                    'username': current_user.username,
                    'nome': perfil['nome'],
                    'email': perfil['email'],
                    'rua': perfil['rua'],
                    'numero': perfil['numero'],
                    'bairro': perfil['bairro'],
                    'cidade': perfil['cidade'],
                    'bio': perfil['bio'],
                    'tecnologias': perfil['tecnologias'],
                    'ativo': perfil['ativo']
                }
                form = ProfileForm(info)
        else:
            info = {''}

    if request.method == 'POST':
        if form.is_valid():
            nome = form.cleaned_data.get('nome')
            email = form.cleaned_data.get('email')
            rua = form.cleaned_data.get('rua')
            numero = form.cleaned_data.get('numero')
            bairro = form.cleaned_data.get('bairro')
            cidade = form.cleaned_data.get('cidade')
            bio = form.cleaned_data.get('bio')
            tecnologias = form.cleaned_data.get('tecnologias')
            ativo = form.cleaned_data.get('ativo')

            json = {
                'username': current_user.username,
                'nome': nome,
                'email': email,
                'rua': rua,
                'numero': numero,
                'bairro': bairro,
                'cidade': cidade,
                'bio': bio,
                'tecnologias': tecnologias,
                'ativo': ativo
            }

            if temPerfil:
                looking.delete_one({'username': current_user.username})
                looking = looking.insert_one(json).inserted_id
                print(json)
            else:
                looking = looking.insert_one(json).inserted_id
                print('nao')

    context = {
        'form': form
    }

    return render(request, 'profile.html', context)
