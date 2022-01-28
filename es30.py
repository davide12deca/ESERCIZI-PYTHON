f = open("./file/primi.txt", "w")
x = 0
num = 2

while(x < 100):
    if(ePrimo(num) == True):
        f.write(str(num))
        x = x+1
    num = num+1        


