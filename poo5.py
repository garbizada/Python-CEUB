import math
class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def get_ponto_x(self):
        return self.x
    
    def get_ponto_y(self):
        return self.y
    
    def set_ponto_x(self, loca_x):
        if type(loca_x) in (float, int):     # ou usar if isinstance(loca_x, int)
            self.x = loca_x
        else:
            print("Digite uma posição númerica!!")
    
    def set_ponto_y(self, loca_y):
        if type(loca_y) in (float, int):
            self.y = loca_y
        else:
            print("Digite uma posição númerica!!")

    def __str__(self):
        s = f"{self.x},{self.y}"
        return s 
    
    def distancia_origem(qlqr_ponto):
        origem_x = 0
        origem_y = 0
        distancia = math.sqrt((origem_x - qlqr_ponto.x )**2 + (origem_y  - qlqr_ponto.y )**2)
        return distancia

    def distancia_dois_pontos (qlqr_ponto, outro_ponto):
        distancia_2_p = math.sqrt((outro_ponto.x - qlqr_ponto.x )**2 + (outro_ponto.y  - qlqr_ponto.y )**2)
        return distancia_2_p




if __name__ == "__main__":

    ponto1 = Point()
    print(ponto1.get_ponto_x())
    print(ponto1.get_ponto_y())

    ponto2 = Point(2, 3)

    print("Atributos x e y do ponto 2: ",ponto2.__str__())

    ponto3 = Point(3)
    ponto3.set_ponto_y(0)
    print("Atributos x e y do ponto 3: ",ponto3.__str__())

    ponto4 = Point(0,5)

     
    print("Distancia da origem", Point.distancia_origem(ponto2))

    print("Distancia entre dois pontos", Point.distancia_dois_pontos(ponto2, ponto3))
    



        

