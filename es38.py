from itertools import tee
from re import T


def  Fibonacci(n):
    temp = 1
    numPerc = 1
    while temp < n:
        fib = temp + numPerc
        numPerc = temp
        temp = fib
        if fib <= n:
            print(fib)

num  = int(input("inserisci un numero intero: "))