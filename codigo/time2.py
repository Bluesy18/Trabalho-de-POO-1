from classes import Time
from subclasses import Goleiro, Defensor, MeioCampista, Atacante

# j1 = Defensor(nome_jogador, numero_jogador, pos_jogador, habgoleiro, defesa, fisico, passe, drible, velocidade, finalizacao)

j1 = Goleiro("Truppel", "1", "GOL", 10, 0, 0, 0, 0, 0, 0)
j2 = Defensor("Andrei", "2", "LE", 1, 9, 5, 9, 7, 5, 4)
j3 = Defensor("Diogo", "5", "ZAG", 8, 7, 10, 7, 4, 2, 8)
j4 = Defensor("Thiago", "42", "ZAG", 1, 10, 3, 6, 2, 2, 6)
j5 = Defensor("Davi", "12", "LD", 8, 9, 6, 7, 6, 8, 4)
j6 = MeioCampista("Denian", "8", "VOL", 4, 7, 8, 4, 6, 7, 5)
j7 = MeioCampista("Vini", "7" , "MC", 6, 5, 9, 5, 7, 6, 8)
j8 = MeioCampista("André", "11", "MC", 1, 3, 6, 7, 6, 6, 6)
j9 = Atacante("Gustavo", "24", "PE", 9, 5, 9, 6, 7, 6, 6)
j10 = Atacante("Erick", "9", "ATA", 1, 3, 4, 3, 1, 3, 4)
j11 = Atacante("Bryan", "10", "PD", 6, 3, 5, 7, 10, 8, 7)

jogadores = [j1, j2, j3, j4, j5, j6, j7, j8, j9, j10, j11]
goleiros = [j1]
defensores = [j2, j3, j4, j5]
meio_campistas = [j6, j7, j8]
atacantes = [j9, j10, j11]

time2 = Time("IFSC-SJ", jogadores, goleiros, defensores, meio_campistas, atacantes)