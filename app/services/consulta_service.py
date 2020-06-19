from ..models import ConsultaPet
from .pet_service import listar_pets

def cadastrar_consulta(consulta):
    consulta_bd = ConsultaPet.objects.create(pet=consulta.pet, motivo_consulta=consulta.motivo_consulta,
                                             peso_atual=consulta.peso_atual, medicamento_atual=consulta.medicamento_atual,
                                             medicamentos_prescritos=consulta.medicamentos_prescritos,
                                             exames_prescritos=consulta.exames_prescritos)
    consulta_bd.save()


def listar_consultas(id):
    consultas = ConsultaPet.objects.filter(pet=id).all()
    return consultas

def listar_consultas_pets(id):
    consultas = ConsultaPet.objects.filter(pet__dono=id).all()
    return consultas

def editar_consulta(consulta, consulta_novo):
    consulta.pet = consulta_novo.pet
    consulta.data = consulta_novo.data
    consulta.motivo_consulta = consulta_novo.motivo_consulta
    consulta.peso_atual = consulta_novo.peso_atual
    consulta.medicamento_atual = consulta_novo.medicamento_atual
    consulta.medicamentos_prescritos = consulta_novo.medicamentos_prescritos
    consulta.exames_prescritos = consulta_novo.exames_prescritos
    consulta.save(force_update=True)


def listar_consulta_id(id):
    consulta = ConsultaPet.objects.get(id=id)
    return consulta
