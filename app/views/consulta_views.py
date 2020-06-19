from django.shortcuts import render, redirect
from ..forms import consulta_forms
from ..entidades import consulta
from ..services import consulta_service, pet_service

def inserir_consulta(request, id):
    if request.method == "POST":
        form_consulta = consulta_forms.ConsultaPetForm(request.POST)
        pet = pet_service.listar_pet_id(id)
        if form_consulta.is_valid():
            motivo_consulta = form_consulta.cleaned_data["motivo_consulta"]
            consulta_nova = consulta.ConsultaPet(pet=pet, motivo_consulta=motivo_consulta)
            consulta_service.cadastrar_consulta(consulta_nova)
            return redirect('listar_pet_id', pet.id)
    else:
        form_consulta = consulta_forms.ConsultaPetForm()
    return render(request, 'consultas/form_consulta.html', {'form_consulta': form_consulta})

def listar_consultas(request):
    consultas = consulta_service.listar_consultas()
    return render(request, 'consultas/lista_consultas.html', {'consultas': consultas})

def listar_consulta_id(request, id):
    consulta = consulta_service.listar_consulta_id(id)
    return render(request, 'consultas/lista_consulta.html', {'consulta': consulta})

def editar_consulta(request, id):
    consulta_antigo = consulta_service.listar_consulta_id(id)
    form_consulta = consulta_forms.PetForm(request.POST or None, instance=consulta_antigo)
    if form_consulta.is_valid():
        dono = form_consulta.cleaned_data["dono"]
        nome = form_consulta.cleaned_data["nome"]
        cor = form_consulta.cleaned_data["cor"]
        nascimento = form_consulta.cleaned_data["nascimento"]
        categoria = form_consulta.cleaned_data["categoria"]
        consulta_novo = consulta.Pet(dono=dono, nome=nome, cor=cor, nascimento=nascimento,
                                    categoria=categoria)
        consulta_service.editar_consulta(consulta_antigo, consulta_novo)
        return redirect('listar_consultas')
    return render(request, 'consultas/form_consulta.html', {'form_consulta': form_consulta})