

class Conta(object):                    # Superclasse
    qtd_conta = 0
    @classmethod
    def get_qtd_conta(cls):
        return cls.qtd_conta

   

    def __init__(self, nome, saldo):  # Construtor  com default
        self.nome = nome                # Atributos de instância (objeto)
        self.saldo = saldo
        Conta.qtd_conta += 1


    def get_nome(self):                 # Consulta
        return self.nome
    
    def set_nome(self, novo_nome):      # Altera
        self.nome = novo_nome

    def get_saldo(self):
        return self.saldo
    
    def __str__(self):                  # Sobrescreve o método __str__ do Python
        s = f'Nome: {self.nome}, R$ {self.saldo}'               # f-string
        return s
    
    def deposito(self, valor):          # Métodos funcionais
        self.saldo += valor             # self.saldo = self.saldo + valor

    def retirada(self, valor): 
        nome_classe = self.__class__.__name__
        if nome_classe == 'Conta_PF':
            total = valor + 2
        else:
            total = valor + 5

        valor_retirada = int(input("Digite o saldo que quer retirar"))        
        if valor_retirada > self.saldo:
            print('Não é possivel retirar uma quantidade que não e possuida')

        elif valor_retirada > 0 :
            self.saldo = self.saldo - valor_retirada

        else:
            print('Não é possivel retirar um valor negativo')          # self.saldo = self.saldo - valor



class Conta_PF(Conta):      # Subclasse Conta_PF herda da superclasse Conta
    def __init__(self, nome, saldo, genero = '', cpf=''):  # Valores default
        super().__init__(nome, saldo)   # Chama o construtor da superclasse
        self.genero = genero
        self.cpf = cpf
        
    def get_genero(self):               # Consulta
        return self.genero
    
    def set_genero(self, novo_genero):  # Altera
        self.genero = novo_genero

    def get_cpf(self):
        return self.cpf
    
    def set_cpf(self, novo_cpf):
        self.cpf = novo_cpf



class Conta_PJ(Conta):  # Subclasse Conta_PJ que herda da superclasse Conta
    def __init__(self, nome, saldo, modalidade = '', cnpj=''):  # Construtor
        super().__init__(nome, saldo)       # Chama o construtor da superclasse
        self.modalidade = modalidade
        self.cnpj = cnpj

    def get_modalidade(self):
        return self.modalidade
    
    def get_cnpj(self):
        return self.cnpj
    
    def set_cnpj(self, novo_cnpj):
        self.cnpj = novo_cnpj


if __name__ == '__main__':
    cpf1 = Conta_PF('felipe', 10000, 'MASCULINO', '000090900')
    cpf2 = Conta_PF('Pedro', 200000, 'MASCULINO')
    cpf3 = Conta_PF('Lethicia', 5000)

    cpf1.deposito(600)
    print("O novo saldo da conta 1 de pessoa fisica é: " , cpf1.get_saldo())

    cpf1.retirada(1200)
    print("O novo saldo apos a retirada da conta 1 vai ser de: ", cpf1.get_saldo())

    cpj1 = Conta_PJ('Caue', 1000000000, '' , '500993090009')
    cpj2 = Conta_PJ('Cortex', 1000000000)


    cpf2.retirada(5000)
    cpj2.retirada(9000)

    print(cpf2.get_saldo())
    print(cpj2.get_saldo())

    print( Conta.get_qtd_conta())





