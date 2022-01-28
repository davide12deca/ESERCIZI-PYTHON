from typing_extensions import Self


class pila():
    def __init__(self):  ##costruttore inizializza la pila vuota
        self.pila =[]
        

    def push(self, elemento):   ## funzione push aggiunge l'elemento passato alla pila
        self.pila.append(elemento)
        
        
    def pop(self):  ##restituisce la pila senza l'ultimo elemento
       
        if(len(self.pila)!=0):
            return self.pila.pop()
        else:
            return None

    def print(self):
        print(self.pila)


p1 = pila()  ##istanza della classe pila
