print("Digite [-1] para terminar o programa")
while True:
    tabuada = int(input("Digite o numero da tabuada: "))
    if tabuada== -1:
        break
    print('Tabuada de multiplicaçao de ', tabuada)
    for i in range(1, 11):
        print(f"{i:2} x {tabuada} = {i * tabuada:2}")
