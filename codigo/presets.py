from subclasses import Goleiro, Defensor, MeioCampista, Atacante

# j1 = Defensor(nome_jogador, numero_jogador, pos_jogador, habgoleiro, defesa, fisico, passe, drible, velocidade, finalizacao)

gol1 = [1, 0, 0, 0, 0, 0, 0]
gol2 = [2, 0, 0, 0, 0, 0, 0]
gol3 = [3, 0, 0, 0, 0, 0, 0]
gol4 = [4, 0, 0, 0, 0, 0, 0]
gol5 = [5, 0, 0, 0, 0, 0, 0]
gol6 = [6, 0, 0, 0, 0, 0, 0]
gol7 = [7, 0, 0, 0, 0, 0, 0]
gol8 = [8, 0, 0, 0, 0, 0, 0]
gol9 = [9, 0, 0, 0, 0, 0, 0]
gol10 = [10, 0, 0, 0, 0, 0, 0]

goleiros_preset = [gol1, gol2, gol3, gol4, gol5, gol6, gol7, gol8, gol9, gol10]

overall = int(input("digite o over q tu quer: "))

habgoleiro = goleiros_preset[overall-1][0]

print(habgoleiro)





# def1 = Defensor("b", "0", "DEF", 1, 1, 1, 1, 1, 1, 1)
# def2 = Defensor("b", "0", "DEF", 1, 2, 2, 2, 1, 1, 1)
# def3 = Defensor("b", "0", "DEF", 1, 3, 3, 2, 1, 1, 1)
# def4 = Defensor("b", "0", "DEF", 1, 4, 4, 3, 2, 2, 2)
# def5 = Defensor("b", "0", "DEF", 1, 5, 5, 4, 3, 3, 2)
# def6 = Defensor("b", "0", "DEF", 1, 6, 6, 5, 4, 4, 2)
# def7 = Defensor("b", "0", "DEF", 1, 7, 7, 6, 5, 5, 3)
# def8 = Defensor("b", "0", "DEF", 1, 8, 8, 7, 6, 6, 3)
# def9 = Defensor("b", "0", "DEF", 1, 9, 9, 8, 7, 7, 3)
# def10 = Defensor("b", "0", "DEF", 1, 10, 10, 9, 8, 8, 4)

# defensores_preset = [def1, def2, def3, def4, def5, def6, def7, def8, def9, def10]

# mei1 = MeioCampista("c", "0", "MEI", 1, 1, 1, 1, 1, 1, 1)
# mei2 = MeioCampista("c", "0", "MEI", 1, 2, 2, 2, 2, 2, 2)
# mei3 = MeioCampista("c", "0", "MEI", 1, 3, 3, 3, 3, 3, 3)
# mei4 = MeioCampista("c", "0", "MEI", 1, 4, 4, 4, 4, 4, 4)
# mei5 = MeioCampista("c", "0", "MEI", 1, 5, 5, 5, 5, 5, 5)
# mei6 = MeioCampista("c", "0", "MEI", 1, 6, 6, 6, 6, 6, 6)
# mei7 = MeioCampista("c", "0", "MEI", 1, 7, 7, 7, 7, 7, 7)
# mei8 = MeioCampista("c", "0", "MEI", 1, 8, 8, 8, 8, 8, 8)
# mei9 = MeioCampista("c", "0", "MEI", 1, 9, 9, 9, 9, 9, 9)
# mei10 = MeioCampista("c", "0", "MEI", 1, 10, 10, 10, 10, 10, 10)

# meio_campistas_preset = [mei1, mei2, mei3, mei4, mei5, mei6, mei7, mei8, mei9, mei10]

# ata1 = Atacante("d", "0", "ATA", 1, 1, 1, 1, 1, 1, 1)
# ata2 = Atacante("d", "0", "ATA", 1, 2, 1, 1, 2, 2, 2)
# ata3 = Atacante("d", "0", "ATA", 1, 2, 1, 1, 3, 3, 3)
# ata4 = Atacante("d", "0", "ATA", 1, 2, 2, 2, 4, 4, 4)
# ata5 = Atacante("d", "0", "ATA", 1, 3, 3, 3, 5, 5, 5)
# ata6 = Atacante("d", "0", "ATA", 1, 3, 4, 4, 6, 6, 6)
# ata7 = Atacante("d", "0", "ATA", 1, 3, 5, 5, 7, 7, 7)
# ata8 = Atacante("d", "0", "ATA", 1, 4, 6, 6, 8, 8, 8)
# ata9 = Atacante("d", "0", "ATA", 1, 4, 7, 7, 9, 9, 9)
# ata10 = Atacante("d", "0", "ATA", 1, 4, 8, 8, 10, 10, 10)

# atacantes_preset = [ata1, ata2, ata3, ata4, ata5, ata6, ata7, ata8, ata9, ata10]

# for i in atacantes_preset:
#   print(i.get_overall())