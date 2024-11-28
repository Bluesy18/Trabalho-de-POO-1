from Jogador import Jogador
from decimal import Decimal, ROUND_HALF_UP

class Goleiro(Jogador):
  def __init__(self, nome_jogador, numero_jogador, pos_jogador, habgoleiro, defesa, fisico, passe, drible, velocidade, finalizacao):
    super().__init__(nome_jogador, numero_jogador, pos_jogador, habgoleiro, defesa, fisico, passe, drible, velocidade, finalizacao)

    overall = habgoleiro

    self.overall = Decimal(overall).quantize(0, ROUND_HALF_UP)