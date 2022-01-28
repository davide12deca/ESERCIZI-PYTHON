list = []

f = open("./file/testo.txt","r")
list = f.readlines()

print(list[0], list[1])

f.close()