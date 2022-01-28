nome = input("inserisci il tuo nome: ")
cognome = input("inserisci il tuo cognome: ")
giorno = int(input("inserisci il tuo giorno di nascita: "))
mese = input("inserisci il mese di nascita: ")
anno = int(input("inserisci l'anno di nascita: "))

diz = {"nome: ": nome, "cognome: ": cognome, "giorno: ": giorno, "mese: ": mese, "anno: ": anno}

f = open("./file/anagrafici.txt","w")

f.write(diz["nome: "])
f.write("\n")
f.write(diz["cognome: "])
f.write("\n")
f.write(str(diz["giorno: "]))
f.write("/")
f.write(diz["mese: "])
f.write("/")
f.write(str(diz["anno: "]))