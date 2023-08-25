# Generated by Django 4.2.4 on 2023-08-25 11:48

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('locais', '0002_microbacia_alter_municipio_nome_and_more'),
        ('pessoas', '0002_rename_user_pessoa_usuario_pessoa_profissao'),
        ('projetos', '0001_initial'),
        ('instituicoes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Solicitacao_de_fundos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_da_solicitacao', models.DateField(blank=True, default=datetime.date.today, verbose_name='Data da solicitação de fundos')),
                ('cronograma', models.TextField(blank=True, help_text='Especifique um cronograma ou período estimado de relaização das atividades com os fundos solicitados.', max_length=300, null=True, verbose_name='Cronograma de execução')),
                ('urgencia', models.CharField(choices=[('Alta', 'ALTA'), ('Média', 'MÉDIA'), ('Baixa', 'BAIXA')], help_text='Selecione o caráter de urgência para liberação de fundos.', max_length=5, verbose_name='Caráter de urgência')),
                ('observacoes', models.TextField(blank=True, help_text='Inclua quaiquer observações que considerar necessário.', null=True, verbose_name='Observações')),
                ('atividade_vinculada', models.ForeignKey(blank=True, help_text='Selecione a(s) atividade(s) a que esta solicitação está diretamente vinculada.', null=True, on_delete=django.db.models.deletion.CASCADE, to='projetos.atividade')),
                ('etapa_vinculada', models.ForeignKey(blank=True, help_text='Selecione a(s) etapa(s) a que esta solicitação está diretamente vinculada, se houver', null=True, on_delete=django.db.models.deletion.SET_NULL, to='projetos.etapa', verbose_name='Etapa vinculada')),
                ('municipio_solicitante', models.ForeignKey(blank=True, help_text='Selecione o município para onde irão os fundos', null=True, on_delete=django.db.models.deletion.SET_NULL, to='locais.municipio', verbose_name='Município vinculado à solicitação de fundos')),
                ('objetivo_especifico_vinculado', models.ForeignKey(blank=True, help_text='Selecione o objetivo específico a que esta solicitação está diretamente vincula.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='projetos.objetivo_especifico_de_projeto', verbose_name='Objetivo específico vinculado à solicitação de fundos')),
                ('projeto_vinculado', models.ForeignKey(blank=True, help_text='Selecione o projeto a que esta solicitação está diretamente vinculada.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='projetos.projeto', verbose_name='Projeto vinculado à solicitação de fundos')),
                ('responsavel_pelo_preenchimento', models.ForeignKey(blank=True, help_text='Selecione a pessoa responsável pelo preenchimento desta solicitação.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='pessoas.pessoa', verbose_name='Responsável pelo preenchimento da solicitação de fundos')),
                ('ur_vinculada', models.OneToOneField(blank=True, help_text='Selecione a UR a que esta solicitação está diretamente vinculada, se houver.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='locais.unidade_de_referencia', verbose_name='UR vinculada à solicitação de fundos')),
            ],
        ),
        migrations.CreateModel(
            name='orcamento_para_solicitacao_de_fundos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_do_orcamento', models.DateField(blank=True, help_text='Identifique o orçamento informado a sua data de emissão e selecione a data aqui.', null=True)),
                ('inclui', models.TextField(blank=True, help_text='Descreva tudo que está icluso no valor total do orçamento, especificando detalhes dos serviços quando for o caso.', null=True, verbose_name='Descritivo do que está incluso no orçamento')),
                ('exclui', models.TextField(blank=True, help_text='Descreva o que o orçameto não inclui, quando pertinente.', null=True, verbose_name='Descritivo do que não está incluso no orçamento')),
                ('validade', models.PositiveIntegerField(blank=True, help_text='Especifique em número de dias a validade do orçamento.', null=True)),
                ('forma_de_garantia', models.CharField(blank=True, help_text='Explicite a forma e tempo de garantia do produto ou serviços estabelecida pelo fornecedor.', max_length=200, null=True)),
                ('valor_total_do_orcamento', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('dados_para_pagamento', models.TextField(blank=True, help_text='Inclua os dados para pagamento deste orçamento conforme preferência do fornecedor.', null=True, verbose_name='Dados para pagamento')),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
                ('arquivos', models.FileField(blank=True, null=True, upload_to='fundos/orcamentos')),
                ('empresa_fornecedora', models.ForeignKey(blank=True, help_text='Seleciona a instituição fornecedora do orçamento. Se não houver, clique em "+" para inserir.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='instituicoes.instituicao', verbose_name='Empresa fornecedora')),
                ('profissional_fornecedor', models.ForeignKey(blank=True, help_text='Selecione o profissional fornecedor. Senão houver, clieque em "+" para inserir.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='pessoas.pessoa')),
                ('solicitacao_de_fundos', models.ForeignKey(blank=True, help_text='Selecione a solicitação de fundos na qual este orçamento pertence.', null=True, on_delete=django.db.models.deletion.CASCADE, to='fundos.solicitacao_de_fundos')),
            ],
            options={
                'verbose_name': 'Orçamento',
                'verbose_name_plural': 'Orçamentos',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Item_de_orcamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, help_text='Insira o nome to serviço, material ou maquinário (item de orçamento)', max_length=120, null=True)),
                ('quantidade', models.PositiveIntegerField(help_text='Especifique a quantidade que deseja adquirir considerando a unidade de medida especificada.')),
                ('unidade_de_medida', models.CharField(blank=True, help_text='Especifique a unidade de medida deste ítem de orçamento', max_length=20, null=True)),
                ('preco_unitario', models.DecimalField(decimal_places=2, help_text='Especifique o preço unitário do item de orçamento.', max_digits=10)),
                ('preco_total_do_item', models.DecimalField(decimal_places=2, editable=False, max_digits=10)),
                ('orcamento', models.ForeignKey(help_text='Selecione o orçamento no qual este item pertence.', on_delete=django.db.models.deletion.CASCADE, related_name='itens_orcados', to='fundos.orcamento_para_solicitacao_de_fundos')),
            ],
            options={
                'verbose_name': 'Item de orçamento',
                'verbose_name_plural': 'Itens de orçamento',
                'ordering': ('id',),
            },
        ),
    ]
