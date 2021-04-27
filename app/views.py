from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.shortcuts import render
from finalProject import settings
from django.db import connections
from .forms import TechForm
from pymongo import MongoClient
from django.views.decorators.cache import cache_page


CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)
mongo_client = MongoClient()
# mongo_client = MongoClient('172.19.0.2', 27017)

@cache_page(CACHE_TTL)
def mapView(request):
    mongodb = mongo_client['LOOKING']

    cursor = connections['postgis'].cursor()

    cursor.execute("SELECT getViewBox(%s)", ['Paraíba'])
    viewbox = cursor.fetchone()

    cursor.execute("SELECT ST_AsSVG(EST.GEOM) FROM ESTADOS EST WHERE EST.NOME = %s", ['Paraíba'])
    svg_estado = cursor.fetchone()

    looking = mongodb.looking.find({'ativo': True})
    svg_municipio = []
    perfis = []

    form = TechForm(request.POST or None)

    if form.is_valid():
        input = form.cleaned_data.get('tecnologia')
        looking = mongodb['looking'].find({"tecnologias": {'$regex': input, '$options': 'i'}})
    for each in looking:
        cursor.execute("SELECT ST_AsSVG(MUN.GEOM), MUN.NOME FROM MUNICIPIOS MUN WHERE MUN.NOME ILIKE %s AND MUN.SIGLA_UF LIKE 'PB'", [each['cidade']])
        svg = cursor.fetchone()
        svg_municipio.append({'svg': svg[0], 'cidade': svg[1]})

        perfis.append({
            'cidade': each['cidade'],
            'nome': each['nome'],
            'email': each['email'],
            'endereco': each['rua'] + ' - ' + str(each['numero']) + ' - ' + each['bairro'],
            'bio': each['bio'],
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