import mysql.connector

# Conectando ao banco de dados
conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='1102004Caue!',
    database="db_escola"
)
cursor = conexao.cursor()

#1. Criando base de dados
def criar_db():
    cursor.execute("""CREATE DATABASE db_escola """)
    print("Base de dados criada com sucesso!")

# 2. Criando a tabela
def criar_tabela():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Estudante (
        Id INT AUTO_INCREMENT PRIMARY KEY,
        Nome VARCHAR(100) UNIQUE NOT NULL,
        Idade INT NOT NULL,
        Altura DECIMAL(5,2),
        Peso DECIMAL(5,2),
        DataNascimento DATE
    )
    """)
    conexao.commit()
    print("Tabela criada com sucesso.")

# 3. Inserindo dados na tabela
def inserir_dados():
    # Inserindo um registro por vez
    cursor.execute("""
    INSERT INTO Estudante (Nome, Idade, Altura, Peso, DataNascimento)
    VALUES ('Fulano', 16, 1.75, 70.5, '2004-05-20')
    """)
    conexao.commit()
    print("Registro inserido com sucesso.")

# 4. Consultando dados da tabela
def consultar_dados():
    cursor.execute("SELECT * FROM Estudante")
    dados = cursor.fetchall()
    if dados:
        # Exibindo os registros na vertical
        print("Registros na vertical:")
        for registro in dados:
            print(registro)

        # Exibindo os registros na horizontal
        print("\nRegistros na horizontal:")
        for registro in dados:
            print(f"Id: {registro[0]}, Nome: {registro[1]}, Idade: {registro[2]}, Altura: {registro[3]}, Peso: {registro[4]}, Data de Nascimento: {registro[5]}")
    else:
        print("Tabela vazia.")

# Chamando as funções
criar_db()
criar_tabela()
inserir_dados()
consultar_dados()

# Fechando conexão
conexao.close()
