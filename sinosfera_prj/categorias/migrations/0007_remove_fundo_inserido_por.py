# Generated by Django 4.2.4 on 2023-09-03 20:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categorias', '0006_fundo_inserido_por'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fundo',
            name='inserido_por',
        ),
    ]
