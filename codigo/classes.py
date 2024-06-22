class Time:
    def __init__(self, nome_time, lista_jogadores):
        self.nome_time = nome_time
        self.lista_jogadores = lista_jogadores

        overall_time = 0
        for i in range(11):
            overall_time += self.lista_jogadores[i].overall

        self.overall_time = overall_time

    def get_overall_time(self):
        return self.overall_time
        
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

    
