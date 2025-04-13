from enum import Enum
from django.db import models
from django.contrib.auth.models import User  # Importa o modelo de usuário padrão do Django

# Modelo para armazenar os instrumentos disponíveis
class Instrumento(models.Model):
    nome = models.CharField(max_length=50, unique=True)  # Nome do instrumento

    def __str__(self):
        return self.nome  # Retorna o nome do instrumento como representação textual

# Enumeração para os instrumentos disponíveis
class InstrumentoEnum(Enum):
    BATERIA = "Bateria"
    BAIXO = "Baixo"
    CANTO = "Canto"
    GUITARRA = "Guitarra"
    PIANO = "Piano"
    SAXOFONE = "Saxofone"
    VIOLAO = "Violão"
    VIOLINO = "Violino"

    @classmethod
    def choices(cls):
        return [(item.value, item.value) for item in cls]  # Retorna uma lista de tuplas para o campo de escolhas

# Modelo para armazenar informações dos professores
class Professor(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)  # Relaciona com um usuario do Django
    nome = models.CharField(max_length=150)  # Nome do professor
    nascimento = models.DateField()  # Data de nascimento do professor
    cpf = models.CharField(max_length=14, unique=True)  # CPF do professor que vamos usar como chave unica pro usuario
    rg = models.CharField(max_length=20)  # RG do professor
    
    # Armazena os instrumentos como uma string separada por virgulas
    instrumentos = models.CharField(max_length=255, choices=InstrumentoEnum.choices())

    def get_instrumentos_lista(self):
        return self.instrumentos.split(", ") if self.instrumentos else []  # Retorna os instrumentos como lista

    def __str__(self):
        return self.nome  # Retorna o nome do professor como representação textual

# Modelo para armazenar informações dos alunos
class Aluno(models.Model):
    matricula = models.AutoField(primary_key=True)  # Número de matricula gerado automaticamente (talvez autoincrement seja melhor)
    nome = models.OneToOneField(User, on_delete=models.CASCADE)  # Relaciona com um usuario do Django pra acessar o banco
    instrumento_interesse = models.ForeignKey(Instrumento, on_delete=models.SET_NULL, null=True, blank=True)  # Instrumento de interesse do aluno
    telefone = models.CharField(max_length=20, blank=True, null=True)  # Telefone do aluno
    curso = models.CharField(max_length=100, blank=True, null=True)  # Adicionando o campo curso 
    email = models.CharField(max_length=100, blank=True, null=True)  # Adiciona o campo email
    # falta email e outras informações pertinentes tipo CPF etc...

    def __str__(self):
        return self.nome