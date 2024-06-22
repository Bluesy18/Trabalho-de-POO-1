from decimal import Decimal, ROUND_HALF_UP

class Time:
    def __init__(self, nome_time, lista_jogadores, lista_goleiros, lista_defensores, lista_meio_campistas, lista_atacantes):

        # Define atributos recebidos
        self.nome_time = nome_time
        self.lista_jogadores = lista_jogadores
        self.lista_goleiros = lista_goleiros
        self.lista_defensores = lista_defensores
        self.lista_meio_campistas = lista_meio_campistas
        self.lista_atacantes = lista_atacantes

        # Calcula índice defensivo
        indice_defensivo = lista_goleiros[0].get_overall()

        for defe in self.lista_defensores:
            indice_defensivo += defe.get_overall()

        meias = 0
        for meia in self.lista_meio_campistas:
            meias += meia.get_overall()

        meias = meias/len(self.lista_meio_campistas)

        indice_defensivo = (indice_defensivo/(len(self.lista_defensores)+1))*2
        indice_defensivo = (indice_defensivo+meias)/3

        self.indice_defensivo = Decimal(indice_defensivo).quantize(0, ROUND_HALF_UP)

        # Calcula índice ofensivo
        indice_ofensivo = 0

        for ata in self.lista_atacantes:
            indice_ofensivo += ata.get_overall()
        
        indice_ofensivo = (indice_ofensivo/len(self.lista_atacantes))*2
        indice_ofensivo = (indice_ofensivo+meias)/3

        self.indidice_ofensivo = Decimal(indice_ofensivo).quantize(0, ROUND_HALF_UP)

        # Calcula overall
        overall_time = 0
        for i in range(11):
            overall_time += self.lista_jogadores[i].overall

        self.overall_time = overall_time

    # Métodos
    def get_overall_time(self):
        return self.overall_time
        
    def get_nome_time(self):
        return self.nome_time
    
    def get_jogadores(self):
        return self.lista_jogadores
    
    def get_indice_defensivo(self):
        return self.indice_defensivo
    
    def get_indice_ofensivo(self):
        return self.indidice_ofensivo 

    
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

class Jogo:
    def __init__(self, gols_time1, gols_time2):
        self.gols_time1 = gols_time1
        self.gols_time2 = gols_time2

    def get_gols_time1(self):
        return self.gols_time1
    
    def get_gols_time2(self):
        return self.gols_time2
