import statistics
lista = []
print ('Digite [0] para sair')
while True:
  valor = int(input("Valor: "))
  if valor == 0 :
    break
    lista.append(valor)
print("Valores da lista: \n ", lista)
print("Quantidade de elementos da lista: ", len(lista)) #Quantidade de elementos armazenados na lista;
print("Soma dos elementos da lista: ", sum(lista)) #Soma dos elementos da lista
print("Maior valor; ", max(lista)) #maior valor da lista
print("Menor valor: ", min(lista)) #menor valor da lista
pesquisa = int(input("Valor a procura: ")) #Leia um valor e verificar se ele está na lista;
if pesquisa in lista:   #Leia um valor e verificar se ele está na lista;
  print("Valor encontrado. \n")   #Leia um valor e verificar se ele está na lista;
  posicao = lista.index(pesquisa)   #mostre também a posição (índice) do valor encontrado;
  print("Posição do número na lista: ", posicao)  #mostre também a posição (índice) do valor encontrado;

else: #Leia um valor e verificar se ele está na lista;
  print("Valor não encontrado\n") #Leia um valor e verificar se ele está na lista;

print("Antes do sort(): \n", lista) #Mostre a lista na ordem crescente;
lista.sort() #Mostre a lista na ordem crescente;
print("Depois do sort(): \n ", lista) #Mostre a lista na ordem crescente;

lista.insert(1, 33) #Insira (acrescente) o valor 33 na posição (índice) 1 da lista;
print("Lista apos inserido números: ",lista) #Insira (acrescente) o valor 33 na posição (índice) 1 da lista;

lista.sort(reverse=True) # Mostre a lista na ordem decrescente;
print("Lista na ordem decrescente:",lista) # Mostre a lista na ordem decrescente;


media = statistics.mean(lista) #Calcule e mostre a média dos valores da lista;
print("A média dos números na lista é:", "%.3f" % media) #Calcule e mostre a média dos valores da lista;


#TEM QUE FAZER l- Porcentagem dos números maiores que dez da lista.
