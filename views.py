from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Pais, Estado
from .forms import PaisForm, EstadoForm
from .entidades import pais, estado
from .service import pais_service, estado_service


# Create your views here.
def listar_pais(request):
    pais = pais_service.listar_pais()
    return render(request, 'pais/listar_pais.html', {'pais': pais})

def inserir_pais(request):
    # aqui fazemos a validação das informações e inserimos no DB
    if request.method == "POST":
        form = PaisForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            sigla = form.cleaned_data['sigla']
            pais_novo = pais.pais(nome=nome, sigla=sigla)
            pais_service.cadastrar_pais(pais_novo)
            return redirect('listar_pais')
    else:
        form = PaisForm()
    return render(request, 'pais/form_pais.html', {'form': form})


def listar_pais_id(request, id):
    pais = pais_service.listar_pais_id(id)
    return render(request, 'pais/lista_pais.html', {'pais': pais})


def editar_pais(request, id):
    pais_antigo = pais_service.listar_pais_id(id)
    form = PaisForm(request.POST or None, instance=pais)
    if form.is_valid():
        nome = form.cleaned_data['nome']
        sigla = form.cleaned_data['sigla']
        pais_novo = pais.pais(nome=nome, sigla=sigla)
        pais_service.editar_pais(pais_antigo, pais_novo)
        return redirect('listar_pais')
    return render(request, 'pais/form_pais.html',{'form': form})


def remover_pais(request, id):
    pais = pais_service.listar_pais_id(id)
    if request.method == "POST":
        pais_service.remover_pais(pais)
        return redirect('listar_pais')
    else:
        return render(request, 'pais/confirma_exclusao.html', {'pais': pais})


# =============================================Estados===================================================
def listar_estado(request):
    estado = estado_service.listar_estado()
    return render(request, 'pais/listar_estado.html', {'estado': estado})

def inserir_estado(request):
    # aqui fazemos a validação das informações e inserimos no DB
    if request.method == "POST":
        form = EstadoForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            sigla = form.cleaned_data['sigla']
            estado_novo = estado.Estado(nome=nome_estado, sigla=sigla_estado)
            estado_service.cadastrar_estado(estado_novo)
            return redirect('listar_estado')
    else:
        form = EstadoForm()
    return render(request, 'pais/cad_estado.html', {'form': form})


def listar_estado_id(request, id_estado):
    estado = estado_service.listar_estado_id(id_estado)
    return render(request, 'pais/lista_estado.html', {'estado': estado})


def editar_estado(request, id_estado):
    estado = estado_service.listar_estado_id(id_estado)
    form = EstadoForm(request.POST or None, instance=estado)
    if form.is_valid():
        nome_estado = form.cleaned_data['nome']
        sigla_estado = form.cleaned_data['sigla']
        estado_novo = estado.Estado(nome=nome_estado, sigla=sigla_estado)
        estado_service.editar_estado(estado, estado_novo)
        return redirect('listar_estado')
    return render(request, 'pais/cad_estado.html',{'form': form})


def remover_estado(request, id):
    estado = estado_service.listar_estado_id(id)
    if request.method == "POST":
        estado_service.remover_estado(estado)
        return redirect('listar_estado')
    else:
        return render(request, 'pais/confirma_exclusao.html', {'estado': estado})
