from os import fdopen
import turtle
snow = turtle.Turtle()
finestra = turtle.Screen()

f = open("./file/testo.txt","w")
righe = f.readlines()

for riga in righe(10):
    lista = riga.split(":")
    if lista[0] == "forward":
    

f.close()
