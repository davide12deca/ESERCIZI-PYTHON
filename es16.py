## python ha due cicli, il while e il for 
voto = -1
while(voto < 6){
    print(f"sei insufficente!")
    voto = int(input("inserisci il tuo voto: "))
}
 if(voto = 6):
     print(f"sei appena sufficente")
 elif(voto > 6) 
     print(f"bravo!")


## ciclo for:

classi = ["4arob", " 3arob", "5brob", "4achi"]
classe = input("inserisci la classe che ti interessa: ")
indirizzi = {"rob":"Smart-rob", "chi":"Chimica", "inf":"Informatica"}
for classe in classi:
    indirizzo = indirizzi[classe[-3:]]    
    print(f"La classe {classe} è dell' indirizzo {indirizzi}") ## -3 stampa le ultime 3 lettere
