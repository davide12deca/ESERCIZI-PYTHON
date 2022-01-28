from curses.ascii import ENQ


class coda():
    def __init__(self):
        self.coda = []
    
    def enqueue(self, elemento):
        self.coda.append(elemento)

    def dequeue(self):
    
        if(len(self.pila)!=0):
            return self.pila.pop()
        else:
            return None

    def print(self):
        print(self.pila)

def main():
    c1 = coda()  ##istanza della classe pila
    c1 = enqueue("ciao")
    c1 = dequeue()

if __name__ == "__main__":
    main()


