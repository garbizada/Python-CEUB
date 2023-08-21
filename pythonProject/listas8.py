import statistics
l_numpar = []
print("Digite 0 para sair")
while True :
    valor = int(input("Digite o valor: "))
    if valor == 0 :
        break
    if valor % 2 == 0 :
        l_numpar.append(valor)
if len(l_numpar) > 0: 
    media_par = statistics.mean(l_numpar)
    print(media_par)
else:
    print("Não foi digitado número par")
