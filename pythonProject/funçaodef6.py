def maximo(num1, num2):
    if num1 >= num2:
        maior = num1
    else:
        maior = num2
    return maior

if __name__ == '__main__':
    num1= int(input("Primeiro valor:"))
    num2= int(input("Segundo valor:"))
    v_maximo= maximo(num1, num2)
    print("\nMaior valor:", v_maximo)