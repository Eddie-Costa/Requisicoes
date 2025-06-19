import os
import mysql.connector
from pathlib import Path

'''Conexao com DB mysql'''
conexao= mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '',
        database = 'REQ'
    )
cursor = conexao.cursor()

class requisicoes:
    def __init__(self):
        self.op = 0

    """Método responsavél por executar o menu e fazer o desvio condicional dependendo da escolha do usuário"""
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
                self.RodarScriptDB(self.Alterar())  
                
    """Menu Principal do Sistema"""
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

    """Método com o Objetivo de realizar a funcao Insert"""
    def Cadastrar(self):
        Chapa = int(input("Informe a Chapa do Colaborador: "))
        Nome = input("Digite o nome do Operador: ")
        ID = 0
        script = "INSERT INTO OPERADORES (CHAPA, NOME) VALUES ("+ str(Chapa) +",'"+ Nome +"');"
        return script
    
    """Método com o Objetivo de realizar a funcao Update"""
    def Alterar(self):
        op=0
        script = ""
        while op!=3:
            id = int(input("Informe o ID do Colaborador que deseja alterar: "))
            op = int(input("Oque voce deseja alterar? 1-Chapa 2-Nome 3-Cancelar: "))
            match op:
                case 1:
                    Chapa = int(input("Informe a nova Chapa do Colaborador: "))
                    script = "UPDATE OPERADORES SET CHAPA = "+str(Chapa)+" WHERE ID_OPERADOR = "+ str(id)+" ;"
                case 2:    
                    Nome = input("Digite o novo nome do Operador: ")
                    script = "UPDATE OPERADORES SET NOME = '"+ Nome +"' WHERE ID_OPERADOR = "+ str(id)+" ;"     
                case 3: 
                    break
            return script    
        
    """Método com o Objetivo de Rodar os Códigos criado na variavel Script"""
    def RodarScriptDB(self, script):
        try:
            cursor.execute(script)
            conexao.commit()
            print("comando realizado")
        except:
            print("Comando nao sucedido")
        


obj = requisicoes()
obj.ExecutarMenu()
