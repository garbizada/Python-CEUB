lista = []
print("Digite 0 para sair")
while True :
    valor = int(input("Digite o valor: "))
    if valor == 0 :
        break
    lista.append(valor)
print("Menor número digitado foi : ", min(lista))
print("A quantidade de números digitados: ", len(lista))
print("A soma dos valores digitados é: ", sum(lista))