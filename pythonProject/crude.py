l_nomes = [] #CRUDE C=CREATE, R=READ, U=UPDATE, D=DELETE, E=EXIT
def menu():
  print("[c]- CREATE")
  print("[r]- READ")
  print("[u]- UPDATE")
  print("[d]- DELETE")
  print("[e]- EXIT")
  opcao = input("Opção : ")
  return opcao
def create():
  nome = input("Nome: ")
  l_nomes.append(nome)

def read():
  print(l_nomes)


if __name__ == '__main__':
  while True:
    op = menu()
    if op == 'c':
      create()

    elif op == 'r':
      read()

    elif op == 'u':
      print('update()')

    elif op == 'd':
      print('delete()')
    else:
      break