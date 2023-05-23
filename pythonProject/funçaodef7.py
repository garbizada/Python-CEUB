def soma(valor1, valor2):
    somar= valor1 + valor2
    return somar
def subtrai(valor1, valor2):
    subtrair= valor1 - valor2
    return subtrair

if __name__ == '__main__':
    valor1 = float(input("Digite o primeiro valor: "))
    valor2 = float(input("Digite o segundo valor: "))
    v_soma = soma(valor1, valor2)
    v_subtrai = subtrai(valor1, valor2)
    print("\nO valor retornado da soma é: ",v_soma)
    print("\nO valor retornado da subtração é: ", v_subtrai)
