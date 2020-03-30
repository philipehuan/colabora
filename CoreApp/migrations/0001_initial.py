# Generated by Django 3.0 on 2020-03-24 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Colaborador',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=60)),
                ('nascimento', models.DateField()),
                ('rg', models.CharField(max_length=15)),
                ('cpf', models.CharField(max_length=15)),
                ('telefone', models.CharField(blank=True, max_length=12, null=True)),
                ('cnh', models.CharField(blank=True, max_length=12, null=True)),
                ('cnh_tipo', models.CharField(blank=True, max_length=10, null=True)),
                ('sexo', models.CharField(max_length=1)),
                ('foto_colaborador', models.BinaryField(blank=True, null=True)),
                ('funcao', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'colaborador',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nomedepartamento', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'departamento',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Formacao',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('tipo_formacao', models.CharField(max_length=14)),
                ('nome_curso', models.CharField(max_length=50)),
                ('instituicao', models.CharField(max_length=50)),
                ('dt_inicio', models.DateField()),
                ('dt_fim', models.DateField()),
            ],
            options={
                'db_table': 'formacao',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Funcao',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nomefuncao', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'funcao',
                'managed': False,
            },
        ),
    ]
