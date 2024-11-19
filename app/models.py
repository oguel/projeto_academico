from django.db import models
import datetime

class UF(models.Model):
    class Meta:  
        verbose_name = "UF"
        verbose_name_plural = "UFs"


    sigla = models.CharField(max_length=2, unique=True)

    def __str__(self):
        return self.sigla

class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    UF = models.ForeignKey(UF, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Ocupacao(models.Model):
    class Meta:
        verbose_name = "Ocupação"
        verbose_name_plural = "Ocupações"

    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Pessoa(models.Model):
    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=11, unique=True)
    data_nasc = models.DateField()
    email = models.EmailField(unique=True, blank=True)  # Permite email em branco
    cidade = models.ForeignKey(Cidade, on_delete=models.SET_NULL, null=True, blank=True)
    ocupacao = models.ForeignKey(Ocupacao, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nome

class PessoaJuridica(Pessoa):
    cnpj = models.CharField(max_length=14, unique=True)
    razao_social = models.CharField(max_length=100)
    data_fundacao = models.DateField(verbose_name="Data de Fundação")

    class Meta:
        abstract = True

class InstituicaoEnsino(PessoaJuridica):
    class Meta:
        verbose_name = "Instituição de Ensino"
        verbose_name_plural = "Instituições de Ensino"

    site = models.URLField(blank=True)  # Permite site em branco
    telefone = models.CharField(max_length=20, blank=True)  # Permite telefone em branco

    def __str__(self):
        return self.razao_social

class AreaSaber(models.Model):
    class Meta:
        verbose_name = "Área do Saber"
        verbose_name_plural = "Áreas do Saber"

    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Curso(models.Model):
    nome = models.CharField(max_length=150)
    carga_horaria_total = models.IntegerField(default=180)  # Carga horária padrão de 180h
    duracao_meses = models.IntegerField(default=6)  # Duração padrão de 6 meses
    area_saber = models.ForeignKey(AreaSaber, on_delete=models.SET_NULL, null=True, blank=True)
    instituicao = models.ForeignKey(InstituicaoEnsino, on_delete=models.CASCADE, related_name="cursos")

    def __str__(self):
        return self.nome

class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    area_saber = models.ForeignKey(AreaSaber, on_delete=models.SET_NULL, null=True, blank=True)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name="disciplinas")

    def __str__(self):
        return self.nome

class Turno(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Turma(models.Model):
    nome = models.CharField(max_length=100)
    turno = models.ForeignKey(Turno, on_delete=models.SET_NULL, null=True, blank=True)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name="turmas")

    def __str__(self):
        return f"{self.nome} - {self.turno}"

class Matricula(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, related_name="matriculas")
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE, related_name="matriculas")
    data_inicio = models.DateField(default=datetime.date.today)  # Data de início padrão
    data_previsao_termino = models.DateField()

    def __str__(self):
        return f"{self.pessoa.nome} - {self.turma.curso.nome}"

class Avaliacao(models.Model):
    class Meta:
        verbose_name = "Avaliação"
        verbose_name_plural = "Avaliações"

    descricao = models.TextField()
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE, related_name="avaliacoes")
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    nota = models.DecimalField(max_digits=5, decimal_places=2)  # Nota padrão de 0

    def __str__(self):
        return f"{self.descricao} - {self.turma}"

class Frequencia(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    numero_faltas = models.IntegerField(default=0)  # Faltas padrão de 0

    def __str__(self):
        return f"{self.pessoa.nome} - {self.disciplina.nome} ({self.numero_faltas} faltas)"
