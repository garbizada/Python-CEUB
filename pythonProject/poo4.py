class Produto(object):
    qtd_produto = 0
    produtos = []

    @classmethod
    def get_qtd_produto(cls):
        return cls.qtd_produto

    def __init__(self, nome, vlr_compra = 0, vlr_venda = 0, qtd_estoque = 0, qtd_minima = 0):
        self.nome = nome
        self.vlr_compra = vlr_compra
        self.vlr_venda = vlr_venda
        self.qtd_estoque = qtd_estoque
        self.qtd_minima = qtd_minima
        type(self).qtd_produto += 1
        Produto.produtos.append(self)

    
    @classmethod
    def mostra_produtos(cls):
        print("Nome de todos os produtos: ")
        for objeto in Produto.produtos:
            print(f"- {objeto.get_nome()}")

        

    def get_nome(self):
        return self.nome
    
    def set_nome(self, novo_nome):
        if isinstance(novo_nome, str):
            self.nome = novo_nome
        else: 
            print("Erro: Nome não contém número")

        
    
    def get_qtd_estoque(self):
        return self.qtd_estoque
    
    def set_qtd_estoque(self, nova_qtd_e):
        if isinstance(nova_qtd_e, int):
            self.qtd_estoque = nova_qtd_e
        else: 
            print("Erro: Quantidade não contém letras")
        
    
    def get_qtd_minima(self):
        return self.qtd_minima

    def set_qtd_minima(self, nova_qtd_m):
        self.qtd_minima = nova_qtd_m
    

    def set_vlr_compra(self, vlr_compra_nova):
        if isinstance(vlr_compra_nova, int):
            self.vlr_compra = vlr_compra_nova
        else: 
            print("Erro: Valor não contém letra")
    
    
    def __str__(self):
        s = f"{self.nome},{self.vlr_compra},{self.qtd_estoque}"
        return s 


    def lucro(self):
        lucro = self.vlr_venda - self.vlr_compra
        return lucro

    def atualiza_estoque(self):
        qtd_vendida = int(input("Digite a quantidade de produtos vendidos: "))
        self.qtd_estoque -= qtd_vendida
    
    def repor_produto(self):
        qtd_comprada = int(input("Digite a quantidade de produtos comprados: "))
        self.qtd_estoque += qtd_comprada


    def alerta_estoque(self):
        if self.qtd_estoque < self.qtd_minima:
            return True
        else: 
            return False

    def maior_qtd(self,outro_produto):
        if self.qtd_estoque > outro_produto.qtd_estoque:
            return f"O produto {self.nome} tem mais quantidade em estoque"
        elif self.qtd_estoque < outro_produto.qtd_estoque:
            return f"O produto {outro_produto.nome} tem mais quantidade em estoque"
        else:
            return "Ambos produtos tem a mesma quantidade em estoque"


    def maior_lucro(self,outro_lucro):
        if self.lucro() > outro_lucro.lucro():
            return f"O produto {self.nome} tem mais lucro"
        elif self.lucro() < outro_lucro.lucro():
            return f"O produto {outro_lucro.nome} tem mais lucro"
        else:
            return "Ambos produtos tem o mesmo lucro"

if __name__ == "__main__":

    

    produto1 = Produto("Arroz", 15, 25, 500, 100)
    print("Nome do produto: ",produto1.get_nome())
    print("A quantidade de produtos no estoque é: ",produto1.get_qtd_estoque())
    print("A quantidade minima é: ",produto1.get_qtd_minima())

    produto1.set_qtd_minima(50)
    print("Após alteração da qtd minima ficou: ",produto1.get_qtd_minima())

    print("O lucro obtido no produto é de: ", produto1.lucro())
    produto1.atualiza_estoque()
    produto1.repor_produto()

    print("A quantidade de produtos no estoque está em alerta?: ", produto1.alerta_estoque())


    produto2 = Produto("Feijão")
    produto3 = Produto("Manteiga", 10)
    produto4 = Produto("Cebola",0,0,1000)

    print(produto1.maior_qtd(produto4))

    print(produto1.maior_lucro(produto2))
    
    print("A quantidade total de produtos é: ",Produto.get_qtd_produto())
    Produto.mostra_produtos()
    



    
    

        