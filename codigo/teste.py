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