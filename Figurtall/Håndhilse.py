print("Velkommen til H�ndHilsningSpillet")
restart = 1
while restart == 1:
    figureNum = int(input("Hvor mange folk skal håndhilse? "))
    blockamount = figureNum * (figureNum - 1) / 2
    print("Det ble",blockamount,"H�ndhilsnisnger")
    restart = input("vil du spille igjen? ")
    if restart == 'ja':
        restart = 1
    elif restart == 'nei':
        restart = 0