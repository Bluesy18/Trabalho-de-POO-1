from classes import Jogador
from decimal import Decimal, ROUND_HALF_UP

class Goleiro(Jogador):
  def __init__(self, nome_jogador, numero_jogador, pos_jogador, habgoleiro, defesa, fisico, passe, drible, velocidade, finalizacao):
    super().__init__(nome_jogador, numero_jogador, pos_jogador, habgoleiro, defesa, fisico, passe, drible, velocidade, finalizacao)

    overall = habgoleiro

    self.overall = Decimal(overall).quantize(0, ROUND_HALF_UP)

  def get_overall(self):
    return self.overall
  
  def get_nome(self):
    return self.nome_jogador
    
  def get_numero(self):
    return self.numero_jogador
  
  def get_pos(self):
    return self.pos_jogador

class Defensor(Jogador):
  def __init__(self, nome_jogador, numero_jogador, pos_jogador, habgoleiro, defesa, fisico, passe, drible, velocidade, finalizacao):
    super().__init__(nome_jogador, numero_jogador, pos_jogador, habgoleiro, defesa, fisico, passe, drible, velocidade, finalizacao)

    self.defesa_peso = defesa*4
    self.fisico_peso = fisico*3

    overall = ((self.defesa_peso + self.fisico_peso + self.passe + self.drible + self.velocidade)/10)

    self.overall = Decimal(overall).quantize(0, ROUND_HALF_UP)
  
  def get_overall(self):
    return self.overall
  
  def get_nome(self):
    return self.nome_jogador
    
  def get_numero(self):
    return self.numero_jogador
  
  def get_pos(self):
    return self.pos_jogador

class MeioCampista(Jogador):
  def __init__(self, nome_jogador, numero_jogador, pos_jogador, habgoleiro, defesa, fisico, passe, drible, velocidade, finalizacao):
    super().__init__(nome_jogador, numero_jogador, pos_jogador, habgoleiro, defesa, fisico, passe, drible, velocidade, finalizacao)

    self.passe_peso = passe*3
    self.drible_peso = drible*3

    overall = ((self.defesa + self.fisico + self.passe_peso + self.drible_peso + self.velocidade + self.finalizacao)/10)

    self.overall = Decimal(overall).quantize(0, ROUND_HALF_UP)
  
  def get_overall(self):
    return self.overall
  
  def get_nome(self):
    return self.nome_jogador
    
  def get_numero(self):
    return self.numero_jogador
  
  def get_pos(self):
    return self.pos_jogador
  
class Atacante(Jogador):
  def __init__(self, nome_jogador, numero_jogador, pos_jogador, habgoleiro, defesa, fisico, passe, drible, velocidade, finalizacao):
    super().__init__(nome_jogador, numero_jogador, pos_jogador, habgoleiro, defesa, fisico, passe, drible, velocidade, finalizacao)

    self.finalizacao_peso = finalizacao*4
    self.velocidade_peso = velocidade*2
    self.drible_peso = drible*2

    overall = ((self.fisico + self.passe + self.drible_peso + self.velocidade_peso + self.finalizacao_peso)/10)

    self.overall = Decimal(overall).quantize(0, ROUND_HALF_UP)

  def get_overall(self):
    return self.overall
  
  def get_nome(self):
    return self.nome_jogador
    
  def get_numero(self):
    return self.numero_jogador
  
  def get_pos(self):
    return self.pos_jogador
  



    

