#from statistics import mean#
#print('A média da Turma é: ', mean(l_notas))                MEAN É ALGORITMO DO PYTHON PARA CALCULAR A MEDIA ARITMETICA MAS PRECISA SER IMPORTADO DE STATISTICS#

l_notas = []
print('Digite o [-1] para sair')
while True:
    nota = float(input("Nota do aluno: "))
    if nota == -1:
        break
    l_notas.append(nota)
if len(l_notas) != 0:
    media = sum(l_notas) / len(l_notas)  
    print(' Média da Turma : ',media )
    print('A quantidade de alunos na sala é de : ', len(l_notas))
else:
    print('Não existe divisão por zero.')
