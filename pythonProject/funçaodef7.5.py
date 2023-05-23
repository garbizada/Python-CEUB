def soma(x, y):
    return x + y
def subtrai(x, y):
    subtrair= x - y
    return subtrair

if __name__ == '__main__':
   v1= int(input("Digite o Primeiro valor: "))
   v2= int(input("Digite o segundo valor: "))
   opcao= int(input("[1]para realizar Soma\n[2]para realizar subtração\n Opção: "))
   if opcao == 1:
       print("Soma: ", soma(v1,v2))
   else:
       print("Subtração: ", subtrai(v1, v2))
