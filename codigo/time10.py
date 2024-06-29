from classes import Time
from subclasses import Goleiro, Defensor, MeioCampista, Atacante

# j1 = Defensor(nome_jogador, numero_jogador, pos_jogador, habgoleiro, defesa, fisico, passe, drible, velocidade, finalizacao)

j1 = Goleiro("Truppel", "1", "GOL", 10, 0, 0, 0, 0, 0, 0)
j2 = Defensor("Andrei", "2", "LE", 10, 10, 10, 10, 10, 10, 10)
j3 = Defensor("Diogo", "5", "ZAGE", 10, 10, 10, 10, 10, 10, 10)
j4 = Defensor("Thiago", "42", "ZAGD", 10, 10, 10, 10, 10, 10, 10)
j5 = Defensor("Davi", "12", "LD", 10, 10, 10, 10, 10, 10, 10)
j6 = MeioCampista("Denian", "8", "VOL", 10, 10, 10, 10, 10, 10, 10)
j7 = MeioCampista("Vini", "7" , "MCE", 10, 10, 10, 10, 10, 10, 10)
j8 = MeioCampista("André", "11", "MCD", 10, 10, 10, 10, 10, 10, 10)
j9 = Atacante("Gustavo", "24", "PE", 10, 10, 10, 10, 10, 10, 10)
j10 = Atacante("Erick", "9", "ATA", 10, 10, 10, 10, 10, 10, 10)
j11 = Atacante("Bryan", "10", "PD", 10, 10, 10, 10, 10, 10, 10)



jogadores = [j1, j2, j3, j4, j5, j6, j7, j8, j9, j10, j11]
goleiros = [j1]
defensores = [j2, j3, j4, j5]
meio_campistas = [j6, j7, j8]
atacantes = [j9, j10, j11]

time10 = Time("time10", jogadores, goleiros, defensores, meio_campistas, atacantes)