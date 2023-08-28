# from django.contrib import admin
# from pessoas.models import *
# from instituicoes.models import *
# from locais.models import *
# from planos.models import *
# from programas.models import *
# from projetos.models import *
# from fundos.models import *

# class CustomAdminSite(admin.AdminSite):
#     model_ordering = {
#         'pessoas': [CustomUser, Pessoa,],
#         'instituicoes': [Instituicao,],
#         'locais': [Microbacia, Municipio, Unidade_de_referencia,],
#         'planos': [Plano, Programa_de_acoes_prioritarias, Acao_prioritaria],
#         'programas': [Programa, Diretriz_especifica_de_programa,],
#         'projetos': [Projeto, Objetivo_especifico_de_projeto, Etapa, Atividade,],
#         'fundos': [Solicitacao_de_fundos, Orcamento, Pedido_de_item, Item,],
#     }

#     def get_app_list(self, request):
#         app_list = super().get_app_list(request)
#         for app_label, models in self.model_ordering.items():
#             app = next((app for app in app_list if app['app_label'] == app_label), None)
#             if app:
#                 app['models'] = sorted(app['models'], key=lambda x: models.index(x['object_name']))
#         return app_list