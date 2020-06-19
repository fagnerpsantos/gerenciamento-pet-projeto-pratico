from ..models import ConsultaPet

def cadastrar_consulta(consulta):
    consulta_bd = ConsultaPet.objects.create(pet=consulta.pet, motivo_consulta=consulta.motivo_consulta)
    consulta_bd.save()


def listar_consultas(id):
    consultas = ConsultaPet.objects.filter(pet=id).all()
    return consultas

def editar_consulta(consulta, consulta_novo):
    consulta.pet = consulta_novo.pet
    consulta.data = consulta_novo.data
    consulta.motivo_consulta = consulta_novo.motivo_consulta
    consulta.save(force_update=True)

def listar_consulta_id(id):
    consulta = ConsultaPet.objects.get(id=id)
    return consulta
