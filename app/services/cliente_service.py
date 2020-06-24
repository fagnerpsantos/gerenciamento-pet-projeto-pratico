from ..models import Cliente
from django.db import connection

def listar_clientes():
    clientes = Cliente.objects.all()
    return clientes

def listar_cliente_id(id):
    cliente = Cliente.objects.get(id=id)
    return cliente

def remover_cliente(cliente):
    cliente.delete()

def cadastrar_cliente(cliente):
    Cliente.objects.create(nome=cliente.nome, email=cliente.email, endereco=cliente.endereco, cpf=cliente.cpf,
                           data_nascimento=cliente.data_nascimento, profissao=cliente.profissao)

def editar_cliente(cliente, cliente_novo):
    cliente.nome = cliente_novo.nome
    cliente.email = cliente_novo.email
    cliente.endereco = cliente_novo.endereco
    cliente.cpf = cliente_novo.cpf
    cliente.data_nascimento = cliente_novo.data_nascimento
    cliente.profissao = cliente_novo.profissao
    cliente.save(force_update=True)