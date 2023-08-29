class Veiculo:
    def __init__(self,modelo, ano=0 ,valor=0):
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def get_nome_atributos1(self):
        return self.get_nome_atributos1
    
    def set_nome_atributo1(self, novo_valor):
        self.nome_atributo1 = novo_valor
    
    def set_modelo(self, novo_modelo):
        self.modelo = novo_modelo
    
    def set_ano(self, novo_ano):
        self.ano = novo_ano
    
    def get_valor(self):
        return self.valor
    
    def mostra_dados1(self):
        print("Veículo 1: ",self.modelo,"Ano:",self.ano,"Preço:",self.valor)

    def mostra_dados2(self):
        print("Veículo 2: ",self.modelo,"Ano:",self.ano,"Preço:",self.valor)

    def mostra_dados3(self):
        print("Veículo 3: ",self.modelo,"Ano:",self.ano,"Preço:",self.valor)

    def mostra_dados4(self):
        print("Veículo 4: ",self.modelo,"Ano:",self.ano,"Preço:",self.valor)

    def mostra_dados5(self):
        print("Veículo 5: ",self.modelo,"Ano:",self.ano,"Preço:",self.valor)
    
    def set_valor(self, novo_valor):
        self.valor = novo_valor

    def aumenta_valor(self, aumento):
        self.valor += aumento

    def compara_valor(self, outro_veiculo):
        if self.valor > outro_veiculo.valor:
            return f"O veículo {self.modelo} é mais caro."
        elif self.valor < outro_veiculo.valor:
            return f"O veículo {outro_veiculo.modelo} é mais caro."
        else:
            return "Os veículos têm o mesmo valor."

    def compara_valor_2(self, outro_veiculo):
        if self.valor > outro_veiculo.valor:
            return self.retorna_dados()
        elif self.valor < outro_veiculo.valor:
            return outro_veiculo.retorna_dados()
        else:
            return "Os veículos têm o mesmo valor."





if __name__ == "__main__":

    veiculo1 = Veiculo("Onix LTZ Turbo", 2021, 85000.00)
    print("Antes da alteracão:")
    veiculo1.mostra_dados1()

    veiculo1.set_modelo("Cruze Ltz Turbo")
    print("Após a alteração: ")
    veiculo1.mostra_dados1()

    veiculo1.set_valor(78000.00)
    print("Após desconto o preço ficou assim: ")
    veiculo1.mostra_dados1()


    veiculo1_aumento = float(input("Digite o valor do aumento: "))
    veiculo1.aumenta_valor(veiculo1_aumento)

    print("Após o aumento ficou: ")
    veiculo1.mostra_dados1()



    
    veiculo2 = Veiculo("Peugeot 208", 2024, 110000.00)

    veiculo2.mostra_dados2()

    veiculo3 = Veiculo("Renault Kwid", 2022)

    veiculo3.mostra_dados3()

    veiculo4 = Veiculo("Porsche cayman")

    veiculo4.mostra_dados4()

    veiculo5 = Veiculo("Corolla Cross", 0, 215000.00)

    veiculo5.mostra_dados5()


    

    