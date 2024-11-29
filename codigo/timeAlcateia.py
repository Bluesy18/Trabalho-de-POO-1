from Time import Time
from Goleiro import Goleiro
from Defensor import Defensor
from MeioCampista import MeioCampista
from Atacante import Atacante

# j1 = Defensor(nome_jogador, numero_jogador, pos_jogador, habgoleiro, defesa, fisico, passe, drible, velocidade, finalizacao)

j1 = Goleiro("Bernardo", "1", "GOL", 9, 0, 0, 0, 0, 0, 0)
j2 = Defensor("Tribeck", "5", "LE", 1, 8, 6, 7, 8, 4, 5)
j3 = Defensor("Marraui", "4", "ZAGE", 8, 9, 10, 5, 3, 6, 6)
j4 = Defensor("Caetano", "3", "ZAGD", 1, 7, 7, 6, 5, 6, 4)
j5 = Defensor("Pedrão", "2", "LD", 1, 4, 6, 5, 2, 3, 1)
j6 = MeioCampista("Clasen", "8", "VOL", 4, 5, 7, 9, 6, 5, 7)
j7 = MeioCampista("Janders", "10", "MCE", 3, 6, 9, 7, 6, 4, 6)
j8 = MeioCampista("Ilton", "6", "MCD", 1, 4, 9, 4, 6, 8, 7)
j9 = Atacante("Kendrick", "7", "PE", 1, 4, 8, 8, 5, 6, 7)
j10 = Atacante("Davi Goat", "9", "ATA", 10, 10, 10, 10, 10, 10, 10)
j11 = Atacante("Kern", "11", "PD", 9, 4, 7, 7, 9, 8, 7)



jogadores = [j1, j2, j3, j4, j5, j6, j7, j8, j9, j10, j11]
goleiros = [j1]
defensores = [j2, j3, j4, j5]
meio_campistas = [j6, j7, j8]
atacantes = [j9, j10, j11]

timeAlcateia = Time("Alcateia", jogadores, goleiros, defensores, meio_campistas, atacantes)