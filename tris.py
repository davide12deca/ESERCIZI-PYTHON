##def disegnaGriglia():
  ##  print(f"{griglia[0]} | {griglia[1]} | {griglia[2]}\n{griglia[3]} | {griglia[4]} | {griglia[5]} \n {griglia[6]} | {griglia[7]} | {griglia[8]} \n ")

griglia = {0: " ", 1: " ",2: " ", 2: " ",4: " ",5: " ",6: " ", 7: " ",8: " "}
giocatori = {1: "Davide", 2: "Bob"}

partitaFinita = False
while(True):
    #ciclo
    conta = 0

    while(conta<9):
        
        mossa = input(giocatori[1] + " Dove vuoi posizionare la X: ")
        print(f",{griglia[0]}, |, {griglia[1]}, |, {griglia[2],}\n,{griglia[3]}, |, {griglia[4]}, |, {griglia[5]}, \n, {griglia[6]}, |, {griglia[7]}, |, {griglia[8]}, \n ")
        if(griglia[mossa] == " "):
            griglia[mossa] = "X"
        else: 
            mossa = (input(giocatori[1] + "inserisci una posizione libera: "))
            print(f",{griglia[0]}, |, {griglia[1]}, |, {griglia[2],}\n,{griglia[3]}, |, {griglia[4]}, |, {griglia[5]}, \n, {griglia[6]}, |, {griglia[7]}, |, {griglia[8]}, \n ")

        
        mossa2 = input(giocatori[2] + " Dove vuoi posizionare  lo 0:")
        print(f",{griglia[0]}, |, {griglia[1]}, |, {griglia[2],}\n,{griglia[3]}, |, {griglia[4]}, |, {griglia[5]}, \n, {griglia[6]}, |, {griglia[7]}, |, {griglia[8]}, \n ")
        if(griglia[mossa2] == " "):
            griglia[mossa2] = "0"
        else: 
            mossa2 = (input(giocatori[1] + "inserisci una posizione libera: "))
            print(f",{griglia[0]}, |, {griglia[1]}, |, {griglia[2],}\n,{griglia[3]}, |, {griglia[4]}, |, {griglia[5]}, \n, {griglia[6]}, |, {griglia[7]}, |, {griglia[8]}, \n ")
        conta = conta + 1
    #chiedere le mosse al giocatore 1
    #controllo cella libera

    #disegna la griglia mentre giocano
    

    
    #chiedere la mossa al giocatore 2
    #controllo cella libera

    #disegna la griglia mentre giocano
   
    