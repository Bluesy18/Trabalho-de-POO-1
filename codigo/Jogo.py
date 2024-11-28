import random

class Jogo:
    def __init__(self, time1, time2):
        self.time1 = time1
        self.time2 = time2
        for player1 in self.time1.lista_jogadores:
            player1.partidas_jogadas += 1

        for player2 in self.time2.lista_jogadores:
            player2.partidas_jogadas += 1
    
    def simulacao(self):

        gols1 = (self.time1.get_indice_ofensivo()-self.time2.get_indice_defensivo())

        if (gols1 < 0):
            gols1 = 0

        gols2 = (self.time2.get_indice_ofensivo()-self.time1.get_indice_defensivo())

        if (gols2 < 0):
            gols2 = 0

        self.gols1 = gols1
        self.gols2 = gols2

    def resultado(self):
        print(f"\nResultado do jogo:\n{self.time1.get_nome_time()}  {self.gols1} X {self.gols2}  {self.time2.get_nome_time()}\n")

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

            for f1 in assistentes1:
                if (assistentes1[assistentes1.index(f1)] == artilheiros1[assistentes1.index(f1)]):
                    assis1[assistentes1.index(f1)].assistencias_feitas -= 1
                    assistentes1.pop(assistentes1.index(f1))

            artilheiros1p = ", ".join(map(str, artilheiros1))
            assistentes1p = ", ".join(map(str, assistentes1))

            print(f"O(s) gol(s) do time {self.time1.get_nome_time()} foi(foram) de {artilheiros1p}")
            if(len(assistentes1) == 0):
                print()
            else:
                print(f"A(s) assistência(s) do time {self.time1.get_nome_time()} foi(foram) de {assistentes1p}\n")

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

            for f2 in assistentes2:
                if (assistentes2[assistentes2.index(f2)] == artilheiros2[assistentes2.index(f2)]):
                    assis2[assistentes2.index(f2)].assistencias_feitas -= 1
                    assistentes2.pop(assistentes2.index(f2))

            artilheiros2p = ", ".join(map(str, artilheiros2))
            assistentes2p = ", ".join(map(str, assistentes2))
            print(f"O(s) gol(s) do time {self.time2.get_nome_time()} foi(foram) de {artilheiros2p}")
            if(len(assistentes2) == 0):
                print()
            else:
                print(f"A(s) assistência(s) do time {self.time2.get_nome_time()} foi(foram) de {assistentes2p}\n")

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
        self.time1.set_perdedor_false()
        self.time2.set_perdedor_false()
        self.time1.set_indice_ofensivo_original()
        self.time2.set_indice_ofensivo_original()