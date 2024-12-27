from pylab import randint
rødt=0
lyselilla=0 
lilla=0 
lyseblå=0 
lysegrønn=0
n=int(input("hvor mange ganger vil du snurre hjulet? "))

for i in range(n):
    lykkehjul = randint(1,7)
    
    if lykkehjul == 1:
        rødt = rødt+1 
    elif lykkehjul == 2:
        rødt = rødt+1
    elif lykkehjul == 3:
        lyselilla = lyselilla+1 
    elif lykkehjul == 4:
        lilla = lilla+1 
    elif lykkehjul == 5:
        lyseblå = lyseblå+1 
    elif lykkehjul == 6:
        lysegrønn = lysegrønn+1
    
print("rødt",rødt, rødt/n*100,"%")
print("lyselilla:", lyselilla,lyselilla/n*100,"%")
print("lilla:", lilla, lilla/n*100,"%")
print("lyseblå:", lyseblå, lyseblå/n*100,"%")
print("lysegrønn:",lysegrønn, lysegrønn/n*100,"%")
print("sum:", rødt+lyselilla+lilla+lyseblå+lysegrønn)
