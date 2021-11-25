num1 = float(input("inserisci primo numero: "))
num2 = float(input("inserisci secondo numero: "))
operazione = input("che operazione vuoi fare?")

if(operazione == "somma"):
    somma = num1+num2
    print(somma)
elif(operazione == "sottrazione"):
    sott = num1-num2
    print(sott)
elif(operazione == "moltiplicaizone"):
    molt = num1*num2
    print(molt)
else:
    div = num1/num2
    print(div)

