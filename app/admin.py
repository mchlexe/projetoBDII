from django.contrib import admin
from .models import Usuario


class ListandoUsuarios(admin.ModelAdmin):
    list_display = ('cod', 'nome', 'email')
    list_display_links = ('cod', 'nome')
    search_fields = ('cod',)
    # list_filter = ('nome',)
    list_per_page = 20


# Register your models here.
admin.site.register(Usuario, ListandoUsuarios)
