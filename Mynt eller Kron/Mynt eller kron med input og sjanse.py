from pylab import randint

restart = 1
while restart == 1:
    n = int(input("Skriv antall kast: "))
    
    if n <= 0:
        print("Antall kast må være større enn 0.")
        continue
    
    ener = 0
    toer = 0
    en_av = 2 ** n
    fraction = 1 / en_av
    percentage = fraction * 100
    
    for i in range(n):
        terning = randint(1, 3)
        if terning == 1:
            ener += 1 
        elif terning == 2:
            toer += 1 
      
       
    print("mynt:", ener, ener/n*100, "%")
    print("kron:", toer, toer/n*100, "%")
    print("")
    print("Sjansen for å få kombinasjonen du fikk var 1 av",en_av)
    print("")
    print("Prosentsjansen var:", percentage, "% sjanse")
    print("")
    
    restart = input("Hvis du vil kaste igjen, skriv 1. Hvis ikke, skriv 'exit': ")
    if restart == "exit":
        print("Ferdig, takk for at du spilte.")
        break
    restart = 1  
