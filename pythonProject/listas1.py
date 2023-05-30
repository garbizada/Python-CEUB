l_numeros = []
print('Digite o [-1] para sair')
while True: 
    numero= int(input("Digite um numero: "))
    if numero== -1:
        break
    l_numeros.append(numero)
print('Quantidade de numeros: ', len(l_numeros))
print('Soma dos números: ', sum(l_numeros))
print('Os números digitados foram:\n ', l_numeros)