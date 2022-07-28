class Radio():

    def __init__(self):
        self._lista_musica = []

    def tocar_musica(self):
        print("iniciando radio...")

        if len(self._lista_musica) == 0:
            print("sem musicas...")

        print("Total de musicas: {}".format(len(self._lista_musica)))
        for musica in self._lista_musica:
            print(f'tocando - {musica}')

    def adicionar_musica(self, musica):
        self._lista_musica.append(musica)
