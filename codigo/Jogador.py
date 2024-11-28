class Jogador:
    def __init__(self, nome_jogador, numero_jogador, pos_jogador, habgoleiro, defesa, fisico, passe, drible, velocidade, finalizacao):
        partidas_jogadas = 0
        partidas_vencidas = 0
        gols_marcadados = 0
        assistencias_feitas = 0
        is_capitao = False

        self.partidas_jogadas = partidas_jogadas
        self.partidas_vencidas = partidas_vencidas
        self.gols_marcados = gols_marcadados
        self.assistencias_feitas = assistencias_feitas
        self.is_capitao = is_capitao
        self.pos_jogador = pos_jogador
        self.nome_jogador = nome_jogador
        self.numero_jogador = numero_jogador
        self.habgoleiro = habgoleiro
        self.defesa = defesa
        self.fisico = fisico
        self.passe = passe
        self.drible = drible
        self.velocidade = velocidade
        self.finalizacao = finalizacao

    def get_partidas_jogadas(self):
        return self.partidas_jogadas
    
    def get_partidas_vencidas(self):
        return self.partidas_vencidas

    def get_gols_marcados(self):
        return self.gols_marcados
    
    def get_assistencias_feitas(self):
        return self.assistencias_feitas
    
    def get_is_capitao(self):
        return self.is_capitao
    
    def get_overall(self):
        return self.overall
  
    def get_nome(self):
        return self.nome_jogador
    
    def get_numero(self):
        return self.numero_jogador
  
    def get_pos(self):
        return self.pos_jogador
    
    def set_is_capitao(self):
        self.is_capitao = True

    def set_num(self, num_novo):
        self.numero_jogador = num_novo