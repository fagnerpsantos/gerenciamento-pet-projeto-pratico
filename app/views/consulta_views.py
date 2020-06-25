from django.contrib.auth.decorators import user_passes_test
from django.core.mail import send_mail, EmailMessage
from django.shortcuts import render, redirect
from django.template.loader import render_to_string

from gerenciamento_pet import settings

from ..forms import consulta_forms
from ..entidades import consulta
from ..services import consulta_service, pet_service


@user_passes_test(lambda u: u.cargo == 1)
def inserir_consulta(request, id):
    if request.method == "POST":
        form_consulta = consulta_forms.ConsultaPetForm(request.POST)
        pet = pet_service.listar_pet_id(id)
        if form_consulta.is_valid():
            motivo_consulta = form_consulta.cleaned_data["motivo_consulta"]
            peso_atual = form_consulta.cleaned_data["peso_atual"]
            medicamento_atual = form_consulta.cleaned_data["medicamento_atual"]
            medicamentos_prescritos = form_consulta.cleaned_data["medicamentos_prescritos"]
            exames_prescritos = form_consulta.cleaned_data["exames_prescritos"]
            consulta_nova = consulta.ConsultaPet(pet=pet, motivo_consulta=motivo_consulta, peso_atual=peso_atual,
                                                 medicamento_atual=medicamento_atual,
                                                 medicamentos_prescritos=medicamentos_prescritos,
                                                 exames_prescritos=exames_prescritos)
            consulta_service.cadastrar_consulta(consulta_nova)
            return redirect('listar_pet_id', pet.id)
    else:
        form_consulta = consulta_forms.ConsultaPetForm()
    return render(request, 'consultas/form_consulta.html', {'form_consulta': form_consulta})


@user_passes_test(lambda u: u.cargo == 1)
def listar_consulta_id(request, id):
    consulta = consulta_service.listar_consulta_id(id)
    return render(request, 'consultas/lista_consulta.html', {'consulta': consulta})


@user_passes_test(lambda u: u.cargo == 1)
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
        return redirect('listar_consulta_id', consulta_antigo.id)
    return render(request, 'consultas/form_consulta.html', {'form_consulta': form_consulta})


def enviar_email_consulta(request, id):
    consulta = consulta_service.listar_consulta_id(id)
    pet_consulta = pet_service.listar_pet_id(consulta.pet.id)
    assunto = 'Resumo da sua consulta no PET'
    html_message = render_to_string('consultas/consulta_email.html', {'consulta': consulta})
    corpo_email = ' it  means a world to us '
    email_remetente = settings.EMAIL_HOST_USER
    email_destino = [pet_consulta.dono.email, ]
    # email = EmailMessage(assunto, corpo_email, email_remetente, email_destino, attachments=html_message)
    send_mail(assunto, corpo_email, email_remetente, email_destino, html_message=html_message)

    # email.send()
    return redirect('listar_consulta_id', id)
