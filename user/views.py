from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from pymongo import MongoClient
from user.forms import ProfileForm
from django.shortcuts import render
import sqlite3

class Register(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'

def index(request):
    return redirect('login')

def profile(request):
    mongo_client = MongoClient('172.19.0.2', 27017)
    # mongo_client = MongoClient()
    mongodb = mongo_client['LOOKING']

    looking = mongodb.looking

    form = ProfileForm(request.POST)
    nome = ''
    email = ''
    rua = ''
    numero = ''
    bairro = ''
    cidade = ''
    bio = ''
    tecnologias = ''


    if form.is_valid():
        nome = form.cleaned_data.get('nome')
        email = form.cleaned_data.get('email')
        rua = form.cleaned_data.get('rua')
        numero = form.cleaned_data.get('numero')
        bairro = form.cleaned_data.get('bairro')
        cidade = form.cleaned_data.get('cidade')
        bio = form.cleaned_data.get('bio')
        tecnologias = form.cleaned_data.get('tecnologias')

        json = {
            # 'user': user.username,
            'nome': nome,
            'email': email,
            'rua': rua,
            'numero': numero,
            'bairro': bairro,
            'cidade': cidade,
            'bio': bio,
            'tecnologias': tecnologias
        }

        looking = looking.insert_one(json).inserted_id

        #print(json)

    context = {
        'form': form
    }
    return render(request, 'profile.html', context)