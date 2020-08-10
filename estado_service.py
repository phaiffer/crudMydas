from ..models import Estado


def listar_estado():
    estado = Estado.objects.all()
    return estado


def listar_estado_id(id_estado):
    estado = Estado.objects.get(id_estado=id_estado)
    return estado


def remover_estado(estado):
    estado.delete()


def cadastrar_estado(estado):
    Estado.objects.create(nome=estado.nome_estado, sigla=estado.sigla_estado)


def editar_estado(estado, estado_novo):
    estado.nome_estado = estado_novo.nome_estado
    estado.sigla_estado = estado_novo.sigla_estado
    estado.save(force_update=True)
