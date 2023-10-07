from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from django.contrib.gis import admin
from leaflet.admin import LeafletGeoAdmin
from .models import Microbacia, Municipio, Unidade_de_referencia
# from core.admin import custom_admin_site

@admin.register(Microbacia)
class MicrobaciaAdmin(admin.ModelAdmin):
    fields = ('id', 'nome',)
    readonly_fields = ('id',)
    list_display = ('id', 'nome',)
    search_fields = ('nome',)
    ordering = ('id', 'nome',)
    # list_filter = ('municipio',)


@admin.register(Municipio)
class MunicipioAdmin(admin.ModelAdmin):
    fields = ('id', 'nome',)
    readonly_fields = ('id',)
    list_display = ('id', 'nome',)
    search_fields = ('nome',)
    ordering = ('id', 'nome',)
    # list_filter = ('municipio',)


@admin.register(Unidade_de_referencia)
class Unidade_de_referenciaAdmin(LeafletGeoAdmin):
    fields = ('id', 'nome', 'proprietario_pf_de_ur', 'proprietario_pj_de_ur', 'municipio_da_ur', 'localizacao',)
    readonly_fields = ('id',)
    list_display = ('id', 'nome', 'proprietario_pf_de_ur', 'proprietario_pj_de_ur', 'municipio_da_ur', 'localizacao',)
    search_fields = ('nome', 'municipio_da_ur',)
    ordering = ('id', 'nome', 'municipio_da_ur',)
    list_filter = ('municipio_da_ur',)

