def NPRIMI():
    def NPRIMI(N):   ##funzione numeri primi.
        k = 2
        continua = True

        while(continua==True and k < N):
            if(N%k==0):
                continua=False
            
            else:
                k = k + 1

            return continua




x = int(input("inserisci numero"))
primi = [k for k in range(2,1003) if nprimi(k)]
if(NPRIMI(x)==True):
    print(f"il numero è primo!")
    
else: 
    print(f"il numero non è primo!")