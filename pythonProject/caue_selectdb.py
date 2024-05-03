import mysql.connector
conexao = mysql.connector.connect(user= 'root', password='', host='127.0.0.1', database='db_loja_2')

print('Conexão:', conexao)
cursor = conexao.cursor()

sql = 'SELECT * FROM tb_produto'
cursor.execute(sql)
l_registros = cursor.fetchall()
print(l_registros)
print('- List of tuplas: ')
for l in l_registros:
    print(l)
cursor.close()
conexao.close()
print('\n Conexão fechada.')