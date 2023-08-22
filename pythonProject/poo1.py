class Aluno : 
    def __init__(self,nome, mensalidade=1000.0, idade=18):
        self.nome = nome
        self.mensalidade = mensalidade
        self.idade = idade
    def get_nome(self):
        return self.nome
    def set_nome(self, novo_nome):
        self.nome = novo_nome
    def get_mensalidade(self):
        return self.mensalidade
    def set_mensalidade(self, nova_mensalidade):
        self.mensalidade = nova_mensalidade
    def get_idade(self):
        return self.idade
    def set_idade(self, nova_idade):
        self.idade = nova_idade
    def mostra_dados(self):
        print("Nome:", self.nome, "Mensalidade: ", self.mensalidade,"Idade: ", self.idade)
    def retorna_dados(self):
        return "Nome: ",self.nome,"Mensalidade: ", self.mensalidade, "Idade; ", self.idade
    def aumento_mensalidade_valor (self,aumento):
        self.mensalidade += aumento
    
    def aumento_mensalidade_porcentagem (self, percentual):
        aumento = self.mensalidade * (percentual/100)
        self.mensalidade += aumento

    def pode_tirar_cnh(self):
        if self.idade >= 18:
            return True
        else:
            return False
    




if __name__ == "__main__":

    aluno1 = Aluno('Cauê')
    aluno2 = Aluno('Carla', 900.00, 20)
    
    aluno1.mostra_dados()
    aluno2.mostra_dados()

    aluno1.set_mensalidade(1100.0)
    aluno2.set_idade(21)

    print("Após alteraçôes: ")
    aluno1.mostra_dados()
    aluno2.mostra_dados()

    aluno1.aumento_mensalidade_valor(100.0)
    aluno2.aumento_mensalidade_porcentagem(10)

    print("Após aumentos: ")
    aluno1.mostra_dados()
    aluno2.mostra_dados()

    print("Aluno 1 pode tirar CNH: ", aluno1.pode_tirar_cnh() )
    print("Aluno 2 pode tirar CNH: ", aluno2.pode_tirar_cnh())

    aluno3 = Aluno("Carlos")
    aluno3.mostra_dados()

   






