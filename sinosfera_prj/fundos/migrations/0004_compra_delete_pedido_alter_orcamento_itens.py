# Generated by Django 4.2.4 on 2023-09-02 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categorias', '0002_initial'),
        ('fundos', '0003_alter_pedido_orcamento'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.DecimalField(decimal_places=2, help_text='Especifique a quantidade que deseja adquirir considerando a unidade de medida do item de despesa.', max_digits=6, verbose_name='Quantidade')),
                ('preco_unitario', models.DecimalField(decimal_places=2, help_text='Especifique o preço unitário do item de orçamento.', max_digits=10, verbose_name='Preço unitário')),
                ('subtotal_da_compra', models.DecimalField(decimal_places=2, default=0, editable=False, max_digits=10, verbose_name='Subtotal do item de despesa')),
                ('item', models.ForeignKey(blank=True, help_text='Selecione o item de despesa para essa compra.', null=True, on_delete=django.db.models.deletion.CASCADE, to='fundos.item', verbose_name='Item de despesa')),
                ('orcamento', models.ForeignKey(blank=True, help_text='Selecione o orçamento a que esta compra de itens de despesa faz parte.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='fundos.orcamento', verbose_name='Orçamento a que esta compra pertence')),
                ('unidade', models.ForeignKey(blank=True, help_text='Selecione a unidade de medida do item de despesa.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='categorias.unidade_de_medida')),
            ],
            options={
                'verbose_name': 'Compra',
                'verbose_name_plural': 'Compras',
                'ordering': ('id',),
            },
        ),
        migrations.DeleteModel(
            name='Pedido',
        ),
        migrations.AlterField(
            model_name='orcamento',
            name='itens',
            field=models.ManyToManyField(through='fundos.Compra', to='fundos.item'),
        ),
    ]
