lettere = ["a", "b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," "]

codifica = int(input("vuoi codificare, inserisci 1. // vuoi decodificare, inserisci 0. \n"))

if(codifica == 1):
    parola = input("inserisci parola da codificare: ")
    num = int(input("inserisci numero di criptografia:"))  

    nuovaStringa = ""
 
    for x in parola:
        nuovaStringa+= lettere[int((x + num)%28)]

elif(codifica == 0):
    parola = input("inserisci parola da decodificare: ")
    num = int(input("inserisci numero di criptografia:"))  

    for x in int(len(parola)):
      print(lettere[x-(num%len(lettere))])

else:
    print(f"numero non valido.")


