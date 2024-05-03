import mysql.connector
conexao = mysql.connector.connect(user= 'root', password='', host='127.0.0.1', database='db_loja_2')

print('Conexão:', conexao)
cursor = conexao.cursor()
sql = "CREATE TABLE tb_produto(ID INT NOT NULL AUTO_INCREMENT, nome VARCHAR(80) NOT NULL UNIQUE, preco DECIMAL(9,2) NOT NULL, dta_validade DATE NULL, PRIMARY KEY(ID))"
cursor.execute(sql)
cursor.close()
conexao.close()
print('\n Conexão fechada.')