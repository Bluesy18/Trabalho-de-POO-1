from time1 import time1
from time2 import time2

print(f"{time1.get_nome_time()} - {time1.get_overall_time()}:\n")
for i in range (11):
    print(f"{time1.lista_jogadores[i].get_pos()}: {time1.lista_jogadores[i].get_numero()} - {time1.lista_jogadores[i].get_nome()} - OVR: {time1.lista_jogadores[i].get_overall()}")

print()
print(f"{time2.get_nome_time()} - {time2.get_overall_time()}:\n")
for i in range (11):
    print(f"{time2.lista_jogadores[i].get_pos()}: {time2.lista_jogadores[i].get_numero()} - {time2.lista_jogadores[i].get_nome()} - OVR: {time2.lista_jogadores[i].get_overall()}")

print(time1.get_indice_defensivo())
print(time2.get_indice_defensivo())