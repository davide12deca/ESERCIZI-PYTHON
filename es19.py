## CREA UN PROGRAMMA CHE PERMATTA ALL'UTENTE DI INSERIRE UN NUMERO QUALUNQUE DI INTERI ALL'INTERNO DI UNA LISTA STAMPALA AL TERMINE DELL' INTERIMENTO 
numero = int(input("inserisci 0 per terminare l'inserimento, altrimenti inserisci il numero nella lista: "))
lista = []

for indice in range(numero):
     lista.append(int(input("inserisci numero: ")))

print(lista)  
