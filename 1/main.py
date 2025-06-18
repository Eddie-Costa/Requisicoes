import os
import mysql.connector
from db import criarBD
from pathlib import Path

'''Conexao com DB mysql'''

conexao= mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '',
        database = 'REQ'
    )

class requisicoes:
    def __init__(self):
        self.op = 0
        arquivo = Path("Operadores.db")
        if arquivo.exists():
            print("DataBase já criado")
        else:    
            criarBD()
            print("database criado!!!")

    def ExecutarMenu(self):
        while self.op!=5:
            self.Menu()

            if self.op==1:
                self.RodarScriptDB(self.Cadastrar())
            elif self.op==2:
                print("Deletar")
            elif self.op==3:
                print("Imprimir")  
            elif self.op==4:
                print("Alterar")  

    def Menu(self):
        print("""
                                                    ====================================
                                                    |          MENU PRINCIPAL          |
                                                    ====================================
                                                    | 1 | Cadastrar                    |
                                                    | 2 | Excluir                      |
                                                    | 3 | Imprimir                     |
                                                    | 4 | Alterar                      |
                                                    | 5 | Sair                         |
                                                    ====================================
        """)
        self.op = int(input("Escolha uma opção:"))

    def Cadastrar(self):
        Chapa = int(input("Informe a Chapa do Colaborador: "))
        Nome = input("Digite o nome do Operador: ")
        ID = 0
        script = "INSERT INTO OPERADORES (ID, CHAPA, NOME) VALUES ("+ str(ID) +" ,"+ str(Chapa) +",'"+ Nome +"')"
        return script
    
    def RodarScriptDB(self, script):
        conexao = sqlite3.connect('Operadores.db')
        cursor = conexao.cursor()
        cursor.execute(script)


obj = requisicoes()
obj.ExecutarMenu()
