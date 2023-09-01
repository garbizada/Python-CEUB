class Computador:
    def __init__(self,processador: str =0,placa_de_video: str =0,memoria=16):
        self.processador = processador
        self.placa_de_video = placa_de_video
        self.memoria = 16

    def set_processador(self,novo_processador):
        self.processador = novo_processador

    def get_processador(self):
        return self.processador

    def set_placa_de_video(self,nova_placa):
        self.placa_de_video = nova_placa

    def get_placa_de_video(self):
        return self.placa_de_video

    def set_memoria(self,nova_memoria):
        if nova_memoria >= 8:
            self.memoria = nova_memoria
        else:
            print("Seu pc esta precisando melhorar ein!")

    def get_memoria(self):
        return self.memoria
    
    def mostra_placa(self):
        print("Seu computador tem a placa de vìdeo: ",self.placa_de_video)


    def mostra_processador(self):
        print("Seu computador tem  processador ",self.processador)

    def aumenta_memoria(self):
        self.memoria += 4
    
    def mostra_memoria(self):
        print("Seu computador tem ",self.memoria,"gb de memoria")



if __name__ == "__main__":

    computador1 = Computador("i3-9000k","RTX-3090","36")
    #computador 1 metodos

    print(f"Mémoria do computador 1 antes do aumento: {computador1.memoria}")
    computador1.aumenta_memoria()
    print(f"Mémoria do computador 1 apos o aumento: {computador1.memoria}")




    #fim computador 1

    computador2 = Computador("i7-13440k","RTX-4090")
     #computador 2 metodos
    nova_memoria = int(input("Quantas GB tem sua memoria: "))
    computador2.set_memoria(nova_memoria)
    computador2.mostra_memoria()
    





    #fim computador 2

    computador3 = Computador("i9-13450k")
     #computador 3 metodos

    nova_placa = input("Qual a placa de vídeo do seu computador?: ")
    computador3.set_placa_de_video(nova_placa)
    computador3.mostra_placa()
    computador3.mostra_memoria()


    





    #fim computador 3

    
    


