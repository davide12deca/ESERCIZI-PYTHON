import math
num = int(input("inserisci numero: "))

lista = [math.pow(2,x) for x in range(num) if (math.pow(2,x)<=num)]

for j in lista:
 print(j)

