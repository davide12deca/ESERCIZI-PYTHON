num = int(input("inserisci numero: "))

if((num%2)==0):
    print(f"il numero è divisibile per due! ")
elif((num%3)==0):
    print(f"il numero è divisibile per tre! ")

elif((num%5)==0):
    print(f"il numero è divisibile per cinque! ")

else:
    print(f"il numero non è divisibile ne per due ne per tre ne per cinque.") 
