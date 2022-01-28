import pila

scelta = int(input("inserisci elemento == (1)/ estrai elemento == (2)"))

if(scelta == 1):
    pila.p1.push(int(input("inserisci elemento da inserire: ")))


elif(scelta == 2):
    pila.p1.pop()

print 