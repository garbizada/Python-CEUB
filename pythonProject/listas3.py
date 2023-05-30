l_numpar = []
print('Digite o [0] para sair')
while True:
    numero = float(input("Digite um número: "))
    if numero == 0:
        break
    if numero % 2 == 0:
        l_numpar.append(numero)
if len(l_numpar) != 0:
    media = sum(l_numpar) / len(l_numpar)
    print("A média dos numeros digitados é: ", media)
else:
    print('Não e possivel dividir por zero')



