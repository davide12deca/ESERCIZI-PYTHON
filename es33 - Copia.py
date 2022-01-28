num  = int(input("inserisci numero: "))

lista = ["pari" if((x%2)==0) else "dispari" for x in range(1,num+1)]
print(lista)