from pylab import time

correctanswer = 0
Wronganswers = 0

print("1. Bolsjevikene")
print("2. Mensjevikene")
print("3. Russiske Mafia")
Q1 = input("Hvem vant borgerkrigen i russland? ")

if Q1 == '1':
    print("Checking your answer......")
    time.sleep(2)
    print ("Well done Lets move on to the next question")
    correctanswer = correctanswer + 1
    time.sleep(1)
    print(Wronganswers, "Wrong Answers")
    print(correctanswer, "Correct answers")
    print("")
else:
    print("Checking your answer......")
    time.sleep(2)
    print ("Wrong, Better luck next time")
    Wronganswers = Wronganswers + 1
    time.sleep(1)
    print(Wronganswers, "Wrong Answers")
    print(correctanswer, "Correct answers")
    print("")

time. sleep(2)
print("Hint: Bruk den gregoriske kalenderen")
print("1. Mars")
print("2. Februar")
print("3. Mai")
Q2 = input("Når var Februar Revolusjonen? ")

if Q2 == '1':
    print("Checking your answers......")
    time.sleep(2)
    print("Well Done, Lets move on to the next question")
    correctanswer = correctanswer + 1
    time.sleep(1)
    print(correctanswer, "Correct answers")
    print(Wronganswers, "Wrong Answers")
    print("")

else:
    print("Checking your anwers.....")
    time.sleep(2)
    print("Wrong, better luck next time")
    Wronganswers = Wronganswers + 1 
    time.sleep(1)
    print(Wronganswers, "Wrong Answers")
    print(correctanswer, "Correct answers")
    print("")