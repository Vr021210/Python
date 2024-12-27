from pylab import randint

restart = 1
while restart == 1:
    n = int(input("Skriv antall kast: "))
    
    if n <= 0:
        print("Antall kast må være større enn 0.")
        continue
    
    ener = 0
    toer = 0
    treer = 0
    firer = 0
    femmer = 0
    sekser = 0
    
    for i in range(n):
        terning = randint(1, 7)
        if terning == 1:
            ener += 1 
        elif terning == 2:
            toer += 1 
        elif terning == 3:
            treer += 1  
        elif terning == 4:
            firer += 1  
        elif terning == 5:
            femmer += 1  
        elif terning == 6:
            sekser += 1 
       
    print("Enere:", ener, ener/n*100, "%")
    print("Toere:", toer, toer/n*100, "%")
    print("Treere:", treer, treer/n*100, "%")
    print("Firere:", firer, firer/n*100, "%")
    print("Femmere:", femmer, femmer/n*100, "%")
    print("Seksere:", sekser, sekser/n*100, "%")
    
    restart = input("Hvis du vil kaste igjen, skriv 1. Hvis ikke, skriv 'exit': ")
    if restart == "exit":
        print("Ferdig, takk for at du spilte.")
        break
    restart = 1  