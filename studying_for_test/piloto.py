class Piloto: 

  aumento = 1.10

  def __init__(self, nome, sobrenome, salario):
    self.nome = nome
    self.sobrenome = sobrenome
    self.salario = salario


  @property
  def email(self):
    return '{}.{}@email.com.br'.format(self.nome, self.sobrenome)

  @property

  def nome_completo(self):
    return '{} {}'.format(self.nome, self.sobrenome)


  def aumentar_salario(self):
    self.salario = float(self.salario * self.aumento)


    
