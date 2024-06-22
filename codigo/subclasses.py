from classes import Jogador
from decimal import Decimal, ROUND_HALF_UP

class Goleiro(Jogador):
  def __init__(self, nome_jogador, numero_jogador, habgoleiro, defesa, fisico, passe, drible, velocidade, finalizacao):
    super().__init__(nome_jogador, numero_jogador, habgoleiro, defesa, fisico, passe, drible, velocidade, finalizacao)

    self.habgoleiro = habgoleiro*10

    overall = habgoleiro

    self.overall = Decimal(overall).quantize(0, ROUND_HALF_UP)

  def get_overall(self):
    return self.overall
  
  def get_nome(self):
    return self.nome_jogador
    
  def get_numero(self):
    return self.numero_jogador

class Defensor(Jogador):
  def __init__(self, nome_jogador, numero_jogador, habgoleiro, defesa, fisico, passe, drible, velocidade, finalizacao):
    super().__init__(nome_jogador, numero_jogador, habgoleiro, defesa, fisico, passe, drible, velocidade, finalizacao)

    self.defesa = defesa*4
    self.fisico = fisico*3

    overall = ((self.defesa + self.fisico + self.passe + self.drible + self.velocidade)/10)

    self.overall = Decimal(overall).quantize(0, ROUND_HALF_UP)
  
  def get_overall(self):
    return self.overall
  
  def get_nome(self):
    return self.nome_jogador
    
  def get_numero(self):
    return self.numero_jogador

class MeioCampista(Jogador):
  def __init__(self, nome_jogador, numero_jogador, habgoleiro, defesa, fisico, passe, drible, velocidade, finalizacao):
    super().__init__(nome_jogador, numero_jogador, habgoleiro, defesa, fisico, passe, drible, velocidade, finalizacao)

    self.passe = passe*3
    self.drible = drible*3

    overall = ((self.defesa + self.fisico + self.passe + self.drible + self.velocidade + self.finalizacao)/10)

    self.overall = Decimal(overall).quantize(0, ROUND_HALF_UP)
  
  def get_overall(self):
    return self.overall
  
  def get_nome(self):
    return self.nome_jogador
    
  def get_numero(self):
    return self.numero_jogador

class Atacante(Jogador):
  def __init__(self, nome_jogador, numero_jogador, habgoleiro, defesa, fisico, passe, drible, velocidade, finalizacao):
    super().__init__(nome_jogador, numero_jogador, habgoleiro, defesa, fisico, passe, drible, velocidade, finalizacao)

    self.finalizacao = finalizacao*4
    self.velocidade = velocidade*2
    self.drible = drible*2

    overall = ((self.fisico + self.passe + self.drible + self.velocidade + self.finalizacao)/10)

    self.overall = Decimal(overall).quantize(0, ROUND_HALF_UP)

  def get_overall(self):
    return self.overall
  
  def get_nome(self):
    return self.nome_jogador
    
  def get_numero(self):
    return self.numero_jogador



    

