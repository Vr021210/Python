print("Velkommen til KvadratTall")
restart = 1
while restart == 1:
    figureNum = int(input("Hvilken figur vil du vite hvor mange blokker det blir? "))
    blockamount = figureNum * (figureNum)
    print("Det ble",blockamount,"Blokker")
    restart = input("vil du spille igjen? ")
    if restart == 'ja':
        restart = 1
    elif restart == 'nei':
        restart = 0