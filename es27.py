tavola= [(x*y)for x in range(11) for y in range(11)]
indice = 0
indice1 = 11

for _ in range(11):
    print(tavola[indice: indice1])
    indice+=11
    indice1+=11