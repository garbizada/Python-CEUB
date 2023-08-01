import statistics
l_altura = []
l_genero = []
print("Digite 0 para sair")
while True :
    altura = float(input("Digite a altura: "))
    if altura == 0: 
        break
    l_altura.append(altura)
    genero = input("[m] para Masculino \n[f] para Feminino: ")
    l_genero.append(genero)

print("Maior altura do grupo : ", max(l_altura))
print("Menor altura do grupo : ", min(l_altura))
print("Masc : ", l_genero.count("m"))
print("Fem : ", l_genero.count("f"))
media = statistics.mean(l_altura)
print("A média de altura do grupo é : ", media)
    