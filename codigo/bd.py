import sqlite3 

class BD:
    def __init__(self):
        self.cx = sqlite3.connect("geral.db")
        self.cursor = self.cx.cursor()


    def criar_banco(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS times (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_time TEXT NOT NULL                           
        )
        ''')

        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS jogadores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_jogador TEXT NOT NULL,
            numero INTEGER,
            posicao TEXT NOT NULL,
            habgoleiro INTEGER,
            defesa INTEGER,
            fisico INTEGER,
            passe INTEGER,         
            drible INTEGER,
            velocidade INTEGER,
            finalizacao INTEGER,
            time_id INTEGER,
            FOREIGN KEY (time_id) REFERENCES times (id)                        
        )
        ''')

        self.cx.commit()
        print("Tabelas criadas")

    def add_time(self,nome):
        self.cursor.execute("INSERT INTO times (nome_time) VALUES (?)", (nome,))
        self.cx.commit()
        print(f"Certo. Seu time será chamado de {nome} e jogará na formação 4-3-3.")
        self.cursor.execute("SELECT id FROM times WHERE nome_time = ?", (nome,))
        time = self.cursor.fetchone()
        if time:
            return time[0]
        else:
            return None


    '''def buscar_id_time(nome):
        cursor.execute("SELECT id FROM times WHERE nome_time = ?", (nome,))
        time = cursor.fetchone()
        if time:
            return time[0]
        else:
            return None'''



    def add_jogador(self,nome_jogador, numero, posicao, habgoleiro, defesa, fisico, passe, drible, velocidade, finalizacao,id_time):
        self.cursor.execute('''
        INSERT INTO jogadores 
        (nome_jogador, numero, posicao, habgoleiro, defesa, fisico, passe, drible, velocidade, finalizacao,time_id)
        VALUES (?,?,?,?,?,?,?,?,?,?,?) 
        ''', (nome_jogador, numero, posicao, habgoleiro, defesa, fisico, passe, drible, velocidade, finalizacao,id_time))
        self.cx.commit()

    def atualizar_camisa_do_jogador(self,nome_jogador,num):
        self.cursor.execute('''
        UPDATE jogadores 
        SET numero = ?
        WHERE nome = ?
        ''', (num, nome_jogador))
        self.cx.commit()
        print(f"Camisa do '{nome_jogador}' atualizada!")

    def listar_times(self):
        self.cursor.execute("SELECT nome_time FROM times")
        times = self.cursor.fetchall()
        print(*times)

    








    
    