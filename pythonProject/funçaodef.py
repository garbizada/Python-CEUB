def soma():                             #DEFINE A FUNÇAO SOMA#
    x= float(input("Digite o valor de x: "))
    y= float(input("Digite o valor de y: "))
    print("soma :", x + y)


def bemvindo():                         #DEFINE A FUNÇAO BEMVINDO#
    print("Bem-vindo ao def do Python")

def bemvindo2(msg):
    print(msg)

if __name__ == '__main__':             #CHAMA A FUNÇAO MAIN
    print("oi")
    bemvindo()
    print("oi denovo")
    bemvindo2('OLA')
    var =input("Digite uma mensagem: ")
    bemvindo2(var)


