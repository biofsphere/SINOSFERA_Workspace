# Generated by Django 4.2.4 on 2023-09-04 23:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pessoas', '0002_remove_pessoa_perfil_atualizado_em_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pessoa',
            name='usuario',
        ),
    ]
