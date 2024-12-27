from pylab import randint
n = 100
ener = 0
toer = 0
treer = 0
firer = 0
femmer = 0
sekser = 0

for i in range(n):
   terning = randint(1,7)
   if terning == 1:
       ener = ener + 1 
   elif terning == 2:
        toer = toer + 1 
   elif terning == 3:
       treer = treer + 1  
   elif terning == 4:
       firer = firer + 1  
   elif terning == 5:
       femmer = femmer
   elif terning == 6:
       sekser = sekser + 1 
       
print("enere:", ener, ener/n*100,"%")
print("toere:", toer, toer/n*100,"%")
print("treere:", treer,treer/n*100,"%")
print("firere:",firer, firer/n*100,"%")
print("femmere:",femmer,femmer/n*100,"%")
print("seksere:",sekser,sekser/n*100,"%")