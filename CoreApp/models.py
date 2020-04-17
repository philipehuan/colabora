# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Colaborador(models.Model):
    nome = models.CharField(max_length=60)
    nascimento = models.DateField()
    rg = models.CharField(max_length=15)
    cpf = models.CharField(max_length=15)
    telefone = models.CharField(max_length=12, blank=True, null=True)
    cnh = models.CharField(max_length=12, blank=True, null=True)
    cnh_tipo = models.CharField(max_length=10, blank=True, null=True)
    sexo = models.CharField(max_length=1)
    departamento = models.ForeignKey('Departamento', models.DO_NOTHING, db_column='departamento')
    funcao = models.CharField(max_length=20)
    foto_colaborador = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'colaborador'

    def __str__(self):
        return self.nome


class Departamento(models.Model):
    nomedepartamento = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'departamento'

    def return_Nome(self):
        return self.nomedepartamento

    def __str__(self):
        return self.nomedepartamento


class Formacao(models.Model):
    colaborador = models.ForeignKey(Colaborador, models.DO_NOTHING, db_column='colaborador')
    tipo_formacao = models.CharField(max_length=14)
    nome_curso = models.CharField(max_length=50)
    instituicao = models.CharField(max_length=50)
    dt_inicio = models.DateField()
    dt_fim = models.DateField()

    class Meta:
        managed = False
        db_table = 'formacao'
        unique_together = (('id', 'colaborador'),)


class Funcao(models.Model):
    nomefuncao = models.CharField(max_length=20)
    departamento = models.ForeignKey(Departamento, models.DO_NOTHING, db_column='departamento', related_name='deps')

    class Meta:
        managed = False
        db_table = 'funcao'
        unique_together = (('id', 'departamento'),)

    def __str__(self):
        return self.nomefuncao
