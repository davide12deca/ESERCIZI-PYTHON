x1 = float(input("inserisci cordinata x1: "))
y1 = float(input("inserisci cordinata y1: "))
x2 = float(input("inserisci cordinata x2: "))
y2 = float(input("inserisci cordinata y2: "))
 
punto1 = (x1,y1)
punto2 = (x2,y2)

differenzaX = punto2[0] - punto1[0] 
differenzaY = punto2[1] - punto2[1]

distanza = ((differenzaX**2) + (differenzaY**2)**(1/2))
print(distanza)
