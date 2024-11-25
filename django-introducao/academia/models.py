from django.db import models

class Formacao(models.Model):
        nome = models.CharField(max_length=100)
        descricao = models.TextField(max_length=500)

def __str__(self):
        return self.nome

class Instituicao(models.Model):
        nome = models.CharField(max_length=100)
        cidade = models.TextField(max_length=500)

def __str__(self):
        return f' {self.nome} ({self.cidade})'

class Meta:
        verbose_name_plural = 'Intituições'

class Instrutor(models.Model):
        nome = models.CharField(max_length=100)
        email = models.EmailField()
        data_nascimento = models.DateField(blank=True, null=True)

