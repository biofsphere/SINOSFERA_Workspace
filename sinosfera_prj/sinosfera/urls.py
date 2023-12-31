"""
URL configuration for sinosfera project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# from .admin import CustomAdminSite # to grab customized model order to admin panel
from django.urls import path, include

admin.site.site_header = 'Administração do SINOSFERA'
admin.site.site_title = 'SINOSFERA'
admin.site.index_title= 'Administração do SINOSFERA'
admin.site.site_url= '/admin'

# custom_admin_site = CustomAdminSite()
# admin.site = custom_admin_site # defines the admin site as the custom_admin_site with the customized order of models.

urlpatterns = [
    # path('grappelli/', include('grappelli.urls')), # grappelli URLS
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    # path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    # path('pessoas/', include('pessoas.urls')),
    path('chaining/', include('smart_selects.urls')),
    path('home/', include('home.urls')),
    path('locais/', include('locais.urls')),
    path('blog/', include('blog.urls')),
    path('dashboards/', include('dashboards.urls')),
    path('mapas/', include('mapas.urls')),
    path('relatorios/', include('relatorios.urls'))
]