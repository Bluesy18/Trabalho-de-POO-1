from classes import Jogador,Time

jogadores = []

j1 = Jogador("Davi", int(12))
j2 = Jogador("André", int(10))

jogadores.append(j1)
jogadores.append(j2)

t1 = Time("Avaí", jogadores)

for jog in jogadores:
    print(jog.get_nome(), jog.get_numero())
    
    
for i in range (2):
    print(t1.lista_jogadores[i].get_nome())
    



    





