l_valor = []
print("Digite o [0] para sair")
while True:
    valor = int(input("Valor inteiro: "))
    if valor == 0:
        break
    l_valor.append(valor)
print(" O menor valor é: ", min(l_valor))
print(" A quantidade de valores digitados é: ", len(l_valor))
