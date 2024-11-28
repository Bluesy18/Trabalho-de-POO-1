from Jogador import Jogador
from decimal import Decimal, ROUND_HALF_UP

class Defensor(Jogador):
  def __init__(self, nome_jogador, numero_jogador, pos_jogador, habgoleiro, defesa, fisico, passe, drible, velocidade, finalizacao):
    super().__init__(nome_jogador, numero_jogador, pos_jogador, habgoleiro, defesa, fisico, passe, drible, velocidade, finalizacao)

    self.defesa_peso = defesa*4
    self.fisico_peso = fisico*3

    overall = ((self.defesa_peso + self.fisico_peso + self.passe + self.drible + self.velocidade)/10)

    self.overall = Decimal(overall).quantize(0, ROUND_HALF_UP)