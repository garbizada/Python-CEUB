def recebinte(valor1):
    print(" Valor recebido: ", valor1)

def recebinte2(valor2, valor3):
    print(" Primeiro valor recebido: ", valor2)
    print(" Segundo valor recebido: ", valor3)

if __name__ == '__main__':
    print(" ------Mensagem Anteporior-----")
    recebinte(5)
    recebinte(0.66)
    recebinte(-50)
    print("---------Mensagem Posperior-------")
    recebinte(5)
    recebinte2(5, 10)

