import sqlite3 
cx = sqlite3.connect("geral.db")
cursor = cx.cursor()


def criar_banco():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS times (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_time TEXT NOT NULL                           
    )
    ''')

    cursor.execute('''
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

    cx.commit()
    print("Tabelas criadas")

def add_time(nome):
    cursor.execute("INSERT INTO times (nome_time) VALUES (?)", (nome,))
    cx.commit()
    print(f"Certo. Seu time será chamado de {nome} e jogará na formação 4-3-3.")
    cursor.execute("SELECT id FROM times WHERE nome_time = ?", (nome,))
    time = cursor.fetchone()
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



def add_jogador(nome_jogador, numero, posicao, habgoleiro, defesa, fisico, passe, drible, velocidade, finalizacao,id_time):
    cursor.execute('''
    INSERT INTO jogadores 
    (nome_jogador, numero, posicao, habgoleiro, defesa, fisico, passe, drible, velocidade, finalizacao,id_time)
    VALUES (?,?,?,?,?,?,?,?,?,?,?) 
    ''', (nome_jogador, numero, posicao, habgoleiro, defesa, fisico, passe, drible, velocidade, finalizacao,id_time))
    cx.commit()
    


    








    
    