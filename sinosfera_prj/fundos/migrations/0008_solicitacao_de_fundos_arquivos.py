# Generated by Django 4.2.4 on 2023-08-30 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fundos', '0007_alter_solicitacao_de_fundos_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitacao_de_fundos',
            name='arquivos',
            field=models.FileField(blank=True, null=True, upload_to='fundos/solicitacoes'),
        ),
    ]