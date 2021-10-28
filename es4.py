#slicing 
stringa = "classe quarta A robotica"
print(f"il primo carattere della stringa è {stringa[0]}")
print(f"l'ultimo carattere della stringa è {stringa[-1]}")
print(stringa[0:6]) #prende  i caratteri dalla posizione zero fino alla posizione 6 escluso 
                    #le stringhe in python sono immutabili
stringa nuova= stringa[:7] + "terza" + stringa[16:]
print(stringa nuova)

a, b = 4, 7  # assegnazione multipla. 
print(f"la variabile a vale: {a}, e la variabile b vale {b}")

a, b = b, a #in una riga di codice inverto i valori delle variabili! 

print(f"la variabile a vale: {a}, e la variabile b vale {b}") 