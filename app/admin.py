from django.contrib import admin
from .models import *



#  Ocupação e pessoas

class PessoaInline(admin.TabularInline):
    model = Pessoa
    extra = 1


@admin.register(Ocupacao)
class OcupacaoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    inlines = [PessoaInline]


#  Instituição e cursos
class CursoInline(admin.TabularInline):
    model = Curso
    extra = 1


@admin.register(InstituicaoEnsino)
class InstituicaoEnsinoAdmin(admin.ModelAdmin):
    list_display = ('razao_social', 'telefone', 'site', 'cidade')
    search_fields = ('razao_social',)
    inlines = [CursoInline]


#  Área do saber e cursos
class CursoAreaInline(admin.TabularInline):
    model = Curso
    extra = 1


@admin.register(AreaSaber)
class AreaSaberAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    inlines = [CursoAreaInline]


#  Cursos e disciplinas
class DisciplinaInline(admin.TabularInline):
    model = Disciplina
    extra = 1


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'instituicao', 'duracao_meses', 'carga_horaria_total')
    search_fields = ('nome', 'instituicao__razao_social')
    inlines = [DisciplinaInline]


# v) Disciplinas e avaliações
class AvaliacaoInline(admin.TabularInline):
    model = Avaliacao
    extra = 1


@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'area_saber', 'curso')
    search_fields = ('nome', 'curso__nome', 'area_saber__nome')
    inlines = [AvaliacaoInline]


# vi) Turmas e alunos
class MatriculaInline(admin.TabularInline):
    model = Matricula
    extra = 1


@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'turno', 'curso')
    search_fields = ('nome', 'curso__nome')
    inlines = [MatriculaInline]


#  UF e cidades
class CidadeInline(admin.TabularInline):
    model = Cidade
    extra = 1


@admin.register(UF)
class UFAdmin(admin.ModelAdmin):
    list_display = ('sigla',)
    search_fields = ('sigla',)
    inlines = [CidadeInline]


#  Estudantes, disciplinas, avaliações, frequência
class FrequenciaInline(admin.TabularInline):
    model = Frequencia
    extra = 1


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'email', 'cidade', 'ocupacao')
    search_fields = ('nome', 'cpf', 'email')
    inlines = [FrequenciaInline]


# Registro de outros modelos sem inlines adicionais
admin.site.register(Avaliacao)
admin.site.register(Frequencia)
