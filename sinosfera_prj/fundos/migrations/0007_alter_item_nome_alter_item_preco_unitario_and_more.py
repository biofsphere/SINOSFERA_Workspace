# Generated by Django 4.2.4 on 2023-09-03 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categorias', '0003_alter_categoria_de_plano_options'),
        ('fundos', '0006_remove_orcamento_itens_item_orcamento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='nome',
            field=models.CharField(blank=True, help_text='Insira o nome ou título do serviço, material ou maquinário (item de despesa no orçamento)', max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='preco_unitario',
            field=models.DecimalField(decimal_places=2, default=0, help_text='Especifique o preço unitário do item de orçamento.', max_digits=10, verbose_name='Preço Un.'),
        ),
        migrations.AlterField(
            model_name='item',
            name='quantidade',
            field=models.DecimalField(decimal_places=2, default=0, help_text='Especifique a quantidade que deseja adquirir considerando a unidade de medida do item de despesa.', max_digits=6, verbose_name='QTD'),
        ),
        migrations.AlterField(
            model_name='item',
            name='subtotal_do_item',
            field=models.DecimalField(decimal_places=2, default=0, editable=False, max_digits=10, verbose_name='Subtotal'),
        ),
        migrations.AlterField(
            model_name='item',
            name='tipo',
            field=models.CharField(blank=True, choices=[('MOB', 'Mão de obra ou serviços'), ('REF', 'Refeições ou alimentação'), ('TRA', 'Frete ou transporte'), ('FMA', 'Ferramentas manuais'), ('FMO', 'Ferramentas motorizadas'), ('MTC', 'Materiais de construção'), ('INS', 'Materiais escolares'), ('AGR', 'Insumo agropecuário'), ('EQU', 'Equipamentos de TI'), ('MOV', 'Móveis'), ('PCO', 'Peças de comunicação'), ('ROA', 'Roupas ou acessórios'), ('OUT', 'Outros')], help_text='Selecione o tipo mais adequado de despesa.', max_length=3, null=True, verbose_name='Tipo de despesa'),
        ),
        migrations.AlterField(
            model_name='item',
            name='unidade',
            field=models.ForeignKey(blank=True, help_text='Selecione a unidade de medida do ítem de despesa no orçamento.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='categorias.unidade_de_medida', verbose_name='UN'),
        ),
    ]
