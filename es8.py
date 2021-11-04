stringa = "ciao" 
#es 8
print(f"la prima lettera è: {stringa[0]} l'ultima lettera è: {stringa[-1]}")
#es9
print(stringa[1:-1])
#es10
print(f"{stringa[0:1]}{stringa[2:3]}{stringa[4: -1]}")
#es11 
print(f"la parola invertita è: {stringa[-1: -3]}")
#es12  
stringa1 = "comunque"

print(stringa1[0:2]+ "?" + stringa1[3:])