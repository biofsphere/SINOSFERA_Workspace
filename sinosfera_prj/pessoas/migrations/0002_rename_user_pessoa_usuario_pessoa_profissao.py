# Generated by Django 4.2.4 on 2023-08-25 11:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categorias', '0001_initial'),
        ('pessoas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pessoa',
            old_name='user',
            new_name='usuario',
        ),
        migrations.AddField(
            model_name='pessoa',
            name='profissao',
            field=models.ForeignKey(blank=True, help_text='Selecione a profissão da pessoa no cadastro', null=True, on_delete=django.db.models.deletion.SET_NULL, to='categorias.profissao'),
        ),
    ]
