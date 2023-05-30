l_numpar = []
l_numimpar = []
print("Digite o [-1] para sair")
while True :
    vl = int(input("Valor: "))
    if vl == -1:
        break
    if vl % 2 == 0:
        l_numpar.append(vl)
    else:
        l_numimpar.append(vl)

if len(l_numpar) > 0:
    media_par = sum(l_numpar) / len(l_numpar)
    print("Média dos pares: ", media_par)
else:
    print("Não tem número par")

if len(l_numimpar) > 0:
    media_impar = sum(l_numimpar) / len(l_numimpar)
    print("Média dos pares: ", media_impar)
else:
    print("Não tem número impar.")