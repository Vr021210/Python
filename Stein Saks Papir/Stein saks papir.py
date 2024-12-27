from pylab import randint
from pylab import time
EST = 1
rock = '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''

paper = '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    '''

scissors = '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''
    
gun = '''
    
 +--^----------,--------,-----,--------^-,
 | |||||||||   `--------'     |          O
 `+---------------------------^----------|
   `\_,---------,---------,--------------'
     / XXXXXX /'|       /'
    / XXXXXX /  `\    /'
   / XXXXXX /`-------'
  / XXXXXX /
 / XXXXXX /
(________(                
 `------'   
           
           '''           
        
win = "You Win!"
  
lose = "You Lose!"
  
tie = "its A Tie!"
  
death = '''
 ____       _           _     ____  _          _   _ 
|  _ \ ___ | |__   ___ | |_  |  _ \(_) ___  __| | | |
| |_) / _ \| '_ \ / _ \| __| | | | | |/ _ \/ _` | | |
|  _ < (_) | |_) | (_) | |_  | |_| | |  __/ (_| | |_|
|_| \_\___/|_.__/ \___/ \__| |____/|_|\___|\__,_| (_)
















'''

si = "Do You Want To Have Another go?"
 
TakkForAtDuSpilte = "Thanks For Playing!"

while EST == True:
                    
    PHånd = input("1 for Stein, 2 for Saks, 3 for papir ")
    RHånd = randint(1,4)
    
    # 1 = Stein
    # 2 = Saks
    # 3 = Papir
    
    if PHånd == '1' and RHånd == 1:
        print(rock)
        print("Checking results......")
        time.sleep(1)
        print("")
        print("Computer chose", RHånd)
        print(rock)
        time.sleep(0.5)
        print(tie)
        time.sleep(1)
        EST = input("Do You Want To Have Another Go?")
        
    elif PHånd == '1' and RHånd == 2:
        print(rock)
        print("Checking results......")
        time.sleep(1)
        print("")
        print("Computer chose", RHånd)
        print(scissors)
        time.sleep(0.5)
        print(win)
        time.sleep(1)
        EST = input(si)
        
    elif PHånd == '1' and RHånd == 3:
        print(rock)
        print("Checking results......")
        time.sleep(1)
        print("")
        print("Computer chose", RHånd)
        print(paper)
        time.sleep(0.5)
        print(lose)
        time.sleep(1)
        EST = input(si)
    
    elif PHånd == '2' and RHånd == 1:
        print(scissors)
        print("Checking results......")
        time.sleep(1)
        print("")
        print("Computer chose", RHånd)
        print(rock)
        time.sleep(0.5)
        print(lose)
        time.sleep(1)
        EST = input(si)
        
    elif PHånd == '2' and RHånd == 2:
        print(scissors)
        print("Checking results......")
        time.sleep(1)
        print("")
        print("Computer chose", RHånd)
        print(scissors)
        time.sleep(0.5)
        print(tie)
        time.sleep(1)
        EST = input(si)
        
    elif PHånd == '2' and RHånd == 3:
        print(scissors)
        print("Checking results......")
        time.sleep(1)
        print("")
        print("Computer chose", RHånd)
        print(paper)
        time.sleep(0.5)
        print(win)
        time.sleep(1)
        EST = input(si)
        
    elif PHånd == '3' and RHånd == 1:
        print(paper)
        print("Checking results......")
        time.sleep(1)
        print("")
        print("Computer chose", RHånd)
        print(rock)
        time.sleep(0.5)
        print(win)
        time.sleep(1)
        EST = input(si)
        
    elif PHånd == '3' and RHånd == 2:
        print(paper)
        print("Checking results......")
        time.sleep(1)
        print("")
        print("Computer chose", RHånd)
        print(scissors)
        time.sleep(0.5)
        print(lose)
        time.sleep(1)
        EST = input(si)
        
    elif PHånd == '3' and RHånd == 3:
        print(paper)
        print("Checking results......")
        time.sleep(1)
        print("")
        print("Computer chose", RHånd)
        print(paper)
        time.sleep(0.5)
        print(tie)
        time.sleep(1)
        EST = input(si)
        
    elif PHånd == '4' and RHånd == 1:
        print(gun)
        print("Checking results......")
        time.sleep(1)
        print("")
        print("Computer chose", RHånd)
        print(rock)
        time.sleep(1)
        print(death)
        time.sleep(1)
        print(win)
        EST = False
        
    elif PHånd == '4' and RHånd == 2:
        print(gun)
        print("Checking results......")
        time.sleep(1)
        print("")
        print("Computer chose", RHånd)
        print(scissors)
        time.sleep(1)
        print(death)
        time.sleep(1)
        print(win)
        EST = False
        
    elif PHånd == '4' and RHånd == 3:
        print(gun)
        print("Checking results......")
        time.sleep(1)
        print("")
        print("Computer chose", RHånd)
        print(paper)
        time.sleep(1)
        print(death)
        time.sleep(1)
        print(win)
        EST = False
    

    if EST == 'yes':
        EST = True
        print("laster inn på nytt....")
        time.sleep(2)
        print("Ferdig innlastet!")
        time.sleep(1)
    else:
        time.sleep(1)
        EST = False
        print(TakkForAtDuSpilte)