

#l_notas = []

#print('Digite [-1] para sair')
#while True: 
    #nota = float(input("Nota do aluno: "))
   # if nota == -1:
  #      break
    
 #   l_notas.append(nota)

#media_notas = sum(l_notas) / len(l_notas)
#print("a quantidade de alunos é: ", len(l_notas))
#print("A média desses alunos é: ", media_notas)


   #  OUTRO MODO DE CALCULAR A MEDIA COM LISTAS SEM O SUM E LEN 
import statistics
lista = [2, 3, 4, 5]
media = statistics.mean(lista)
print(media)
