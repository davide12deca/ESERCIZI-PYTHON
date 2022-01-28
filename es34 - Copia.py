import random 

alice = [random.randrange(1,6) for x in range(10)]
bob = [random.randrange(1,6) for x in range(10)]

f = open("./file/lancio.txt")

for x in range(10):
    f.write(str(alice[x]) + "," + str(bob[x]) + "\n")


f.close()