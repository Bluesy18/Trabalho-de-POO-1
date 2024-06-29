from classes import Time, Jogador, Jogo
from subclasses import Goleiro, Defensor, MeioCampista, Atacante
from timeAlcateia import timeAlcateia
from timeIFSC import timeIFSC
from random import randint
from presets import goleiros_preset, defensores_preset, meio_campistas_preset, atacantes_preset


lista_times = [timeAlcateia, timeIFSC]
lista_times[0].lista_jogadores[2].set_is_capitao()
lista_times[1].lista_jogadores[6].set_is_capitao()
posicoes = ["goleiro", "lat. esquerdo", "zag. esquerdo", "zag. direito", "lat. direito", "volante", "meio-campo esquerdo", "meio-campo direito", "ponta esquerda", "centro-avante", "ponta direita"]
posicoesAbv = ["GOL", "LE", "ZAGE", "ZAGD", "LD", "VOL", "MCE", "MCD", "PE", "ATA", "PD"]

flag = False

while True:
    print('Menu de Gerenciamento de Time')
    print('Escolha uma operação para realizar: ')
    print('1 - Cadastrar jogadores')
    print('2 - Alterar número da camisa de um jogador')
    print('3 - Consultar dados de um jogador')
    print('4 - Excluir/Substituir jogador')
    print('5 - Consultar times')
    print('6 - Simulação')
    print('0 - Encerrar programa')
    op = int(input('Escolha uma operação: '))
    
    if op == 1:
        jogadores = []
        goleiros = []
        defensores = []
        meio_campistas = []
        atacantes = []

        print("Bem vindo ao cadastro de jogadores, aqui você cadastrará cada jogador de um time de 11 jogadores:")
        
        nome_time = input("Primeiramente, digite o nome do time: ")
        print(f"Certo. Seu time será chamado de {nome_time} e jogará na formação 4-3-3:")
        
        for i in range(11):
            print(f"Agora, cadastre o {posicoes[i]}. Para isso você terá algumas opções:")
            
            if i == 0:
                print("1 - Selecionar cada atributo manualmente ")
                print("2 - Selecionar cada atributo aleatoriamente ")
                print("3 - Escolher atributos pré-selecionados, com base na Overall desejada ")
                esc = int(input("Escolha uma opção descrita acima para cadastrar o jogador: "))

                if esc == 1:
                    nome_jogador = input("Nome: ")
                    numero_jogador = input("Número da camisa: ")
                    habgoleiro = int(input("Habilidade do goleiro (1 a 10 estrelas): "))
                    '''g = Jogador(nome_jogador, numero_jogador, "GOL", habgoleiro, 0, 0, 0, 0, 0, 0)
                    '''
                    g = Goleiro(nome_jogador, numero_jogador, posicoesAbv[i], habgoleiro, 0, 0, 0, 0, 0, 0)
                    goleiros.append(g)
                    jogadores.append(g)
                
                elif esc == 2:
                    nome_jogador = input("Nome: ")
                    numero_jogador = input("Número da camisa: ")
                    habgoleiro = randint(0, 10)
                    g = Goleiro(nome_jogador, numero_jogador, posicoesAbv[i], habgoleiro, 0, 0, 0, 0, 0, 0)
                    goleiros.append(g)
                    jogadores.append(g)
                    
                elif esc == 3:
                    nome_jogador = input("Nome: ")
                    numero_jogador = input("Número da camisa: ")
                    overall = int(input("Selecione a Overall desejada para o Jogador (1 a 10 estrelas): "))
                    habgoleiro = goleiros_preset[overall-1][0]
                    g = Goleiro(nome_jogador, numero_jogador, posicoesAbv[i], habgoleiro, 0, 0, 0, 0, 0, 0)
                    goleiros.append(g)
                    jogadores.append(g)
            
            elif ((i >= 1) and (i <= 4)):
                print("1 - Selecionar cada atributo manualmente ")
                print("2 - Selecionar cada atributo aleatoriamente ")
                print("3 - Escolher atributos pré-selecionados, com base na Overall desejada ")
                esc = int(input("Escolha uma opção descrita acima para cadastrar o jogador: "))
            
                if esc == 1:
                    nome_jogador = input("Nome: ")
                    numero_jogador = input("Número da camisa: ")
                    defesa = int(input("Habilidade em defesa (1 a 10 estrelas): "))
                    fisico = int(input("Habilidade física (1 a 10 estrelas): "))
                    passe = int(input("Habilidade em passe (1 a 10 estrelas): "))
                    drible = int(input("Habilidade em drible (1 a 10 estrelas): "))
                    velocidade = int(input("Habilidade em velocidade (1 a 10 estrelas): "))
                    finalização = int(input("Habilidade em finalização (1 a 10 estrelas): "))
                    '''d = Jogador(nome_jogador, numero_jogador, "DEF", 1, defesa, fisico, 0, 0, 0, 0)
                    '''
                    d = Defensor(nome_jogador, numero_jogador, posicoesAbv[i], 1, defesa, fisico, passe, drible, velocidade, finalização)
                    defensores.append(d)
                    jogadores.append(d)
                
                elif esc == 2:
                    nome_jogador = input("Nome: ")
                    numero_jogador = input("Número da camisa: ")
                    defesa = randint(0, 10)
                    fisico = randint(0, 10)
                    passe = randint(0, 10)
                    drible = randint(0, 10)
                    velocidade = randint(0, 10)
                    finalização = randint(0, 10)
                    d = Defensor(nome_jogador, numero_jogador, posicoesAbv[i], 1, defesa, fisico, passe, drible, velocidade, finalização)
                    defensores.append(d)
                    jogadores.append(d)
                    
                elif esc == 3:
                    nome_jogador = input("Nome: ")
                    numero_jogador = input("Número da camisa: ")
                    overall = int(input("Selecione a Overall desejada para o Jogador (1 a 10 estrelas): "))
                    defesa = defensores_preset[overall-1][1]
                    fisico = defensores_preset[overall-1][2]
                    passe = defensores_preset[overall-1][3]
                    drible = defensores_preset[overall-1][4]
                    velocidade = defensores_preset[overall-1][5]
                    finalização = defensores_preset[overall-1][6]
                    d = Defensor(nome_jogador, numero_jogador, posicoesAbv[i], 1, defesa, fisico, passe, drible, velocidade, finalização)
                    defensores.append(d)
                    jogadores.append(d)
                          
            elif ((i >= 5) and (i <= 7)):
                print("1 - Selecionar cada atributo manualmente ")
                print("2 - Selecionar cada atributo aleatoriamente ")
                print("3 - Escolher atributos pré-selecionados, com base na Overall desejada ")
                esc = int(input("Escolha uma opção descrita acima para cadastrar o jogador: "))
            
                if esc == 1:
                    nome_jogador = input("Nome: ")
                    numero_jogador = input("Número da camisa: ")
                    defesa = int(input("Habilidade em defesa (1 a 10 estrelas): "))
                    fisico = int(input("Habilidade física (1 a 10 estrelas): "))
                    passe = int(input("Habilidade em passe (1 a 10 estrelas): "))
                    drible = int(input("Habilidade em drible (1 a 10 estrelas): "))
                    velocidade = int(input("Habilidade em velocidade (1 a 10 estrelas): "))
                    finalização = int(input("Habilidade em finalização (1 a 10 estrelas): "))
                    '''d = Jogador(nome_jogador, numero_jogador, "DEF", 1, defesa, fisico, 0, 0, 0, 0)
                    '''
                    m = MeioCampista(nome_jogador, numero_jogador, posicoesAbv[i], 1, defesa, fisico, passe, drible, velocidade, finalização)
                    meio_campistas.append(m)
                    jogadores.append(m)
                
                if esc == 2:
                    nome_jogador = input("Nome: ")
                    numero_jogador = input("Número da camisa: ")
                    defesa = randint(0, 10)
                    fisico = randint(0, 10)
                    passe = randint(0, 10)
                    drible = randint(0, 10)
                    velocidade = randint(0, 10)
                    finalização = randint(0, 10)
                    m = MeioCampista(nome_jogador, numero_jogador, posicoesAbv[i], 1, defesa, fisico, passe, drible, velocidade, finalização)
                    meio_campistas.append(m)
                    jogadores.append(m)
                    
                if esc == 3:
                    nome_jogador = input("Nome: ")
                    numero_jogador = input("Número da camisa: ")
                    overall = int(input("Selecione a Overall desejada para o Jogador (1 a 10 estrelas): "))
                    defesa = meio_campistas_preset[overall-1][1]
                    fisico = meio_campistas_preset[overall-1][2]
                    passe = meio_campistas_preset[overall-1][3]
                    drible = meio_campistas_preset[overall-1][4]
                    velocidade = meio_campistas_preset[overall-1][5]
                    finalização = meio_campistas_preset[overall-1][6]
                    m = MeioCampista(nome_jogador, numero_jogador, posicoesAbv[i], 1, defesa, fisico, passe, drible, velocidade, finalização)
                    meio_campistas.append(m)
                    jogadores.append(m)
                    
            elif ((i >= 8) and (i <= 10)):
                print("1 - Selecionar cada atributo manualmente ")
                print("2 - Selecionar cada atributo aleatoriamente ")
                print("3 - Escolher atributos pré-selecionados, com base na Overall desejada ")
                esc = int(input("Escolha uma opção descrita acima para cadastrar o jogador: "))
            
                if esc == 1:
                    nome_jogador = input("Nome: ")
                    numero_jogador = input("Número da camisa: ")
                    defesa = int(input("Habilidade em defesa (1 a 10 estrelas): "))
                    fisico = int(input("Habilidade física (1 a 10 estrelas): "))
                    passe = int(input("Habilidade em passe (1 a 10 estrelas): "))
                    drible = int(input("Habilidade em drible (1 a 10 estrelas): "))
                    velocidade = int(input("Habilidade em velocidade (1 a 10 estrelas): "))
                    finalização = int(input("Habilidade em finalização (1 a 10 estrelas): "))
                    '''d = Jogador(nome_jogador, numero_jogador, "DEF", 1, defesa, fisico, 0, 0, 0, 0)
                    '''
                    a = Atacante(nome_jogador, numero_jogador, posicoesAbv[i], 1, defesa, fisico, passe, drible, velocidade, finalização)
                    atacantes.append(a)
                    jogadores.append(a)
                
                if esc == 2:
                    nome_jogador = input("Nome: ")
                    numero_jogador = input("Número da camisa: ")
                    defesa = randint(0, 10)
                    fisico = randint(0, 10)
                    passe = randint(0, 10)
                    drible = randint(0, 10)
                    velocidade = randint(0, 10)
                    finalização = randint(0, 10)
                    a = Atacante(nome_jogador, numero_jogador, posicoesAbv[i], 1, defesa, fisico, passe, drible, velocidade, finalização)
                    atacantes.append(a)
                    jogadores.append(a)
                    
                if esc == 3:
                    nome_jogador = input("Nome: ")
                    numero_jogador = input("Número da camisa: ")
                    overall = int(input("Selecione a Overall desejada para o Jogador (1 a 10 estrelas): "))
                    defesa = atacantes_preset[overall-1][1]
                    fisico = atacantes_preset[overall-1][2]
                    passe = atacantes_preset[overall-1][3]
                    drible = atacantes_preset[overall-1][4]
                    velocidade = atacantes_preset[overall-1][5]
                    finalização = atacantes_preset[overall-1][6]
                    a = Atacante(nome_jogador, numero_jogador, posicoesAbv[i], 1, defesa, fisico, passe, drible, velocidade, finalização)
                    atacantes.append(a)
                    jogadores.append(a)
        for jogad in jogadores:
            print(f"{jogadores.index(jogad)+1} - {jogad.get_nome()}")
        cap_escolha = int(input("Escolha qual jogador será o capitão da equipe: "))
        jogadores[cap_escolha-1].set_is_capitao()
        t = Time(nome_time, jogadores, goleiros, defensores, meio_campistas, atacantes)
        lista_times.append(t)                 
        
    if op == 2:
        print("Bem vindo ao menu de alteração de camisa:")
        flag=False
        for _ in lista_times:
            print(f"{lista_times.index(_)+1} - {_.get_nome_time()}")
        time_camisa = int(input("Digite em qual dos times você deseja alterar a camisa: "))
        name = input("Digite o nome do jogador que terá o número da camisa modificado: ")
        
        for num in lista_times[time_camisa-1].lista_jogadores :        
            if name == num.get_nome():
                num_novo = input("Digite o novo número desejado para esse jogador: ")
                num.set_num(num_novo)
                print(f"Agora, {num.get_nome()} tem o número {num_novo} em sua camisa")
                flag=True
        if flag == False:
            print("Não existe um jogador cadastrado com esse nome!")
    
    if op == 3:
        print("Bem vindo ao menu de consulta de dados:")
        print("1 - Consulta pelo nome do jogador")
        print("2 - Consulta pelo número da camisa do jogador")
        con = int(input("Escolha uma das opções acima: "))
        
        
        if con == 1:
            flag=False
            for _ in lista_times:
                print(f"{lista_times.index(_)+1} - {_.get_nome_time()}")
            time_consulta = int(input("Digite em qual dos times você deseja consultar: "))
            name = input("Digite o nome do jogador que deseja consultar os dados: ")
            
            for jog in lista_times[time_consulta-1].lista_jogadores :
                if name == jog.get_nome():
                    print("Dados do jogador:")
                    if (jog.get_is_capitao() == True):
                        print("> CAPITÃO <")
                    print('Nome:', jog.get_nome())
                    print('Número da camisa:', jog.get_numero())
                    print('Posição:', jog.get_pos())
                    print('Overall(média de habilidade):', jog.get_overall())
                    print("Partidas jogadas:", jog.get_partidas_jogadas())
                    print("Partidas vencidas:", jog.get_partidas_vencidas())
                    print("Gols marcados:", jog.get_gols_marcados())
                    print("Assistências feitas:", jog.get_assistencias_feitas())
                    flag = True
            if flag == False:
                print("Não existe um jogador cadastrado com esse nome!")
        
        if con == 2:
            flag=False
            for _ in lista_times:
                print(f"{lista_times.index(_)+1} - {_.get_nome_time()}")
            time_consulta = int(input("Digite em qual dos times você deseja consultar: ")) 
            nume = input("Digite o número do jogador que deseja consultar os dados: ")
            
            for jog in lista_times[time_consulta-1].lista_jogadores:
                if nume == jog.get_numero():
                    print("Dados do jogador:")
                    if (jog.get_is_capitao() == True):
                        print("> CAPITÃO <")
                    print('Nome:', jog.get_nome())
                    print('Número da camisa:', jog.get_numero())
                    print('Posição:', jog.get_pos())
                    print('Overall(média de habilidade):', jog.get_overall())
                    print("Partidas jogadas:", jog.get_partidas_jogadas())
                    print("Partidas vencidas:", jog.get_partidas_vencidas())
                    print("Gols marcados:", jog.get_gols_marcados())
                    print("Assistências feitas:", jog.get_assistencias_feitas())
                    flag = True
            if flag == False:
                print("Não existe um jogador cadastrado com esse número de camisa!")
    
    if op == 4:
        print("Bem vindo ao menu de substituição de jogador:")
        for _ in lista_times:
            print(f"{lista_times.index(_)+1} - {_.get_nome_time()}")
        time_sub = int(input("Digite em qual dos times você deseja substituir: ")) 
        name = input("Digite o nome do jogador que deseja substituir: ")
        flag=False
        
        for i, j in enumerate(lista_times[time_sub-1].lista_jogadores):
            if name == j.get_nome():
                lista_times[time_sub-1].lista_jogadores.pop(i)
                if (j.get_pos() == "GOL"):
                    index_passado = lista_times[time_sub-1].lista_goleiros.index(j)
                    lista_times[time_sub-1].lista_goleiros.remove(j)
                elif ((j.get_pos() == "LE") or (j.get_pos() == "ZAGE") or (j.get_pos() == "ZAGD") or (j.get_pos() == "LD")):
                    index_passado = lista_times[time_sub-1].lista_defensores.index(j)
                    lista_times[time_sub-1].lista_defensores.remove(j)
                elif ((j.get_pos() == "VOL") or (j.get_pos() == "MCE") or (j.get_pos() == "MCD")):
                    index_passado = lista_times[time_sub-1].lista_meio_campistas.index(j)
                    lista_times[time_sub-1].lista_meio_campistas.remove(j)
                elif ((j.get_pos() == "PE") or (j.get_pos() == "ATA") or (j.get_pos() == "PD")):
                    index_passado = lista_times[time_sub-1].lista_atacantes.index(j)
                    lista_times[time_sub-1].lista_atacantes.remove(j)
                print(f"Certo. Agora cadastre um novo jogador para substiuir o anterior, para isso, ele terá a posição {j.get_pos()} também:")
                print("1 - Selecionar cada atributo manualmente ")
                print("2 - Selecionar cada atributo aleatoriamente ")
                print("3 - Escolher atributos pré-selecionados, com base na Overall desejada ")
                esc = int(input("Escolha uma opção descrita acima para cadastrar o jogador: "))
                
                if (j.get_pos() == "GOL"):
                    if esc == 1:
                        nome_jogador = input("Nome: ")
                        numero_jogador = input("Número da camisa: ")
                        habgoleiro = int(input("Habilidade do goleiro (0 a 10 estrelas): "))                   
                        g = Goleiro(nome_jogador, numero_jogador, posicoesAbv[i], habgoleiro, 0, 0, 0, 0, 0, 0)
                        lista_times[time_sub-1].lista_goleiros.insert(index_passado, g)
                        lista_times[time_sub-1].lista_jogadores.insert(i, g)
                
                    elif esc == 2:
                        nome_jogador = input("Nome: ")
                        numero_jogador = input("Número da camisa: ")
                        habgoleiro = randint(0, 10)
                        g = Goleiro(nome_jogador, numero_jogador, posicoesAbv[i], habgoleiro, 0, 0, 0, 0, 0, 0)
                        lista_times[time_sub-1].lista_goleiros.insert(index_passado, g)
                        lista_times[time_sub-1].lista_jogadores.insert(i, g)
                        
                    elif esc == 3:
                        nome_jogador = input("Nome: ")
                        numero_jogador = input("Número da camisa: ")
                        overall = int(input("Selecione a Overall desejada para o Jogador (0 a 10 estrelas): "))
                        habgoleiro = goleiros_preset[overall-1][0]
                        g = Goleiro(nome_jogador, numero_jogador, posicoesAbv[i], habgoleiro, 0, 0, 0, 0, 0, 0)
                        lista_times[time_sub-1].lista_goleiros.insert(index_passado, g)
                        lista_times[time_sub-1].lista_jogadores.insert(i, g)
                
                elif ((j.get_pos() == "LE") or (j.get_pos() == "ZAGE") or (j.get_pos() == "ZAGD") or (j.get_pos() == "LD")):               
                    if esc == 1:
                        nome_jogador = input("Nome: ")
                        numero_jogador = input("Número da camisa: ")
                        defesa = int(input("Habilidade em defesa (0 a 10 estrelas): "))
                        fisico = int(input("Habilidade física (0 a 10 estrelas): "))
                        passe = int(input("Habilidade em passe (0 a 10 estrelas): "))
                        drible = int(input("Habilidade em drible (0 a 10 estrelas): "))
                        velocidade = int(input("Habilidade em velocidade (0 a 10 estrelas): "))
                        finalização = int(input("Habilidade em finalização (0 a 10 estrelas): "))
                        
                        d = Defensor(nome_jogador, numero_jogador, posicoesAbv[i], 1, defesa, fisico, passe, drible, velocidade, finalização)
                        lista_times[time_sub-1].lista_defensores.insert(index_passado, d)
                        lista_times[time_sub-1].lista_jogadores.insert(i, d)
                
                    elif esc == 2:
                        nome_jogador = input("Nome: ")
                        numero_jogador = input("Número da camisa: ")
                        defesa = randint(0, 10)
                        fisico = randint(0, 10)
                        passe = randint(0, 10)
                        drible = randint(0, 10)
                        velocidade = randint(0, 10)
                        finalização = randint(0, 10)
                        d = Defensor(nome_jogador, numero_jogador, posicoesAbv[i], 1, defesa, fisico, passe, drible, velocidade, finalização)
                        lista_times[time_sub-1].lista_defensores.insert(index_passado, d)
                        lista_times[time_sub-1].lista_jogadores.insert(i, d)
                        
                    elif esc == 3:
                        nome_jogador = input("Nome: ")
                        numero_jogador = input("Número da camisa: ")
                        overall = int(input("Selecione a Overall desejada para o Jogador (0 a 10 estrelas): "))
                        defesa = defensores_preset[overall-1][1]
                        fisico = defensores_preset[overall-1][2]
                        passe = defensores_preset[overall-1][3]
                        drible = defensores_preset[overall-1][4]
                        velocidade = defensores_preset[overall-1][5]
                        finalização = defensores_preset[overall-1][6]
                        d = Defensor(nome_jogador, numero_jogador, posicoesAbv[i], 1, defesa, fisico, passe, drible, velocidade, finalização)
                        lista_times[time_sub-1].lista_defensores.insert(index_passado, d)
                        lista_times[time_sub-1].lista_jogadores.insert(i, d)
                
                elif ((j.get_pos() == "VOL") or (j.get_pos() == "MCE") or (j.get_pos() == "MCD")):                   
                    if esc == 1:
                        nome_jogador = input("Nome: ")
                        numero_jogador = input("Número da camisa: ")
                        defesa = int(input("Habilidade em defesa (0 a 10 estrelas): "))
                        fisico = int(input("Habilidade física (0 a 10 estrelas): "))
                        passe = int(input("Habilidade em passe (0 a 10 estrelas): "))
                        drible = int(input("Habilidade em drible (0 a 10 estrelas): "))
                        velocidade = int(input("Habilidade em velocidade (0 a 10 estrelas): "))
                        finalização = int(input("Habilidade em finalização (0 a 10 estrelas): "))

                        m = MeioCampista(nome_jogador, numero_jogador, posicoesAbv[i], 1, defesa, fisico, passe, drible, velocidade, finalização)
                        lista_times[time_sub-1].lista_meio_campistas.insert(index_passado, m)
                        lista_times[time_sub-1].lista_jogadores.insert(i, m)
                
                    elif esc == 2:
                        nome_jogador = input("Nome: ")
                        numero_jogador = input("Número da camisa: ")
                        defesa = randint(0, 10)
                        fisico = randint(0, 10)
                        passe = randint(0, 10)
                        drible = randint(0, 10)
                        velocidade = randint(0, 10)
                        finalização = randint(0, 10)
                        m = MeioCampista(nome_jogador, numero_jogador, posicoesAbv[i], 1, defesa, fisico, passe, drible, velocidade, finalização)
                        lista_times[time_sub-1].lista_meio_campistas.insert(index_passado, m)
                        lista_times[time_sub-1].lista_jogadores.insert(i, m)
                        
                    elif esc == 3:
                        nome_jogador = input("Nome: ")
                        numero_jogador = input("Número da camisa: ")
                        overall = int(input("Selecione a Overall desejada para o Jogador (0 a 10 estrelas): "))
                        defesa = meio_campistas_preset[overall-1][1]
                        fisico = meio_campistas_preset[overall-1][2]
                        passe = meio_campistas_preset[overall-1][3]
                        drible = meio_campistas_preset[overall-1][4]
                        velocidade = meio_campistas_preset[overall-1][5]
                        finalização = meio_campistas_preset[overall-1][6]
                        m = MeioCampista(nome_jogador, numero_jogador, posicoesAbv[i], 1, defesa, fisico, passe, drible, velocidade, finalização)
                        lista_times[time_sub-1].lista_meio_campistas.insert(index_passado, m)
                        lista_times[time_sub-1].lista_jogadores.insert(i, m)
                
                elif ((j.get_pos() == "PE") or (j.get_pos() == "ATA") or (j.get_pos() == "PD")): 
                    if esc == 1:
                        nome_jogador = input("Nome: ")
                        numero_jogador = input("Número da camisa: ")
                        defesa = int(input("Habilidade em defesa (0 a 10 estrelas): "))
                        fisico = int(input("Habilidade física (0 a 10 estrelas): "))
                        passe = int(input("Habilidade em passe (0 a 10 estrelas): "))
                        drible = int(input("Habilidade em drible (0 a 10 estrelas): "))
                        velocidade = int(input("Habilidade em velocidade (0 a 10 estrelas): "))
                        finalização = int(input("Habilidade em finalização (0 a 10 estrelas): "))

                        a = Atacante(nome_jogador, numero_jogador, posicoesAbv[i], 1, defesa, fisico, passe, drible, velocidade, finalização)
                        lista_times[time_sub-1].lista_atacantes.insert(index_passado, a)
                        lista_times[time_sub-1].lista_jogadores.insert(i, a)
                
                    elif esc == 2:
                        nome_jogador = input("Nome: ")
                        numero_jogador = input("Número da camisa: ")
                        defesa = randint(0, 10)
                        fisico = randint(0, 10)
                        passe = randint(0, 10)
                        drible = randint(0, 10)
                        velocidade = randint(0, 10)
                        finalização = randint(0, 10)
                        a = Atacante(nome_jogador, numero_jogador, posicoesAbv[i], 1, defesa, fisico, passe, drible, velocidade, finalização)
                        lista_times[time_sub-1].lista_atacantes.insert(index_passado, a)
                        lista_times[time_sub-1].lista_jogadores.insert(i, a)
                        
                    elif esc == 3:
                        nome_jogador = input("Nome: ")
                        numero_jogador = input("Número da camisa: ")
                        overall = int(input("Selecione a Overall desejada para o Jogador (0 a 10 estrelas): "))
                        defesa = atacantes_preset[overall-1][1]
                        fisico = atacantes_preset[overall-1][2]
                        passe = atacantes_preset[overall-1][3]
                        drible = atacantes_preset[overall-1][4]
                        velocidade = atacantes_preset[overall-1][5]
                        finalização = atacantes_preset[overall-1][6]
                        a = Atacante(nome_jogador, numero_jogador, posicoesAbv[i], 1, defesa, fisico, passe, drible, velocidade, finalização)
                        lista_times[time_sub-1].lista_atacantes.insert(index_passado, a)
                        lista_times[time_sub-1].lista_jogadores.insert(i, a)
                flag=True
        if flag == False:
            print("Não existe um jogador cadastrado com esse nome!")
    
    if op == 5:
        print("Bem vindo à consulta de times.")
        for _ in lista_times:
            print(f"{lista_times.index(_)+1} - {_.get_nome_time()}")
        time_consultaGeral = int(input("Digite qual dos times você deseja consultar: "))     
        
        print(f"Nome do time: {lista_times[time_consultaGeral-1].get_nome_time}")

        for timeCon in lista_times[time_consultaGeral-1].lista_jogadores:
            if (timeCon.get_is_capitao() == True):
                print(f"{timeCon.get_pos()}: {timeCon.get_numero()} - {timeCon.get_nome()} (c) - OVR: {timeCon.get_overall()}")
            else:
                print(f"{timeCon.get_pos()}: {timeCon.get_numero()} - {timeCon.get_nome()} - OVR: {timeCon.get_overall()}")

    if op == 6:
        print("Bem vindo à simulação.")
        lista_simu = lista_times[:]
        for _ in lista_simu:
            print(f"{lista_simu.index(_)+1} - {_.get_nome_time()}")
        time_simu = int(input("Digite qual dos times você deseja inserir na simulação: "))
        time1 = lista_simu[time_simu-1]
        lista_simu.remove(time1)
        for _ in lista_simu:
            print(f"{lista_simu.index(_)+1} - {_.get_nome_time()}")
        time_simu = int(input("Digite qual dos times restantes você deseja inserir na simulação: "))
        time2 = lista_simu[time_simu-1]

        jogo = Jogo(time1, time2)
        jogo.simulacao()
        jogo.perdedor()
        jogo.zebra()
        jogo.simulacao()
        jogo.resultado()
        jogo.ganhador()

    if op == 0:
        break



