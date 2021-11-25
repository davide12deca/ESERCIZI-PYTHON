dispari = [k for k in range(1000) if ((k%2)!=0)]  ##tutti i numeri dispari 
print(dispari) 


nomi = ["marco", "luca","giovanni", "mario", "maria"]

nomi_m = [nome for nome in nomi in nome[0]=="m"]   ## dalla lista dei nome filtra e prende solo i nomi che iniziano con la m
print(nomi_m)
