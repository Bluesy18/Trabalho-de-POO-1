class Time:
    def __init__(self, nome_time, lista_jogadores):
        self.nome_time = nome_time
        self.lista_jogadores = lista_jogadores
        
    def get_nome_time(self):
        return self.nome_time
    
    def get_jogadores(self):
        return self.lista_jogadores
    
class Jogador:
    def __init__(self, nome_jogador, numero_jogador, pos_jogador, habgoleiro, defesa, fisico, passe, drible, velocidade, finalizacao):
        self.pos_jogador = pos_jogador
        self.nome_jogador = nome_jogador
        self.numero_jogador = numero_jogador
        self.habgoleiro = habgoleiro
        self.defesa = defesa
        self.fisico = fisico
        self.passe = passe
        self.drible = drible
        self.velocidade = velocidade
        self.finalizacao = finalizacao

    
