def retorna_soma(valor1, valor2):
    soma= valor1 + valor2
    return soma

if __name__ == '__main__':
    valor1= float(input("PRimeiro valor: "))
    valor2= float(input("Segundo valor: "))
    v_retorna = retorna_soma(valor1, valor2)
    print("A soma dos dois numeros é igual a: ",v_retorna)

