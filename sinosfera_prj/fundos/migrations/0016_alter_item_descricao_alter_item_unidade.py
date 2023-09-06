# Generated by Django 4.2.4 on 2023-09-06 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categorias', '0012_categoria_de_despesa'),
        ('fundos', '0015_alter_item_id_codificada'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='descricao',
            field=models.CharField(blank=True, help_text='Inclua uma breve descrição do item de despesa.', max_length=80, null=True, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='item',
            name='unidade',
            field=models.ForeignKey(blank=True, default='un', help_text='Selecione a unidade de medida do ítem de despesa no orçamento.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='categorias.unidade_de_medida', verbose_name='Un'),
        ),
    ]
