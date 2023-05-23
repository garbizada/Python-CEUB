ct=0
x=int(input("Digite o valor inicial da sequência: "))
y=int(input("Digite o valor final da sequência: "))

print("-Sequência de números inteiros:")
for i in range(x,y+1, 1):
    print(i, end=" ")
    ct+= 1
print("\nquantidade de valores digitados é: ", ct)