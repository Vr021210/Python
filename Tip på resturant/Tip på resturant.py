import time
Kostnad = int(input("Hvor mye Koster det? "))
Tip = int(input("hvor mange prosent hvil du gi? "))

# Calculate tip as a percentage of the cost
TipAmount = Kostnad * (Tip / 100)

# Output the result
print(Tip, "prosent av", Kostnad, "er", TipAmount)
time.sleep(1)
print("du må betale", Kostnad + TipAmount)
regning_split = input("vil du splitte regningen? ")
total = Kostnad + TipAmount
if regning_split == 'ja':
    time.sleep(1)
    antall_mennesker = int(input("Hvor mange personer? "))
    print(total / antall_mennesker,"per person")
else:
    print("takk for at du spilte.")
    
    

