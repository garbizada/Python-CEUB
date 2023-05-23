def retorna_soma(valor1, valor2):
    soma= valor1 + valor2
    return soma

def retorna_soma2(valor1, valor2):
    return valor1 + valor2




if __name__ == '__main__':
    valor1 = float(input("Digite o primeiro valor: "))
    valor2 = float(input("Digite o segundo valor: "))
    v_retorna = retorna_soma2(valor1, valor2)
    print("Soma = ", v_retorna)



