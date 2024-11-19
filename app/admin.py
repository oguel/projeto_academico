from django.contrib import admin
from .models import *


class CursoInline(admin.TabularInline):
    model = Curso
    extra = 1


class DisciplinaInline(admin.TabularInline):
    model = Disciplina
    extra = 1


class MatriculaInline(admin.TabularInline):
    model = Matricula
    extra = 1


@admin.register(InstituicaoEnsino)
class InstituicaoEnsinoAdmin(admin.ModelAdmin):
    list_display = ('razao_social', 'site', 'telefone', 'cidade')
    inlines = [CursoInline]


@admin.register(AreaSaber)
class AreaSaberAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    inlines = [DisciplinaInline]


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'email', 'cidade', 'ocupacao')
    inlines = [MatriculaInline]


admin.site.register(Cidade)
admin.site.register(Ocupacao)
admin.site.register(Turno)
admin.site.register(Turma)
admin.site.register(Curso)
admin.site.register(Avaliacao)
admin.site.register(Frequencia)
