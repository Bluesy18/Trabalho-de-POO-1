from time1 import time1

# jogadores = []

# nome_jogador = input("Digite o nome do jogador: ")
# numero_jogador = input("Digite o número do jogador: ")
# habgoleiro = int(input("Digite a habilidade como goleiro do jogador: "))
# defesa = int(input("Digite a defesa do jogador: "))
# fisico = int(input("Digite o fisico do jogador: "))
# passe = int(input("Digite o passe do jogador: "))
# drible = int(input("Digite o drible do jogador: "))
# velocidade = int(input("Digite a velocidade do jogador: "))
# finalizacao = int(input("Digite a finalização do jogador: "))

# j1 = Defensor("Davi", int(12))
# j2 = Jogador("André", int(10))

# jogadores.append(j1)
# jogadores.append(j2)

# j1 = Defensor(nome_jogador, numero_jogador, habgoleiro, defesa, fisico, passe, drible, velocidade, finalizacao)
# jogadores.append(j1)

#t1 = Time("Avaí", jogadores)

# for jog in jogadores:
#     print(jog.get_nome(), jog.get_numero())
    
print(f"{time1.get_nome_time()}:\n")
for i in range (11):
    print(f"{time1.lista_jogadores[i].get_pos()}: {time1.lista_jogadores[i].get_numero()} - {time1.lista_jogadores[i].get_nome()} - OVR: {time1.lista_jogadores[i].get_overall()}")
    



    





