# Generated by Django 4.2.4 on 2023-09-03 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categorias', '0004_categoria_de_publico'),
        ('projetos', '0005_publico'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publico',
            name='tipo',
        ),
        migrations.AddField(
            model_name='atividade',
            name='publico_total',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='publico',
            name='categoria',
            field=models.ForeignKey(blank=True, help_text='Selecione o tipo de público envolvido.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='categorias.categoria_de_publico', verbose_name='Categoria de público'),
        ),
        migrations.AlterField(
            model_name='publico',
            name='atividade',
            field=models.ForeignKey(blank=True, help_text='Selecione a atividade vinculada ao público envolvido.', null=True, on_delete=django.db.models.deletion.CASCADE, to='projetos.atividade', verbose_name='Atividade vinculada.'),
        ),
        migrations.AlterField(
            model_name='publico',
            name='descricao',
            field=models.CharField(blank=True, help_text='Inclua uma breve descrição do público envolvido.', max_length=250, null=True, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='publico',
            name='quantidade',
            field=models.PositiveIntegerField(default=0, help_text='Insira a quantidade de pessoas envolvidas da categoria selecionada.', verbose_name='QTD'),
        ),
    ]
