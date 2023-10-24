class Conta(object):
    def __init__(self, nome, saldo):
        self.nome = nome
        self.saldo = saldo
    
    def get_nome(self):
        return self.nome
    
    def get_saldo(self):
        return self.saldo

    def set_nome(self):
        novo_nome = input("Digite o novo nome: ")
        self.nome = novo_nome

    def set_saldo(self):
        novo_saldo = int(input("Digite o novo saldo: "))
        self.saldo = novo_saldo
    
    def __str__(self):
        s = f'Nome: {self.nome}, R$ {self.saldo}'
        return s
    

    def deposito(self):
        valor_deposito = int(input('Digite o valor do deposito: '))
        if valor_deposito > 0 :
            self.saldo = self.saldo + valor_deposito
        else:
            print('Não é possivel depositar saldos negativos')
    

    def retirada_rn2(self, valor):
        nome_classe = self.__class__.__name__
        if nome_classe == 'Conta_PF':
            total = valor + 2
        else:
            total = valor + 5

        valor_retirada = int(input('Digite o valor que deseja retirar: '))

        if valor_retirada > self.saldo:
            print('Não é possivel retirar uma quantidade que não e possuida')

        elif valor_retirada > 0 :
            self.saldo = self.saldo - valor_retirada

        else:
            print('Não é possivel retirar um valor negativo')
        

       



class Conta_PF(Conta):
    def __init__(self, nome, saldo= 0.0, genero=' ', cpf=''):
        super().__init__(nome,saldo)
        self.genero = genero
        self.cpf = cpf

    def get_genero(self):
        return self.genero
    
    def get_cpf(self):
        return self.cpf

    def set_genero(self):
        novo_genero = input("Digite o Genero: ")
        self.genero = novo_genero

    def set_cpf(self):
        novo_cpf = input("Digite o novo CPF: ")
        self.cpf = novo_cpf

    

class Conta_PJ(Conta):
    def __init__(self,nome,saldo,modalidade, cnjp):
        super().__init__(nome,saldo)
        self.modalidade = modalidade
        self.cnjp = cnjp

    def get_modalidade(self):
        return self.modalidade
    
    def get_cnpj(self):
        return self.cnjp

    def set_modalidade(self):
        nova_modalidade = input("Digite a Modalidade: ")
        self.modalidade = nova_modalidade

    def set_cnpj(self):
        novo_cnpj = input("Digite o novo CNPJ: ")
        self.cnpj = novo_cnpj
    


if __name__ == '__main__':
    c1 = Conta('Alice', 800)
    print(c1)

    c1_pf = Conta_PF('Joao', 0, 'Masculino', '09378839200')

   

    


    c1_pj = Conta_PJ('Augusto',500, 'Multinacional','0003902920')

    print(vars(c1_pj))

    

    print(vars(c1_pj))

    c1_pf.retirada_rn2(0)

    print(c1_pf.__dict__)

