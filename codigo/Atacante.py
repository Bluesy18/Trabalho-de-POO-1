from Jogador import Jogador
from decimal import Decimal, ROUND_HALF_UP

class Atacante(Jogador):
  def __init__(self, nome_jogador, numero_jogador, pos_jogador, habgoleiro, defesa, fisico, passe, drible, velocidade, finalizacao):
    super().__init__(nome_jogador, numero_jogador, pos_jogador, habgoleiro, defesa, fisico, passe, drible, velocidade, finalizacao)

    self.finalizacao_peso = finalizacao*4
    self.velocidade_peso = velocidade*2
    self.drible_peso = drible*2

    overall = ((self.fisico + self.passe + self.drible_peso + self.velocidade_peso + self.finalizacao_peso)/10)

    self.overall = Decimal(overall).quantize(0, ROUND_HALF_UP)