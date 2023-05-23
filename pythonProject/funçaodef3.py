#def calcula_dobro():
#    x= int(input("Digite o valor do primeiro número: "))
 #   print("Calcula dobro:", x*2)

#if __name__ == '__main__':
#    calcula_dobro()

    #OPÇAO 2

def calcula_dobro(p_valor):
    dobro= p_valor * 2
    return dobro

if __name__ == '__main__':
    valor= int(input("Valor: "))
    valor_retorno = calcula_dobro(valor)
    print("Valor retornado pela função: ", valor_retorno)
