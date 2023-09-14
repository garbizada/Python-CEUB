class Funko(object):
  qtd_produto = 0
  produtos = []

  @classmethod
  def get_qtd_produto(cls):
      return cls.qtd_produto

  def __init__(self, personagem = 0, cor= 0, preco= 0):
    self.personagem = personagem
    self.cor = cor
    self.preco = preco
    type(self).qtd_produto += 1
    Funko.produtos.append(self)

  @classmethod
  def mostra_produtos(cls):
      print("Nome dos funkos: ")
      for objeto in cls.produtos:
        print(f"- {objeto.get_personagem()}")
  
  def inf_de_venda(self):
      print("Nome: ",self.personagem," \nCor do Funko: ", self.cor,"\nPreço: ",self.preco)


  def __str__(self):
        s = self.personagem + " - " + self.cor + " - " + str(self.preco)
        return s 


  
  def get_personagem(self):
        return self.personagem
    
  def set_personagem(self, novo_nome):
        if isinstance(novo_nome, str):
            self.personagem = novo_nome
        else: 
            print("Erro: Nome não contém número")
  
  def get_cor(self):
        return self.cor
    
  def set_cor(self, nova_cor):
        if isinstance(nova_cor, str):
            self.cor = nova_cor
        else: 
            print("Erro: Nome não contém número")

  def get_preco(self):
        return self.preco
    
  def set_preco(self, novo_preco):
        if isinstance(novo_preco, int):
            self.preco = novo_preco
        else: 
            print("Erro: Número não contém letra")

  def mais_caro(self,outro_produto):
        if self.preco > outro_produto.preco:
            return f"O produto {self.personagem} é mais caro"
        elif self.preco < outro_produto.preco:
            return f"O produto {outro_produto.personagem} é mais caro"
        else:
            return "Ambos produtos tem o mesmo preço"


if __name__ == "__main__":

  funko1 = Funko("Homem aranha", "vermelho", 600)
  funko2 = Funko("Baby Yoda",0, 150)
  funko3 = Funko("Darth Vader")


  print("A quantidade total de produtos é: ",Funko.get_qtd_produto())
  Funko.mostra_produtos()

  funko1.inf_de_venda()
  funko1.__str__()
  
  funko1.set_preco(5000)
  print("Após alteração o preço ficou: ",funko1.get_preco())

  funko1.set_personagem("Homem aranha Miles morales")
  print("Após alteração o nome virou: ",funko1.get_personagem())

  funko1.set_cor("Vermelho e azul")
  print("Após alteração a cor ficou: ",funko1.get_cor())

  print(funko1.mais_caro(funko2))
  
