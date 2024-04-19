#Cauê Justen Garbi

class Produto(object):
  def __init__(self, nome, preco):
    self.nome = nome
    self.preco = preco

  

  def desconto(self,por_desconto):
    desconto = self.preco * por_desconto
    return self.preco - desconto



class Eletronico(Produto):
  def __init__(self, nome, preco, voltagem = 220):
    super().__init__(nome,preco)
    self.voltagem = voltagem

  def mostra_dados(self):
    return "O nome do eletronico é: " , self.nome , ", O valor dele é: ", self.preco , ", e a voltagem dele e: " , self.voltagem ,  "!"




class Vestuario(Produto):
  def __init__(self, nome,preco, tamanho = "m"):
    super().__init__(nome, preco)
    self.tamanho = tamanho

  def set_tamanho(self,novo_tamanho): 
    if novo_tamanho in ["p", "m", "g", "gg"]:
      self.tamanho = novo_tamanho
      print("Você escolheu o tamanho ", novo_tamanho , "!")
    else:
      print("Não existe esse tipo de tamanho")



if __name__ == "__main__":

  geladeira = Eletronico("Geladeira Phillips", 1500, 330)
  blusa = Vestuario("Blusa polo",150)

  
  
  geladeira.desconto(0.05)
  print(geladeira.mostra_dados())

  blusa.set_tamanho("ggg")
  blusa.set_tamanho("gg")

    