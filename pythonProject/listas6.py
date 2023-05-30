lista = []
print("Digite [-1] para sair")
while True:
    valor = int(input("Valor inteiro: "))
    if valor == -1:
        break
    lista.append(valor)
print("Menor número digitado foi: ", min(lista))
print("Maior número digitado foi: ", max(lista))