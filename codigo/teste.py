import random
from classes import Jogo
from time1 import time1
from time2 import time2

def simulacao(time1, time2):
    for player1 in time1.lista_jogadores:
        player1.partidas_jogadas += 1

    for player2 in time2.lista_jogadores:
        player2.partidas_jogadas += 1

    gols1 = (time1.get_indice_ofensivo()-time2.get_indice_defensivo())

    if (gols1 < 0):
        gols1 = 0

    gols2 = (time2.get_indice_ofensivo()-time1.get_indice_defensivo())

    if (gols2 < 0):
        gols2 = 0

    jogo = Jogo(gols1, gols2, time1, time2)
    jogo.ganhador()

    print(f"Resultado do jogo:\n{time1.get_nome_time()}  {jogo.get_gols_time1()} X {jogo.get_gols_time2()}  {time2.get_nome_time()}")

    gols1 = int(gols1)
    gols2 = int(gols2)

    if (gols1 > 0):
        artilheiros1 = []
        arti1 = random.choices(time1.lista_jogadores, weights = time1.finalizacoes, k = gols1)

        for art1 in arti1:
            art1.gols_marcados += 1
            artilheiros1.append(art1.get_nome())

        assistentes1 = []
        assis1 = random.choices(time1.lista_jogadores, weights = time1.passes, k = gols1)

        for assi1 in assis1:
            assi1.assistencias_feitas += 1
            assistentes1.append(assi1.get_nome())

        for f1 in range(gols1):
            if (assistentes1[f1] == artilheiros1[f1]):
                assis1[f1].assistencias_feitas -= 1
                assistentes1.pop(f1)

        print(f"Os gols do time {time1.get_nome_time()} foram de {artilheiros1}")
        print(f"As assistências do time {time1.get_nome_time()} foram de {assistentes1}")

    if (gols2 > 0):
        artilheiros2 = []
        arti2 = random.choices(time2.lista_jogadores, weights = time2.finalizacoes, k = gols2)

        for art2 in arti2:
            art2.gols_marcados += 1
            artilheiros2.append(art2.get_nome())

        assistentes2 = []
        assis2 = random.choices(time2.lista_jogadores, weights = time2.passes, k = gols2)

        for assi2 in assis2:
            assi2.assistencias_feitas += 1
            assistentes2.append(assi2.get_nome())

        for f2 in range(gols2):
            if (assistentes1[f2] == artilheiros1[f2]):
                assis2[f2].assistencias_feitas -= 1
                assistentes1.pop(f2)

        print(f"Os gols do time {time2.get_nome_time()} foram de {artilheiros2}")
        print(f"As assistências do time {time2.get_nome_time()} foram de {assistentes2}")

    

def consulta(time1, time2):
    print(f"{time1.get_nome_time()} - {time1.get_overall_time()}:\n")
    for i in range (11):
        print(f"{time1.lista_jogadores[i].get_pos()}: {time1.lista_jogadores[i].get_numero()} - {time1.lista_jogadores[i].get_nome()} - OVR: {time1.lista_jogadores[i].get_overall()}")

    print()
    print(f"{time2.get_nome_time()} - {time2.get_overall_time()}:\n")
    for i in range (11):
        print(f"{time2.lista_jogadores[i].get_pos()}: {time2.lista_jogadores[i].get_numero()} - {time2.lista_jogadores[i].get_nome()} - OVR: {time2.lista_jogadores[i].get_overall()}")

    print(f"Índice defensivo: {time1.get_indice_defensivo()} Índice ofensivo: {time1.get_indice_ofensivo()}")
    print(f"Índice defensivo: {time2.get_indice_defensivo()} Índice ofensivo: {time2.get_indice_ofensivo()}")


for r in range(5):
    consulta(time1, time2)
    simulacao(time1, time2)

for p1 in time1.lista_jogadores:
    print(p1.get_nome())
    print(p1.get_partidas_jogadas())
    print(p1.get_partidas_vencidas())
    print(p1.get_gols_marcados())
    print(p1.get_assistencias_feitas())

for p2 in time2.lista_jogadores:
    print(p2.get_nome())
    print(p2.get_partidas_jogadas())
    print(p2.get_partidas_vencidas())
    print(p2.get_gols_marcados())
    print(p2.get_assistencias_feitas())


