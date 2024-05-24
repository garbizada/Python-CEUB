"""
- Instalar o package (pacote) mysql-connector-python:
Main Menu (botão, lado superior esquerdo): - Solução 1, no PyCharm
  File
    – settings
Project: NomeProjeto
    - Python Interpreter
Lado superior esquerdo 	(botão [+])
Available packages: ...
    botão: loaded list of packeges
        mysql-connector-python
    botão: Install package

----- ou

>pip install mysql-connector-python    - Solução 2, no terminal dos IDEs

"""

import mysql.connector

def create_database():
    conexao_db = mysql.connector.connect(user='root',  # user do servidor
                            password='',               # passwd='ceub123456'
                            host='127.0.0.1')          # host='localhost'
                            # database='')
    print('Conexão db:', conexao_db)  # Teste
    cursor_db = conexao_db.cursor()   # Cria cursor para executar comandos SQL
    sql = "CREATE DATABASE if not exists db_cadastro"  # O nome do database
    cursor_db.execute(sql)            # Executa o comando sql
    cursor_db.close()
    conexao_db.close()
    print('\nConexão db fechada.')

def create_connection():
    con = mysql.connector.connect(user='root',      # user do servidor
                            password='',            # passwd='ceub123456'
                            host='127.0.0.1',       # host='localhost'
                            database='db_cadastro')  # Nome do schema criado
    print('Conexão:', con)                          # Testando
    return con

def create_table():
    sql_cargo = """ CREATE TABLE IF NOT EXISTS td_cargo( 
    idt int NOT NULL AUTO_INCREMENT,  # Cria automaticamente a chava primária
    nome varchar(45) UNIQUE NOT NULL, # Valores sem repetição
    PRIMARY KEY (idt)                 # Define a chave primária
    )   """
    cursor.execute(sql_cargo)         # Primeiro, crie a tabela td_cargo
    sql_empregado = """ CREATE TABLE IF NOT EXISTS tb_empregado(
    idt int NOT NULL AUTO_INCREMENT,  # Cria automaticamente a chava primária
    nome varchar(45) NOT NULL,        # NOT NULL para valor obrigatório
    dta_nascimento date NULL,         # NULL para valor opcional
    genero enum('M', 'F') NOT NULL,   # Aceita 'M', 'm, 'F' ou 'f' 
    cod_cargo int NOT NULL,           # NOT NULL para valor obrigatório
    PRIMARY KEY (idt),                # Define a chave primária
    FOREIGN KEY(cod_cargo) REFERENCES td_cargo(idt)  # Define chave estrangeira
    )   """
    cursor.execute(sql_empregado)     # Depois, crie a tabela tb_empregado

def insert_cargo():                   # Solução 1
    a_nome = input('Nome do cargo: ')  # Insere primeiro na tabela domínio
    sql = f"""  insert into td_cargo (nome)
                values('{a_nome}')              """
    cursor.execute(sql)
    conexao.commit()                  # Confirma a alteração no database

def insert_empregado():                       # Solução 1
    a_nome = input('Nome empregado: ')
    a_dta_nascimento = input("Data nascimento: aaaa-mm-dd: ")
    a_genero = input("Gênero [M] ou [F]: ")
    a_cod_cargo = int(input('FK - Código Cargo: '))
    sql= f"""insert into tb_empregado (nome, dta_nascimento, genero, cod_cargo)
     values('{a_nome}', '{a_dta_nascimento}', '{a_genero}', {a_cod_cargo}) """
    cursor.execute(sql)
    conexao.commit()                # Confirma a alteração no database

def select_all_emp():
    sql = ' select * from tb_empregado '
    cursor.execute(sql)
    registros = cursor.fetchall()   # registros é uma lista de tuplas
    print('- Tuplas:')              # Solução 2:
    for record in registros:        # Mostra os registros na vertical
        print(record)

def select_innerjoin():
    sql= f"""select t1.nome_empregado, t1.DT_nasc, t2.nome 
             from tb_empregado t1 inner join tb_cargo as t2
              where t1.cod_cargo = t2.idt """
    cursor.execute(sql)
    registros = cursor.fetchall()
    print('- Tuplas: ')
    for record in registros:
        print(record)


def close_connection():
    cursor.close()
    conexao.close()
    print('\nConexão fechada.')

if __name__ == '__main__':
   #create_database()               # Chama a função create_database
    conexao = create_connection()   # Chama a função
    cursor = conexao.cursor()
   # create_table()                  # Chama a função
   # insert_cargo()                  # Chama a função
   # insert_empregado()              # Chama a função
   # select_all_emp()

    select_innerjoin()

    close_connection()            # Chama a função close_connection

