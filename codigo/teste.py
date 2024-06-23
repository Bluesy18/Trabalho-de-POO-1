import random
from classes import Jogo
from time1 import time1
from time2 import time2

print(f"{time1.get_nome_time()} - {time1.get_overall_time()}:\n")
for i in range (11):
    print(f"{time1.lista_jogadores[i].get_pos()}: {time1.lista_jogadores[i].get_numero()} - {time1.lista_jogadores[i].get_nome()} - OVR: {time1.lista_jogadores[i].get_overall()}")

print()
print(f"{time2.get_nome_time()} - {time2.get_overall_time()}:\n")
for i in range (11):
    print(f"{time2.lista_jogadores[i].get_pos()}: {time2.lista_jogadores[i].get_numero()} - {time2.lista_jogadores[i].get_nome()} - OVR: {time2.lista_jogadores[i].get_overall()}")

print(f"Índice defensivo: {time1.get_indice_defensivo()} Índice ofensivo: {time1.get_indice_ofensivo()}")
print(f"Índice defensivo: {time2.get_indice_defensivo()} Índice ofensivo: {time2.get_indice_ofensivo()}")

gols1 = (time1.get_indice_ofensivo()-time2.get_indice_defensivo())

if (gols1 < 0):
    gols1 = 0

gols2 = (time2.get_indice_ofensivo()-time1.get_indice_defensivo())

if (gols2 < 0):
    gols2 = 0

jogo = Jogo(gols1, gols2)

print(f"Resultado do jogo:\n{time1.get_nome_time()}  {jogo.get_gols_time1()} X {jogo.get_gols_time2()}  {time2.get_nome_time()}")

gols1 = int(gols1)
gols2 = int(gols2)

if (gols1 > 0):
    artilheiros1 = []
    arti1 = random.choices(time1.lista_jogadores, weights = time1.finalizacoes, k = gols1)

    for art1 in arti1:
        artilheiros1.append(art1.get_nome())

    assistentes1 = []
    assis1 = random.choices(time1.lista_jogadores, weights = time1.passes, k = gols1)

    for assi1 in assis1:
        assistentes1.append(assi1.get_nome())

    print(f"Os gols do time {time1.get_nome_time()} foram de {artilheiros1}")
    print(f"As assistências do time {time1.get_nome_time()} foram de {assistentes1}")

if (gols2 > 0):
    artilheiros2 = []
    arti2 = random.choices(time2.lista_jogadores, weights = time2.finalizacoes, k = gols2)

    for art2 in arti2:
        artilheiros2.append(art2.get_nome())

    assistentes2 = []
    assis2 = random.choices(time2.lista_jogadores, weights = time2.passes, k = gols2)

    for assi2 in assis2:
        assistentes2.append(assi2.get_nome())

    print(f"Os gols do time {time2.get_nome_time()} foram de {artilheiros2}")
    print(f"As assistências do time {time2.get_nome_time()} foram de {assistentes2}")


# print(time1.get_finalizacoes())
# print(time1.get_finalizacoes_sorted())
# print(time1.get_maiores_fin())
# print(time1.get_artilheiros())