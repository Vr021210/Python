from pylab import randint
n = 100
konge = 0
ikkekonge = 0

for i in range(n):
   kortstokk = randint(1,14)
   if kortstokk == 1:
       konge = konge + 1 
   else: 
        ikkekonge = ikkekonge + 1 
     
print("konger:", konge, konge/n)
print("ikke-konger:", ikkekonge, ikkekonge/n)
