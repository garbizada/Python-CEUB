l_valor = []
print("Digite o [0] para sair")
while True:
    valor = int(input("Valor inteiro: "))
    if valor == 0:
        break
    l_valor.append(valor)
if len(l_valor) == 0:
    print("Não foi digitado número!")
else:
    print(" O menor valor é: ", min(l_valor))
    print(" A quantidade de valores digitados é: ", len(l_valor))
    print(" A soma dos valores digitados: ", sum(l_valor))
