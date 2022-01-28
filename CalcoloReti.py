def bin2dec(binario):
    ndec = 0
    k=len(binario)-1
    for x in binario:
        ndec = ndec + int(x)*2**k
        k = k-1
    return ndec


def dec2bin(decimale,nbit):
    nbin = bin(decimale)[2:]
    nbin = "0"*(nbit-len(nbin)) + nbin
    return nbin


def ip_bin2dec():
    x=x+1
    pass


def ip_dec2bin(ipdec):
    b= ""
    numero = ipdec.split(".")
    for x in numero:
        b+=dec2bin(int(x),8)
        
    return b


def main():
    binario = input("inserisci un numero binario: ")
    print(bin2dec(binario))
    decimale = int(input("Inserisci un numero deicmale: "))
    print(dec2bin(decimale,8))
    ipdec = input("Inserisci un ip di decimali: ")
    print(ip_dec2bin(ipdec))
    ipbin = input("Inserisci un ip in binario: ")

if __name__ == "__main__":
    main()
