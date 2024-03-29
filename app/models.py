from django.contrib.auth.models import User, AbstractUser
from django.db import models
from django_localflavor_br.br_states import STATE_CHOICES


# Create your models_app here.

class EnderecoCliente(models.Model):
    rua = models.CharField(max_length=50, null=False, blank=False)
    cidade = models.CharField(max_length=30, null=False, blank=False)
    estado = models.CharField(max_length=2, choices=STATE_CHOICES, null=False, blank=False)

    def __str__(self):
        return self.rua

class Cliente(models.Model):
    nome = models.CharField(max_length=150, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    endereco = models.ForeignKey(EnderecoCliente, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=14, null=False, blank=False)
    data_nascimento = models.DateField(null=False, blank=False)
    profissao = models.CharField(max_length=25, null=False, blank=False)

    def __str__(self):
        return self.nome


class Pet(models.Model):
    CATEGORIA_PET_CHOICES = (
        ('Ca', 'Cachorro'),
        ('Ga', 'Gato'),
        ('Co', 'Coelho'),
    )

    COR_PET_CHOICES = (
        ('Pr', 'Preto'),
        ('Br', 'Branco'),
        ('Ci', 'Cinza'),
        ('Ma', 'Marrom'),
    )
    nome = models.CharField(max_length=50, null=False, blank=False)
    nascimento = models.DateField(null=False, blank=False)
    categoria = models.CharField(max_length=2, choices=CATEGORIA_PET_CHOICES, null=False, blank=False)
    cor = models.CharField(max_length=2, choices=COR_PET_CHOICES, null=False, blank=False)
    dono = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.nome

class ConsultaPet(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, null=False, blank=False)
    data = models.DateField(null=False, blank=False, auto_now_add=True)
    motivo_consulta = models.CharField(max_length=200, null=False, blank=False)
    peso_atual = models.FloatField(null=True, blank=True)
    medicamento_atual = models.TextField(null=True, blank=True)
    medicamentos_prescritos = models.TextField(null=True, blank=True)
    exames_prescritos = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.pet


class Funcionario(AbstractUser):
    CARGO_CHOICES = [
        (1, 'Veterinario'),
        (2, 'Financeiro'),
        (3, 'Atendimento'),
    ]
    nome = models.CharField(max_length=50, null=False, blank=False)
    nascimento = models.DateField(null=False, blank=False)
    cargo = models.IntegerField(choices=CARGO_CHOICES, null=False, blank=False)
