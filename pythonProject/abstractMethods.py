from abc import ABC, abstractmethod
import math
class FormaGeometrica(ABC):
    qtdFormas = 0
    formas = []

    @classmethod
    def getQtdFormas(cls):
        return cls.qtdFormas


    def __init__(self):
        ...
        FormaGeometrica.qtdFormas += 1
        FormaGeometrica.formas.append(self)


    @classmethod
    def mostraFormas(cls):
        print("Nome de todas as formas: ")
        for objeto in FormaGeometrica.formas:
            print(f"- {objeto.__class__.__name__}")


    @abstractmethod
    def  area(self):
        ...
    @abstractmethod
    def perimetro(self):
        pass

    def concretMethod(self):
        print("Essa e uma mensagem fixa")

    def mostrar_mensagem(self):
        print(f"Qual é essa forma geometrica: {self.__class__.__name__}.")
        self.identificar_objeto()

    def identificar_objeto(self):
        print(f"Objeto da subclasse: {self.__class__.__name__}")


class Quadrado(FormaGeometrica):
    def __init__(self, lado):
        super().__init__()
        self.lado = lado
    
    def getQuadrado(self):
        return self.lado
    
    def setQuadrado(self):
        novo_lado = input("Digite a quantidade de lado do quadrado: ")
        self.lado = novo_lado

    def area(self):
        area = self.lado * self.lado
        return area
    
    def perimetro(self):
        perimetro = 4
        return perimetro

class Circulo(FormaGeometrica):
    def __init__(self, raio):
        super().__init__()
        self.raio = raio

    def getRaio(self):
        return self.raio
    
    def setRaio(self):
        novoRaio = input("Digite o raio do circulo: ")
        self.raio = novoRaio


    def area(self):
        area = math.pi * self.raio * self.raio
        return area
    
    def perimetro(self):
        perimetro = 2 * math.pi * self.raio
        return perimetro
    
    




if __name__ == '__main__':

    #obj_forma = FormaGeometrica()
    #print(obj_forma)           não pode ser criado um objeto da classe abstrata

    objQuadrado = Quadrado(4)
    #objQuadrado.setQuadrado()


    #print(objQuadrado.getQuadrado())
    #print(objQuadrado)


    objCirculo1 = Circulo(10)

    print(f"A area do circulo é: {objCirculo1.area():.2f}")    
    print(f"O perimetro do circulo é: {objCirculo1.perimetro():.2f}")

    objCirculo1.concretMethod()
    objCirculo1.mostrar_mensagem()

    print("A quantidade total de formas é: ",FormaGeometrica.getQtdFormas())
    FormaGeometrica.mostraFormas()