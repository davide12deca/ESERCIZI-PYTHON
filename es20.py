##data una lista di numeri ritorni il suo valore massimo e il suo valore minimo

list = ["1", "10", "19", "2", "35", "3"]


max = 0
k = 0

for lista in list:
    if list[k] > max:
        max = list[k]
    else:
        max = max    
k = k + 1

