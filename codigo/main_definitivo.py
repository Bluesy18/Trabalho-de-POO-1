from classes import Time, Jogador, Jogo
from subclasses import Goleiro, Defensor, MeioCampista, Atacante
from time1 import time1
from codigo.timeIFSC import time2
from random import randint


times_cadastrados = 2
lista_times = [time1, time2]
posicoes = ["Goleiro", "Lat. Esquerdo", "Zag. Esquerdo", "Zag. Direito", "Lat. Direito", "Volante", "Meio-Campo Esquerdo", "Meio-Campo Direito", "Ponta Esquerda", "Centro Avante", "Ponta Esquerda"]
lista_times[0].lista_jogadores[2].set_is_capitao()
lista_times[1].lista_jogadores[6].set_is_capitao()


flag = False

while True:
    print('Menu de Gerenciamento de Time')
    print('Escolha uma operação para realizar: ')
    print('1 - Cadastrar jogadores')
    print('2 - Alterar número da camisa de um jogador')
    print('3 - Consultar dados de um jogador')
    print('4 - Excluir jogador')
    print('5 - Consultar times')
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
                    habgoleiro = int(input("Habilidade do goleiro (0 a 10 estrelas): "))
                    '''g = Jogador(nome_jogador, numero_jogador, "GOL", habgoleiro, 0, 0, 0, 0, 0, 0)
                    '''
                    g = Goleiro(nome_jogador, numero_jogador, "GOL", habgoleiro, 0, 0, 0, 0, 0, 0)
                    goleiros.append(g)
                    jogadores.append(g)
                
                if esc == 2:
                    nome_jogador = input("Nome: ")
                    numero_jogador = input("Número da camisa: ")
                    habgoleiro = randint(0, 10)
                    g = Goleiro(nome_jogador, numero_jogador, "GOL", habgoleiro, 0, 0, 0, 0, 0, 0)
                    goleiros.append(g)
                    jogadores.append(g)
                    
                if esc == 3:
                    nome_jogador = input("Nome: ")
                    numero_jogador = input("Número da camisa: ")
            
            elif ((i >= 1) or (i <= 4)):
                print("1 - Selecionar cada atributo manualmente ")
                print("2 - Selecionar cada atributo aleatoriamente ")
                print("3 - Escolher atributos pré-selecionados, com base na Overall desejada ")
                esc = int(input("Escolha uma opção descrita acima para cadastrar o jogador: "))
            
                if esc == 1:
                    nome_jogador = input("Nome: ")
                    numero_jogador = input("Número da camisa: ")
                    defesa = int(input("Habilidade em defesa (0 a 10 estrelas): "))
                    fisico = int(input("Habilidade física (0 a 10 estrelas): "))
                    passe = int(input("Habilidade em passe (0 a 10 estrelas): "))
                    drible = int(input("Habilidade em drible (0 a 10 estrelas): "))
                    velocidade = int(input("Habilidade em velocidade (0 a 10 estrelas): "))
                    finalização = int(input("Habilidade em finalização (0 a 10 estrelas): "))
                    '''d = Jogador(nome_jogador, numero_jogador, "DEF", 1, defesa, fisico, 0, 0, 0, 0)
                    '''
                    d = Defensor(nome_jogador, numero_jogador, "DEF", 1, defesa, fisico, passe, drible, velocidade, finalização)
                    defensores.append(d)
                    jogadores.append(d)
                
                if esc == 2:
                    nome_jogador = input("Nome: ")
                    numero_jogador = input("Número da camisa: ")
                    defesa = randint(0, 10)
                    fisico = randint(0, 10)
                    passe = randint(0, 10)
                    drible = randint(0, 10)
                    velocidade = randint(0, 10)
                    finalização = randint(0, 10)
                    d = Defensor(nome_jogador, numero_jogador, "DEF", 1, defesa, fisico, passe, drible, velocidade, finalização)
                    defensores.append(d)
                    jogadores.append(d)
                    
                if esc == 3:
                    nome_jogador = input("Nome: ")
                    numero_jogador = input("Número da camisa: ")
                    
            elif ((i >= 5) or (i <= 7)):
                print("1 - Selecionar cada atributo manualmente ")
                print("2 - Selecionar cada atributo aleatoriamente ")
                print("3 - Escolher atributos pré-selecionados, com base na Overall desejada ")
                esc = int(input("Escolha uma opção descrita acima para cadastrar o jogador: "))
            
                if esc == 1:
                    nome_jogador = input("Nome: ")
                    numero_jogador = input("Número da camisa: ")
                    defesa = int(input("Habilidade em defesa (0 a 10 estrelas): "))
                    fisico = int(input("Habilidade física (0 a 10 estrelas): "))
                    passe = int(input("Habilidade em passe (0 a 10 estrelas): "))
                    drible = int(input("Habilidade em drible (0 a 10 estrelas): "))
                    velocidade = int(input("Habilidade em velocidade (0 a 10 estrelas): "))
                    finalização = int(input("Habilidade em finalização (0 a 10 estrelas): "))
                    '''d = Jogador(nome_jogador, numero_jogador, "DEF", 1, defesa, fisico, 0, 0, 0, 0)
                    '''
                    m = MeioCampista(nome_jogador, numero_jogador, "MEI", 1, defesa, fisico, passe, drible, velocidade, finalização)
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
                    m = MeioCampista(nome_jogador, numero_jogador, "MEI", 1, defesa, fisico, passe, drible, velocidade, finalização)
                    meio_campistas.append(m)
                    jogadores.append(m)
                    
                if esc == 3:
                    nome_jogador = input("Nome: ")
                    numero_jogador = input("Número da camisa: ")
                    
            elif ((i >= 8) or (i <= 10)):
                print("1 - Selecionar cada atributo manualmente ")
                print("2 - Selecionar cada atributo aleatoriamente ")
                print("3 - Escolher atributos pré-selecionados, com base na Overall desejada ")
                esc = int(input("Escolha uma opção descrita acima para cadastrar o jogador: "))
            
                if esc == 1:
                    nome_jogador = input("Nome: ")
                    numero_jogador = input("Número da camisa: ")
                    defesa = int(input("Habilidade em defesa (0 a 10 estrelas): "))
                    fisico = int(input("Habilidade física (0 a 10 estrelas): "))
                    passe = int(input("Habilidade em passe (0 a 10 estrelas): "))
                    drible = int(input("Habilidade em drible (0 a 10 estrelas): "))
                    velocidade = int(input("Habilidade em velocidade (0 a 10 estrelas): "))
                    finalização = int(input("Habilidade em finalização (0 a 10 estrelas): "))
                    '''d = Jogador(nome_jogador, numero_jogador, "DEF", 1, defesa, fisico, 0, 0, 0, 0)
                    '''
                    a = Atacante(nome_jogador, numero_jogador, "ATA", 1, defesa, fisico, passe, drible, velocidade, finalização)
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
                    a = Atacante(nome_jogador, numero_jogador, "ATA", 1, defesa, fisico, passe, drible, velocidade, finalização)
                    atacantes.append(a)
                    jogadores.append(a)
                    
                if esc == 3:
                    nome_jogador = input("Nome: ")
                    numero_jogador = input("Número da camisa: ")
        
        times_cadastrados += 1
        lista_times[times_cadastrados-1] = Time(nome_time, jogadores, goleiros, defensores, meio_campistas, atacantes)
        
    
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
                    if (jog.get_is_capitao == True):
                        print("> CAPITÃO <")
                    print('Nome:', jog.get_nome())
                    print('Número da camisa:', jog.get_numero())
                    print('Posição:', jog.get_pos())
                    print('Overall(média de habilidade):', jog.get_overall())
                    print("Partidas jogadas:", jog.get_partidas_jogadas())
                    print("Partidas vencidas:", jog.get_partidas_jogadas())
                    print("Gols marcados:", jog.get_partidas_jogadas())
                    print("Assistências feitas:", jog.get_partidas_jogadas())
                    
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
                    if (jog.get_is_capitao == True):
                        print("> CAPITÃO <")
                    print('Nome:', jog.get_nome())
                    print('Número da camisa:', jog.get_numero())
                    print('Posição:', jog.get_pos())
                    print('Overall(média de habilidade):', jog.get_overall())
                    print("Partidas jogadas:", jog.get_partidas_jogadas())
                    print("Partidas vencidas:", jog.get_partidas_jogadas())
                    print("Gols marcados:", jog.get_partidas_jogadas())
                    print("Assistências feitas:", jog.get_partidas_jogadas())
                    
                    flag = True
            if flag == False:
                print("Não existe um jogador cadastrado com esse nome!")
    
    # if op == 4:
    #     print("Bem vindo ao menu de exclusão de jogador:")
    #     flag=False
    #     for _ in lista_times:
    #         print(f"{lista_times.index(_)+1} - {_.get_nome_time()}")
    #     time_consulta = int(input("Digite em qual dos times você deseja excluir um jogador: "))
    #     name = input("Digite o nome do jogador que deseja excluir: ")
    #     flag=False
        
    #     for i, j in enumerate(lista_jogadores):
    #         if name == j.get_nome():
    #             lista_jogadores.pop(i)
    #             print("Exclusão realizada com sucesso!")
    #             flag=True
    #     if flag == False:
    #         print("Não existe um jogador cadastrado com esse nome!")
    
    if op == 5:
        for _ in lista_times:
            print(f"{lista_times.index(_)+1} - {_.get_nome_time()}")
        time_consultaGeral = int(input("Digite qual dos times você deseja consultar: "))     
        
        print(f"Nome do time: {lista_times[time_consultaGeral-1].get_nome_time}")
        for timeCon in lista_times[time_consultaGeral-1].lista_jogadores:
                print(f"{timeCon.get_pos()}: {timeCon.get_numero()} - {timeCon.get_nome()} - OVR: {timeCon.get_overall()}")
                
        
        
        
        
        
        
        
        
        
        '''pos = input("Posição do jogador(goleiro, defensor, meio, atacante): ").lower()
        
        if pos == "goleiro" :
            g = Goleiro(input("Nome: "), input("Número da camisa: "), "GOL", int(input("Habilidade do goleiro(1 a 10 estrelas): ")), 1, 1, 1, 1, 1, 1)
            lista_jogadores.append(g)
        
        if pos == "defensor" :
            d = Defensor(input("Nome: "), input("Número da camisa: "), "DEF", 1, int(input("Qualidade em defesa(1 a 10 estrelas): ")), int(input("Qualidade física(1 a 10 estrelas): ")), int(input("Qualidade em passe(1 a 10 estrelas): ")), int(input("Qualidade em drible(1 a 10 estrelas): ")), int(input("Qualidade em velocidade(1 a 10 estrelas): ")), int(input("Qualidade em finalização(1 a 10 estrelas): ")))
            lista_jogadores.append(d)
        
        if pos == "meio" :
            m = MeioCampista(input("Nome: "), input("Número da camisa: "), "MEI", 1, int(input("Qualidade em defesa(1 a 10 estrelas): ")), int(input("Qualidade física(1 a 10 estrelas): ")), int(input("Qualidade em passe(1 a 10 estrelas): ")), int(input("Qualidade em drible(1 a 10 estrelas): ")), int(input("Qualidade em velocidade(1 a 10 estrelas): ")), int(input("Qualidade em finalização(1 a 10 estrelas): ")))
            lista_jogadores.append(m)
        
        if pos == "atacante" :
            a = Atacante(input("Nome: "), input("Número da camisa: "), "ATA", 1, int(input("Qualidade em defesa(1 a 10 estrelas): ")), int(input("Qualidade física(1 a 10 estrelas): ")), int(input("Qualidade em passe(1 a 10 estrelas): ")), int(input("Qualidade em drible(1 a 10 estrelas): ")), int(input("Qualidade em velocidade(1 a 10 estrelas): ")), int(input("Qualidade em finalização(1 a 10 estrelas): ")))
            lista_jogadores.append(a)'''
            
        
                
                    
        
        
            
        

