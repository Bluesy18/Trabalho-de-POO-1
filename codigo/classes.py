from decimal import Decimal, ROUND_HALF_UP
import random

class Time:
    def __init__(self, nome_time, lista_jogadores, lista_goleiros, lista_defensores, lista_meio_campistas, lista_atacantes):

        # Define atributo perdedor
        perdedor = False
        self.perdedor = perdedor

        # Define atributos recebidos
        self.nome_time = nome_time
        self.lista_jogadores = lista_jogadores
        self.lista_goleiros = lista_goleiros
        self.lista_defensores = lista_defensores
        self.lista_meio_campistas = lista_meio_campistas
        self.lista_atacantes = lista_atacantes

        # Define finalizações
        finalizacoes = []
        for fin in self.lista_jogadores:
            finalizacoes.append(fin.finalizacao)

        self.finalizacoes = finalizacoes

        # Define passes
        passes = []
        for pas in self.lista_jogadores:
            passes.append(pas.passe)

        self.passes = passes

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
    
    def get_finalizacoes(self):
        return self.finalizacoes
    
    def get_passes(self):
        return self.passes
    
    def get_perdedor(self):
        return self.perdedor
    
    def set_perdedor(self):
        self.perdedor = True

    def set_indice_ofensivo(self, aleatorio):
        io = float(self.indidice_ofensivo)*aleatorio
        self.indidice_ofensivo = Decimal(io).quantize(0, ROUND_HALF_UP)
    
class Jogador:
    def __init__(self, nome_jogador, numero_jogador, pos_jogador, habgoleiro, defesa, fisico, passe, drible, velocidade, finalizacao):
        partidas_jogadas = 0
        partidas_vencidas = 0
        gols_marcadados = 0
        assistencias_feitas = 0
        is_capitao = False

        self.partidas_jogadas = partidas_jogadas
        self.partidas_vencidas = partidas_vencidas
        self.gols_marcados = gols_marcadados
        self.assistencias_feitas = assistencias_feitas
        self.is_capitao = is_capitao
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

    def get_partidas_jogadas(self):
        return self.partidas_jogadas
    
    def get_partidas_vencidas(self):
        return self.partidas_vencidas

    def get_gols_marcados(self):
        return self.gols_marcados
    
    def get_assistencias_feitas(self):
        return self.assistencias_feitas
    
    def get_is_capitao(self):
        return self.is_capitao
    
    def get_overall(self):
        return self.overall
  
    def get_nome(self):
        return self.nome_jogador
    
    def get_numero(self):
        return self.numero_jogador
  
    def get_pos(self):
        return self.pos_jogador
    
    def set_is_capitao(self):
        self.is_capitao = True

    def set_num(self, num_novo):
        self.numero_jogador = num_novo
    

class Jogo:
    def __init__(self, time1, time2):
        self.time1 = time1
        self.time2 = time2
    
    def simulacao(self):
        for player1 in self.time1.lista_jogadores:
            player1.partidas_jogadas += 1

        for player2 in self.time2.lista_jogadores:
            player2.partidas_jogadas += 1

        gols1 = (self.time1.get_indice_ofensivo()-self.time2.get_indice_defensivo())

        if (gols1 < 0):
            gols1 = 0

        gols2 = (self.time2.get_indice_ofensivo()-self.time1.get_indice_defensivo())

        if (gols2 < 0):
            gols2 = 0

        self.gols1 = gols1
        self.gols2 = gols2


        print(f"Indice ofensivo time 1 {self.time1.get_indice_ofensivo()}")
        print(f"Indice defensivo time 1 {self.time1.get_indice_defensivo()}")
        print(f"Indice ofensivo time 2 {self.time2.get_indice_ofensivo()}")
        print(f"Indice defensivo time 2 {self.time2.get_indice_defensivo()}")

    def resultado(self):
        print(f"Resultado do jogo:\n{self.time1.get_nome_time()}  {self.gols1} X {self.gols2}  {self.time2.get_nome_time()}")

        self.gols1 = int(self.gols1)
        self.gols2 = int(self.gols2)

        if (self.gols1 > 0):
            artilheiros1 = []
            arti1 = random.choices(self.time1.lista_jogadores, weights = self.time1.finalizacoes, k = self.gols1)

            for art1 in arti1:
                art1.gols_marcados += 1
                artilheiros1.append(art1.get_nome())

            assistentes1 = []
            assis1 = random.choices(self.time1.lista_jogadores, weights = self.time1.passes, k = self.gols1)

            for assi1 in assis1:
                assi1.assistencias_feitas += 1
                assistentes1.append(assi1.get_nome())

            for f1 in range(self.gols1):
                if (assistentes1[f1] == artilheiros1[f1]):
                    assis1[f1].assistencias_feitas -= 1
                    assistentes1.pop(f1)

            print(f"Os gols do time {self.time1.get_nome_time()} foram de {artilheiros1}")
            print(f"As assistências do time {self.time1.get_nome_time()} foram de {assistentes1}")

        if (self.gols2 > 0):
            artilheiros2 = []
            arti2 = random.choices(self.time2.lista_jogadores, weights = self.time2.finalizacoes, k = self.gols2)

            for art2 in arti2:
                art2.gols_marcados += 1
                artilheiros2.append(art2.get_nome())

            assistentes2 = []
            assis2 = random.choices(self.time2.lista_jogadores, weights = self.time2.passes, k = self.gols2)

            for assi2 in assis2:
                assi2.assistencias_feitas += 1
                assistentes2.append(assi2.get_nome())

            for f2 in range(self.gols2):
                if (assistentes2[f2] == artilheiros2[f2]):
                    assis2[f2].assistencias_feitas -= 1
                    assistentes2.pop(f2)

            print(f"Os gols do time {self.time2.get_nome_time()} foram de {artilheiros2}")
            print(f"As assistências do time {self.time2.get_nome_time()} foram de {assistentes2}")

    def perdedor(self):
        if(self.gols1 > self.gols2):
            self.time2.set_perdedor()
        elif(self.gols1 < self.gols2):
            self.time1.set_perdedor()
        else:
            self.time1.set_perdedor()
            self.time2.set_perdedor()
        self.gols1 = 0
        self.gols2 = 0

    def zebra(self):
        if(self.time1.get_perdedor() == True):
            aleatorio = random.uniform(1, 1.5)
            self.time1.set_indice_ofensivo(aleatorio)
        if(self.time2.get_perdedor() == True):
            aleatorio = random.uniform(1, 1.5)
            self.time2.set_indice_ofensivo(aleatorio)

    def ganhador(self):
        if(self.gols1 > self.gols2):
            for player1 in self.time1.lista_jogadores:
                player1.partidas_vencidas += 1
        elif(self.gols1 < self.gols2):
            for player2 in self.time2.lista_jogadores:
                player2.partidas_vencidas += 1
        self.time1.set_perdedor()
        self.time1.set_perdedor()
