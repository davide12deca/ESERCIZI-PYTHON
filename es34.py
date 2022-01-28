import random
alice = [random.randrange(1,6) for x in range(10)]
bob = [random.randrange(1,6) for x in range(10)]

f = open("./file/lancioDado.txt", "w")

for x in range(10):
    f.write(str(alice[x]) + "," + str(bob[x]) + "\n")

f.close()