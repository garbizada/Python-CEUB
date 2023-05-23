def valor_absoluto(x):
    if x < 0:
       valors = -x
    else:
        valors = x
    return valors

if __name__ == '__main__':
    x= int(input("Digite o número: "))
    print("Valor: ", valor_absoluto(x))