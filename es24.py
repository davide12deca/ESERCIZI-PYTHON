palindroma = lambda frase:  frase == frase[::-1] ## per leggerla al contrario

frase = input("Inserisci una frase: ")
print(palindroma(frase))