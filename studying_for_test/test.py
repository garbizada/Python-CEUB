#PROGRAMA QUE LE VARIOS NUMEROS DIGITADOS PELO USUARIO
#É MOSTRA NA TELA DE SAIDA A QUANTIDADE DE NUMEROS DIGITADOS 

#l_numeros = []    
#print("Digite [-1] para sair")
#while True:
#  numero = int(input("Digite um número:"))
#  if numero == -1:
#    break
#  l_numeros.append(numero)
#print("Quantidade de números: ", len(l_numeros))
#print("Soma dos números digitados: ", sum(l_numeros))
#print(l_numero)



#PROGRAMA QUE CALCULA A MÉDIA ARITMETICA DE UMA TURMA 

#l_notas = []
#print("Digite o [-1] para sair")

#while True:
#  nota = float(input("Digite uma nota:"))
#  if nota == -1:
#    break
#  l_notas.append(nota)
#media =  sum(l_notas)/ len(l_notas)
#print("Média da turma : ", media)
#print("Quantidade de alunos: ", len(l_notas))


#PROGRAMA PARA CALCULAR MEDIA DOS NUMEROS PARES

#num_par = []
#num_impar = []
#print("Digite [0] para sair")
#while True:
 # valor = int(input("Digite um valor: "))
 # if valor == 0:
 #   break
 # if valor % 2 == 0:
  #  num_par.append(valor)
 # else:
  #   num_impar.append(valor)
#qtd_par = len(num_par)
#if qtd_par > 0:
#  media_par = sum(num_par) / len(num_par)
#   print("Média dos números pares é : ", media_par)

#else:
#  print("Não tem número par!")

#qtd_impar = len(num_impar)
#if qtd_impar > 0:
#  media_imp = sum(num_impar) / len(num_impar)
#  print("Média dos números impares: ", media_imp)
#else: 
 # print("Não tem número impar!")



#       EXERCICIOS USANDO DEF E FOR


#sequencia = []
#for i in range(11):
#  sequencia.append(i * 2)
#print("Sequência do dobro dos números naturais até 10: ")
#print(sequencia)
#print("Soma da sequência: ", sum(sequencia))

#numeros = []
#for i in range(10):
#  numero = int(input("DIgite um número: "))
#  numeros.append(numero)
#produto = 1
#for numero in numeros:
#  produto *= numero
#print("O produto dos números é: ", produto)



#       EXERCICIO DE DEF

#def mns_numero(mensagem, numero):
#  print(mensagem, numero)

#if __name__ == "__main__":
#  mns_numero("OLA MUNDO", 17)

#--------------------------------


#def multiplicar_valores(a,b):
#  return a * b


#if __name__ == "__main__":
#  print(multiplicar_valores(7, 7))

#---------------------------------

def retorna_soma(v1,v2):
  soma = v1 + v2
  return soma

if __name__ == "__main__":
  valor1 = int(input("Primeiro valor: "))
  valor2 = int(input("Segundo valor: "))
  v_retorno = retorna_soma(valor1, valor2)
  print("Soma = ", v_retorno)






