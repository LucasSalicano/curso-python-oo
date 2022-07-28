from carro import Carro
from moto import Moto

carro1 = Carro()
carro1.modelo("modelo 1")
carro1.combustivel("flex")
carro1.marca("marca 1")
carro1.ano_fabricacao(2022)
carro1.dados_fabrica()

carro1.adicionar_musica("musica 1")
carro1.adicionar_musica("musica 2")
carro1.adicionar_musica("musica 3")
carro1.adicionar_musica("musica 4")
carro1.tocar_musica()

moto1 = Moto()
moto1.modelo("modelo moto 1")
moto1.combustivel("Gasolina")
moto1.marca("marca moto 1")
moto1.ano_fabricacao(2021)
moto1.dados_fabrica()