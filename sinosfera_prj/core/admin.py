"""
    This model is an attempt to reorder apps and models in the admin interface.
    It instantiates the clas CustoAmdinSite in a varible called custom_admin_site
    that is then used in the admin.py files of each app.
"""
from django.contrib import admin

from django.contrib.admin.sites import AdminSite
from pessoas.models import Pessoa, CustomUser
from instituicoes.models import Instituicao
from locais.models import Microbacia, Municipio, Unidade_de_referencia
from planos.models import Plano, Programa_de_acoes_prioritarias, Acao_prioritaria
from programas.models import Programa, Diretriz_especifica_de_programa
from projetos.models import Projeto, Subprojeto, Etapa, Atividade

class CustomAdminSite(AdminSite):
    def get_app_list(self, request):
        app_list = super().get_app_list(request)

        # Define the desired order of apps and models
        custom_order = {
            'pessoas': [CustomUser, Pessoa],
            'instituicoes': [Instituicao],
            'locais': [Microbacia, Municipio, Unidade_de_referencia],
            'planos': [Plano, Programa_de_acoes_prioritarias, Acao_prioritaria],
            'programas': [Programa, Diretriz_especifica_de_programa],
            'projetos': [Projeto, Subprojeto, Etapa, Atividade],
        }

        # Print the original app_list
        print("Original app_list:")
        print(app_list)

        # Rearrange the app_list based on the custom_order
        ordered_app_list = []
        for app_name in custom_order:
            app_info = next(app for app in app_list if app['name'] == app_name)
            if app_info:
                app_info['models'] = [
                    model_info for model_info in app_info['models'] if model_info['name'] in [model.__name__ for model in custom_order[app_name]]
                ]
                ordered_app_list.append(app_info)
        
        # Print the ordered_app_list
        print("Ordered app_list:")
        print(ordered_app_list)
        
        return ordered_app_list

# Create an instance of the CustomAdminSite
custom_admin_site = CustomAdminSite(name='customadmin')
