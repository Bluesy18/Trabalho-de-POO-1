from decimal import Decimal, ROUND_HALF_UP

class Time:
    def __init__(self, nome_time, lista_jogadores, lista_goleiros, lista_defensores, lista_meio_campistas, lista_atacantes):

        # Define atributo perdedor
        perdedor = False
        self.perdedor = perdedor

        # Define atributos recebidos
        self.nome_time = nome_time
        self.lista_jogadores = lista_jogadores
        self.lista_goleiros = lista_goleiros
        self.lista_defensores = lista_defensores
        self.lista_meio_campistas = lista_meio_campistas
        self.lista_atacantes = lista_atacantes

        # Define finalizações
        finalizacoes = []
        for fin in self.lista_jogadores:
            finalizacoes.append(fin.finalizacao)

        self.finalizacoes = finalizacoes

        # Define passes
        passes = []
        for pas in self.lista_jogadores:
            passes.append(pas.passe)

        self.passes = passes

        # Calcula índice defensivo
        indice_defensivo = lista_goleiros[0].get_overall()

        for defe in self.lista_defensores:
            indice_defensivo += defe.get_overall()

        meias = 0
        for meia in self.lista_meio_campistas:
            meias += meia.get_overall()

        meias = meias/len(self.lista_meio_campistas)

        indice_defensivo = (indice_defensivo/(len(self.lista_defensores)+1))*2
        indice_defensivo = (indice_defensivo+meias)/3

        self.indice_defensivo = Decimal(indice_defensivo).quantize(0, ROUND_HALF_UP)

        # Calcula índice ofensivo
        indice_ofensivo = 0

        for ata in self.lista_atacantes:
            indice_ofensivo += ata.get_overall()
        
        indice_ofensivo = (indice_ofensivo/len(self.lista_atacantes))*2
        indice_ofensivo = (indice_ofensivo+meias)/3

        self.indidice_ofensivo = Decimal(indice_ofensivo).quantize(0, ROUND_HALF_UP)

        # Calcula overall
        overall_time = 0
        for i in range(11):
            overall_time += self.lista_jogadores[i].overall

        self.overall_time = overall_time

    # Métodos
    def get_overall_time(self):
        return self.overall_time
        
    def get_nome_time(self):
        return self.nome_time
    
    def get_jogadores(self):
        return self.lista_jogadores
    
    def get_indice_defensivo(self):
        return self.indice_defensivo
    
    def get_indice_ofensivo(self):
        return self.indidice_ofensivo
    
    def get_finalizacoes(self):
        return self.finalizacoes
    
    def get_passes(self):
        return self.passes
    
    def get_perdedor(self):
        return self.perdedor

    def set_perdedor(self):
        self.perdedor = True

    def set_perdedor_false(self):
        self.perdedor = False

    def set_indice_ofensivo_original(self):
        meias = 0
        for meia in self.lista_meio_campistas:
            meias += meia.get_overall()

        meias = meias/len(self.lista_meio_campistas)

        indice_ofensivo = 0

        for ata in self.lista_atacantes:
            indice_ofensivo += ata.get_overall()
        
        indice_ofensivo = (indice_ofensivo/len(self.lista_atacantes))*2
        indice_ofensivo = (indice_ofensivo+meias)/3

        self.indidice_ofensivo = Decimal(indice_ofensivo).quantize(0, ROUND_HALF_UP)

    def set_indice_ofensivo(self, aleatorio):
        io = float(self.indidice_ofensivo)*aleatorio
        self.indidice_ofensivo = Decimal(io).quantize(0, ROUND_HALF_UP)
    
