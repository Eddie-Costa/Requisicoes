import sqlite3

def criarBD():
    conexao = sqlite3.connect('Operadores.db')
    cursor = conexao.cursor()

    script = 'CREATE TABLE OPERADORES (ID INT AUTO INCREMENT, CHAPA INT,NOME TEXT, PRIMARY KEY(ID));'
    cursor.execute(script)