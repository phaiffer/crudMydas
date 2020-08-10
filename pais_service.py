from ..models import Pais


def listar_pais():
    pais = Pais.objects.all()
    return pais


def listar_pais_id(id):
    pais = Pais.objects.get(id=id)
    return pais


def remover_pais(pais):
    pais.delete()


def cadastrar_pais(pais):
    Pais.objects.create(nome=pais.nome, sigla=pais.sigla)


def editar_pais(pais, pais_novo):
    pais.nome = pais_novo.nome
    pais.sigla = pais_novo.sigla
    pais.save(force_update=True)