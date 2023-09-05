import datetime

class Pessoa:
    def __init__(self,nome, peso, altura, anonascimento =0):
        self.nome = nome
        self.peso = peso
        self.altura = altura
        self.anonascimento = anonascimento

    def get_nome(self):                   
       return self.get_nome
    
    def set_anonascimento(self, novo_ano):            
       self.anonascimento = novo_ano

    def mostra_dados(self):
        print("Nome: ",self.nome," \nPeso em KG: ", self.peso,"\nAltura em centimetros: ",self.altura,"\nAno de nascimento: ",self.anonascimento)

    def set_nome(self, novo_nome):
        if isinstance(novo_nome, str):
            self._nome = novo_nome
        else: 
            print("Erro: Nome não contém número")
    def imc(self):
        imc = self.peso / (self.altura * self.altura)
        return imc
    
    def __str__(self):
        s = f"{self.nome},{self.peso},{self.anonascimento}"
        return s 
        
    
    def calcula_idade(self):
        hoje = datetime.date.today()
        idade = hoje.year - self.anonascimento
        return idade

    def retorna_mais_velho(self, obj):
        if self.anonascimento < obj.anonascimento:
            print("Ano de nascimento mais velho: ", self.anonascimento)
            print("Ano nascimento mais novo: ", obj.anonascimento)
        elif obj.anonascimento < self.anonascimento:
            print("Ano nascimento mais velho: ", obj.anonascimento)
            print("Ano nascimento mais novo: ", self.anonascimento)
        else:
            print("As datas são iguais")





    
    
    
    
    
    
        
        

if __name__ == "__main__":

    pessoa1 = Pessoa("Cauê", 93, 1.93, 2004)
    pessoa2 = Pessoa("Maria", 50, 1.54, 2005)
    pessoa3 = Pessoa("Lethicia", 70, 1.75, 2004)
    
    pessoa1.set_anonascimento(2003)
    print("O IMC da pessoa 1 é: ","%.2f" % pessoa1.imc())


    print("A idade da pessoa 1 é: ",pessoa1.calcula_idade())

    print("Entre a pessoa 1 e a pessoa 2 quem e mais velho? ",pessoa1.retorna_mais_velho(pessoa2))
   





