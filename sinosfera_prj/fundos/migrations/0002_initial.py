# Generated by Django 4.2.4 on 2023-09-02 00:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projetos', '0001_initial'),
        ('instituicoes', '0001_initial'),
        ('fundos', '0001_initial'),
        ('locais', '0001_initial'),
        ('categorias', '0002_initial'),
        ('pessoas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='requisicao',
            name='atividade_vinculada',
            field=models.ManyToManyField(blank=True, help_text='Selecione a(s) atividade(s) a que esta solicitação está diretamente vinculada.', to='projetos.atividade'),
        ),
        migrations.AddField(
            model_name='requisicao',
            name='etapa_vinculada',
            field=models.ManyToManyField(blank=True, help_text='Selecione a(s) etapa(s) a que esta solicitação está diretamente vinculada, se houver', to='projetos.etapa', verbose_name='Etapa(s) vinculada(s)'),
        ),
        migrations.AddField(
            model_name='requisicao',
            name='fundo_solicitado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='categorias.fundo', verbose_name='Fundo de financiamento'),
        ),
        migrations.AddField(
            model_name='requisicao',
            name='instituicao_solicitante',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='instituicoes.instituicao', verbose_name='Insituição solicitante'),
        ),
        migrations.AddField(
            model_name='requisicao',
            name='municipio',
            field=models.ForeignKey(blank=True, help_text='Selecione o município para onde irão os fundos', null=True, on_delete=django.db.models.deletion.SET_NULL, to='locais.municipio', verbose_name='Município solicitante'),
        ),
        migrations.AddField(
            model_name='requisicao',
            name='objetivo_especifico_vinculado',
            field=models.ManyToManyField(blank=True, help_text='Selecione o objetivo específico a que esta solicitação está diretamente vincula.', to='projetos.objetivo_especifico_de_projeto', verbose_name='Objetivo(s) específico(s) vinculado(s) à solicitação de fundos'),
        ),
        migrations.AddField(
            model_name='requisicao',
            name='projeto_vinculado',
            field=models.ForeignKey(blank=True, help_text='Selecione o projeto a que esta solicitação está diretamente vinculada.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='projetos.projeto', verbose_name='Projeto vinculado à solicitação de fundos'),
        ),
        migrations.AddField(
            model_name='requisicao',
            name='responsavel_pelo_preenchimento',
            field=models.ForeignKey(blank=True, help_text='Selecione a pessoa responsável pelo preenchimento desta solicitação.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='pessoas.pessoa', verbose_name='Responsável pelo preenchimento'),
        ),
        migrations.AddField(
            model_name='requisicao',
            name='ur_vinculada',
            field=models.ManyToManyField(blank=True, help_text='Selecione uma ou mais URs destino dos fundos dessa solicitação, se houver.', to='locais.unidade_de_referencia', verbose_name='UR(s) vinculada(s) à solicitação de fundos'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='item',
            field=models.ForeignKey(blank=True, help_text='Selecione o item de despesa para esse pedido.', null=True, on_delete=django.db.models.deletion.CASCADE, to='fundos.item', verbose_name='Item de despesa'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='orcamento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='fundos.orcamento', verbose_name='Selecione o orçamento a que este item de despesa faz parte.'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='unidade',
            field=models.ForeignKey(blank=True, help_text='Selecione a unidade de medida do item de despesa.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='categorias.unidade_de_medida'),
        ),
        migrations.AddField(
            model_name='orcamento',
            name='empresa_fornecedora',
            field=models.ForeignKey(blank=True, help_text='Seleciona a instituição fornecedora do orçamento. Se não houver, clique em "+" para inserir.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='instituicoes.instituicao', verbose_name='Empresa fornecedora'),
        ),
        migrations.AddField(
            model_name='orcamento',
            name='itens',
            field=models.ManyToManyField(through='fundos.Pedido', to='fundos.item'),
        ),
        migrations.AddField(
            model_name='orcamento',
            name='profissional_fornecedor',
            field=models.ForeignKey(blank=True, help_text='Selecione o profissional fornecedor. Senão houver, clieque em "+" para inserir.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='pessoas.pessoa'),
        ),
        migrations.AddField(
            model_name='orcamento',
            name='requisicao',
            field=models.ForeignKey(blank=True, help_text='Selecione a Requisição de Fundos em que este Orçamento faz parte.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='fundos.requisicao', verbose_name='Requisição de Fundos'),
        ),
        migrations.AddField(
            model_name='item',
            name='unidade',
            field=models.ForeignKey(blank=True, help_text='Selecione a unidade de medida do ítem de despesa no orçamento.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='categorias.unidade_de_medida', verbose_name='Un.'),
        ),
    ]