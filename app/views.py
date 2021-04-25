from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404
from django.db.models import F, Func
from .models import Municipios, Estados
from django.db import connection, connections
from .forms import TechForm
from pymongo import MongoClient
from user.forms import ProfileForm


def profile(request):
    #mongo_client = MongoClient('172.19.0.2', 27017)
    mongo_client = MongoClient()
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


def mapView(request):
    mongo_client = MongoClient()
    mongodb = mongo_client['LOOKING']

    cursor = connections['postgis'].cursor()

    cursor.execute("SELECT getViewBox(%s)", ['Paraíba'])
    viewbox = cursor.fetchone()

    cursor.execute("SELECT ST_AsSVG(EST.GEOM) FROM ESTADOS EST WHERE EST.NOME = %s", ['Paraíba'])
    svg_estado = cursor.fetchone()

    looking = mongodb.looking.find({})
    svg_municipio = []
    perfis = []

    form = TechForm(request.POST or None)

    if form.is_valid():
        input = form.cleaned_data.get('tecnologia')
        looking = mongodb['looking'].find({"tecnologias": {'$regex': input}})

    for each in looking:
        cursor.execute("SELECT ST_AsSVG(MUN.GEOM), MUN.NOME FROM MUNICIPIOS MUN WHERE MUN.NOME ILIKE %s AND MUN.SIGLA_UF LIKE 'PB'", [each['cidade']])
        svg = cursor.fetchone()
        svg_municipio.append({'svg': svg[0], 'cidade': svg[1]})

        perfis.append({
            'cidade': each['cidade'],
            'nome': each['nome'],
            'tecnologias': each['tecnologias']
        })


    context = {
        'svgMunicipio': svg_municipio,
        'svgEstado': svg_estado[0],
        'viewbox': viewbox[0],
        'form': form,
        'perfis': perfis
    }

    return render(request, 'index.html', context)


# def mapView(request):
#     mongo_client = MongoClient()
#     mongodb = mongo_client['LOOKING']
#
#     form = MunicipioForm(request.POST or None)
#     viewbox = ['']
#     svg_municipio = ['']
#     svg_estado = ['']
#
#     if form.is_valid():
#         input = form.cleaned_data.get('municipio')
#
#         municipio = Municipios.objects.using('postgis').get(nome__icontains=input, sigla_uf='PB') #__icontains = ILIKE
#         estado = Estados.objects.using('postgis').get(sigla_uf=municipio.sigla_uf)
#
#         cursor = connections['postgis'].cursor()
#         cursor.execute("SELECT getViewBox(%s)", [estado.nome])
#         viewbox = cursor.fetchone()
#
#         cursor.execute("SELECT ST_AsSVG(MUN.GEOM) FROM MUNICIPIOS MUN WHERE MUN.NOME ILIKE %s AND MUN.SIGLA_UF LIKE 'PB'", [municipio.nome])
#         svg_municipio = cursor.fetchone()
#
#         cursor.execute("SELECT ST_AsSVG(EST.GEOM) FROM ESTADOS EST WHERE EST.NOME = %s", [estado.nome])
#         svg_estado = cursor.fetchone()
#
#     context = {
#         'svgMunicipio': svg_municipio[0],
#         'svgEstado': svg_estado[0],
#         'viewbox': viewbox[0],
#         'form': form
#     }
#
#     #test = User.objects.using('mongodb').all().first() #.get(codigo=1)
#
#     #looking = mongodb['looking'].find_one({"nome": {'$regex': 'ch'}})
#
#     # looking = mongodb.looking
#     #
#     # user = {
#     #     'codigo': 2,
#     #     'nome': 'Test',
#     #     'django': 0,
#     #     'java': 1
#     # }
#     #
#     # looking = looking.insert_one(user).inserted_id
#     #
#     # print(looking)
#     #
#     return render(request, 'index.html', context)
