class estado():
    def __init__(self, nome_estado, sigla_estado):
        self.__nome_estado = nome
        self.__sigla_estado = sigla

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def sigla(self):
        return self.__sigla

    @sigla.setter
    def sigla(self, sigla):
        self.__sigla = sigla