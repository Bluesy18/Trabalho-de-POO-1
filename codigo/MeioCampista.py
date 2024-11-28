from Jogador import Jogador
from decimal import Decimal, ROUND_HALF_UP

class MeioCampista(Jogador):
  def __init__(self, nome_jogador, numero_jogador, pos_jogador, habgoleiro, defesa, fisico, passe, drible, velocidade, finalizacao):
    super().__init__(nome_jogador, numero_jogador, pos_jogador, habgoleiro, defesa, fisico, passe, drible, velocidade, finalizacao)

    self.passe_peso = passe*3
    self.drible_peso = drible*3

    overall = ((self.defesa + self.fisico + self.passe_peso + self.drible_peso + self.velocidade + self.finalizacao)/10)

    self.overall = Decimal(overall).quantize(0, ROUND_HALF_UP)