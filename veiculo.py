class Veiculo(object):

    def modelo(self, modelo):
        self._modelo = modelo

    def combustivel(self, combustivel):
        self._combustivel = combustivel

    def ano_fabricacao(self, ano):
        self._ano_fabricacao = ano

    def marca(self, marca):
        self._marca = marca

    def __str__(self):
        return f'{self._modelo} | {self._combustivel} | {self._ano_fabricacao} | {self._marca}'

    def dados_fabrica(self):
        print(f'{self.__module__.title()} : {self}')
