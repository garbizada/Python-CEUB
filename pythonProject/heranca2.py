class Veiculo(object):
    def __init__(self, valor=0, modelo=0, km=1):
        self.valor = valor
        self.modelo = modelo
        self.km = km

    def get_valor(self):
        return self.valor
    
    def get_modelo(self):
        return self.modelo
    
    def get_quilometragem(self):
        return self.quilometragem
    
    def set_valor(self, novo_valor):
        novo_valor = int(input("Digite o novo valor do veiculo: "))
        self.valor = novo_valor

    def set_modelo(self, novo_modelo):
        novo_modelo =(input("Digite o novo modelo do veiculo: "))
        self.modelo = novo_modelo

    def set_km(self, nova_quilometragem):
        nova_quilometragem = int(input("Digite a kilometragem do veiculo: "))
        self.km = nova_quilometragem

    def atualiza_valor(self):
        atualizado_valor = int(input("Digite o valor mais atualizado do veiculo: "))
        if atualizado_valor > 0:
            self.valor = self.valor + atualizado_valor
        else:    
            print("O aumento não pode ser maior do que zero")
            

    def atualiza_valor_pct(self):
        porcentagem = int(input("Digite o acrescimento ao valor em porcentagem: "))
        calcula_pct = self.valor * porcentagem / 100
        if porcentagem > 0 :
            
            self.valor= self.valor + calcula_pct
        else: 
            print("Não é aceito palavras apenas números")

class Carro(Veiculo):
    def __init__(self, valor, modelo, km=1, qtd_portas=4):
        super().__init__(valor,modelo,km)
        self.qtd_portas = qtd_portas

    def get_qtd_portas(self):
        return self.qtd_portas

    def set_qtd_portas(self, nova_qtd):
        nova_qtd = int(input("Digite a quantidade de portas: "))
        self.qtd_portas = nova_qtd
    
    def __str__(self):
        s = f"Valor: {self.valor}, Modelo: {self.modelo}, Kilometragem: {self.km}, Qtd de portas: {self.qtd_portas}"
        return s
    
class Moto(Veiculo):
    def __init__(self,valor,modelo,km,cilindradas):
        super().__init__(valor,modelo,km)
        self.cilindradas = cilindradas
    
    def get_cilindradas(self):
        return self.cilindradas

    def set_cilindradas(self, nova_cilindrada):
        nova_cilindrada = int(input("Digite a cilindrada da moto: "))
        self.cilindradas = nova_cilindrada




if __name__ == '__main__':


    carro1 = Carro(60000, "Ford Ka 2022",0, 4)
    carro2 = Carro(70000, "Gol Last Edition",0,)
    carro3 = Carro(100000,"Mustang Dark Horse")

    moto1 = Moto(45000, "Hornet", 100000, 350)
    moto2 = Moto(120000, "Ninja", 0, 600)

    print(vars(moto1))
    print(vars(carro2))

    print(moto2.__dict__)
    print(carro1.__dict__)

    carro2.atualiza_valor()

    print(carro2.__str__())

    carro3.atualiza_valor_pct()

    print(carro3.__str__())