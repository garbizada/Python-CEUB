class Livro(object): 
    qtd_livro = 0
    livros = []

    @classmethod
    def get_qtd_livro(cls):
        return cls.qtd_livro



    def __init__(self, titulo, autor, paginas, preco = 0):
        self.titulo = titulo 
        self.autor = autor 
        self.paginas = paginas 
        self.preco = preco
        type(self).qtd_livro += 1
        Livro.livros.append(self)

    def get_autor(self):
        return self.autor

    def set_autor(self, novo_autor):
        self.autor = novo_autor

    def get_preco(self):
        return self.preco

    def set_preco(self, novo_preco):
        if (self.preco <= 0):
            print("Pegou de graça foi? salafrario")
        else:
            self.preco = novo_preco

    
    def set_aumento(self,aumento):
       self.preco += aumento

    def mostra_dados(self):
        print("Nome do autor: ", self.autor, "Preço do livro: ", self.preco, "Nome do livro: ", self.titulo, "Número de paginas: ", self.paginas)    
    
    def aumento_porcentagem (self, percentual):
        aumento = self.preco * (percentual/100)
        self.preco += aumento


    def __str__(self):
        s = f"{self.autor},{self.titulo},{self.paginas}, {self.preco}"
        return s 
        
    
if __name__ == '__main__':
    livro1 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien ", 1000, 49.90)
    print(livro1)
    print("O autor do primeiro Livro é: ",livro1.get_autor())
    print("O preço do primeiro livro é: ",livro1.get_preco())

    livro1.set_preco(66.00)
    print("Novo preço: ", livro1.get_preco())


    livro2 = ("Harry Potter e a Pedra filosofal", "J.K. Rowling", 300)
    print(livro2)
    livro3 = ("Percy Jackson", "J.K. Rowling", 500)

    livro1.set_aumento(3000)
    print(livro1.get_preco())

    livro1.mostra_dados()

     
    print("A quantidade total de livros é: ",Livro.get_qtd_livro())


    
