from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Pessoa, Curso, Turma, InstituicaoEnsino


# Listar todas as pessoas
class PessoaListView(ListView):
    model = Pessoa
    template_name = "core/pessoa_list.html"
    context_object_name = "pessoas"


# Criar uma nova pessoa
class PessoaCreateView(CreateView):
    model = Pessoa
    fields = ['nome', 'cpf', 'data_nasc', 'email', 'cidade', 'ocupacao']
    template_name = "core/pessoa_form.html"
    success_url = reverse_lazy("pessoa_list")


# Atualizar informações de uma pessoa
class PessoaUpdateView(UpdateView):
    model = Pessoa
    fields = ['nome', 'cpf', 'data_nasc', 'email', 'cidade', 'ocupacao']
    template_name = "core/pessoa_form.html"
    success_url = reverse_lazy("pessoa_list")


# Excluir uma pessoa
class PessoaDeleteView(DeleteView):
    model = Pessoa
    template_name = "core/pessoa_confirm_delete.html"
    success_url = reverse_lazy("pessoa_list")


# Listar cursos
class CursoListView(ListView):
    model = Curso
    template_name = "core/curso_list.html"
    context_object_name = "cursos"


# Criar um novo curso
class CursoCreateView(CreateView):
    model = Curso
    fields = ['nome', 'carga_horaria_total', 'duracao_meses', 'area_saber', 'instituicao']
    template_name = "core/curso_form.html"
    success_url = reverse_lazy("curso_list")


# Listar turmas
class TurmaListView(ListView):
    model = Turma
    template_name = "core/turma_list.html"
    context_object_name = "turmas"
