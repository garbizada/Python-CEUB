class jogador_volei(object):
  def __init__(self, altura,posicao,salario = 2000):
    self.altura = altura
    self.posicao = posicao
    self.salario = salario

  def get_altura(self):
    print( self.altura)  

  def get_posicao(self):
    print( self.posicao)

  def get_salario(self):
    print( self.salario)
  

  def set_nova_altura(self):
    nova_altura = input("Digite a nova altura: ")
    self.altura = nova_altura

  def set_nova_posicao(self):
    nova_posicao = input('Digite a posicao que o jogador joga: ')
    self.posicao = nova_posicao
  
  def set_novo_salario(self):
    novo_salario = int(input("Digite o novo salario do jogador: "))
    if novo_salario > 0 :
      self.salario = novo_salario
    else:
      print("Nao existe salarios negativos")

  
  def marcar_pontos(self, pontos):
    aumento_por_ponto = 50

    aumento_salario = pontos * aumento_por_ponto

    self.salario += aumento_salario
    print("O novo salario apos o bonus e: ", self.salario)

  
    


class bola_de_volei(object):
  def __init__(self, peso, marca, valor):
    self.peso = peso
    self.marca = marca
    self.valor = valor

  def get_peso(self):
    print(self.peso)
  
  def get_marca(self):
    print( self.marca)
  
  def get_valor(self):
    print(self.valor)

  def set_novo_peso(self):
    novo_peso = input("Digite o peso da bola: ")
    self.peso = novo_peso
  
  def set_nova_marca(self):
    nova_marca = input("Digite a marca da bola: ")
    self.marca = nova_marca

  def set_valor(self):
    novo_valor = int(input("Digite o valor da bola: "))
    self.valor = novo_valor



  


class tipo_volei(object):
  def __init__(self,lugar, categoria,campeonato):
    self.lugar = lugar  
    self.categoria = categoria
    self.campeonato = campeonato

  def get_lugar(self):
    print( self.lugar)
  
  def get_categoria(self):
    print( self.categoria)

  def get_campeonato(self): 
    print( self.campeonato)

  def set_lugar(self):
    novo_lugar = input("Digite o lugar que vai ser jogado: ")
    self.lugar = novo_lugar

  def set_categoria(self):
    nova_categoria = input("Digite a categoria do jogo: ")
    self.categoria = nova_categoria

  def set_campeonato(self):
    novo_campeonato = input("Digite o campeonato que vai ser jogado: ")
    self.campeonato = novo_campeonato
  


if __name__ == '__main__':

  j1 = jogador_volei(1.94, 'ponteiro', 5000)

  #j1.get_altura()
  #j1.get_posicao()
  #j1.get_salario()



  #j1.set_nova_altura()
  #j1.set_nova_posicao()
  #j1.set_novo_salario()
  #j1.marcar_pontos(40)
  #print(j1.__dict__)
  

  b1 = bola_de_volei('300g','mikasa', 700)

  #b1.get_marca()
  #b1.get_peso()
  #b1.get_valor()

  #b1.set_nova_marca()
  #b1.set_novo_peso()
  #b1.set_valor()
  #print(b1.__dict__)

  
  b2 = bola_de_volei('430g','molden', 1200)

  #b2.get_marca()
  #b2.get_peso()
  #b2.get_valor()

  #b2.set_nova_marca()
  #b2.set_novo_peso()
  #b2.set_valor()
  #print(b2.__dict__)

  t1 = tipo_volei('areia', 'SUB-21', 'Mundial')

  #t1.get_campeonato()
  #t1.get_categoria()
  #t1.get_lugar()

  #t1.set_campeonato()
  #t1.set_categoria()
  #t1.set_lugar()
  #print(t1.__dict__)

  t2 = tipo_volei('quadra', 'Profissional', 'Olimpiadas')

  #t2.get_campeonato()
  #t2.get_categoria()
  #t2.get_lugar()

  #t2.set_campeonato()
  #t2.set_categoria()
  #t2.set_lugar()
  #print(t2.__dict__)

