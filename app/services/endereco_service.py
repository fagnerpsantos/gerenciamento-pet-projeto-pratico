from ..models import EnderecoCliente

def cadastrar_endereco(endereco):
    return EnderecoCliente.objects.create(rua=endereco.rua, cidade=endereco.cidade, estado=endereco.estado)

def listar_endereco_id(id):
    endereco = EnderecoCliente.objects.get(id=id)
    return endereco

def editar_endereco(endereco_antigo, endereco_novo):
    endereco_antigo.rua = endereco_novo.rua
    endereco_antigo.cidade = endereco_novo.cidade
    endereco_antigo.estado = endereco_novo.estado
    endereco_antigo.save(force_update=True)

def remover_endereco(endereco):
    endereco.delete()