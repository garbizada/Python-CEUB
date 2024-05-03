import mysql.connector
conexao = mysql.connector.connect(user= 'root', password='', host='127.0.0.1', database='db_loja_2')

print('Conexão:', conexao)
cursor = conexao.cursor()
var_1 = input('Nome: ')
var_2 = float(input('Preço: '))
var_3 = input('Data de Validade: aaaa-mm-dd:')
sql = f'''insert into tb_produto( nome , preco, dta_validade)
values ('{var_1}', {var_2} , '{var_3}')'''
cursor.execute(sql)
conexao.commit()
cursor.close()
conexao.close()
print('\n Conexão fechada.')