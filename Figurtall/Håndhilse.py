print("Velkommen til HåndHilsningSpillet")
restart = 1
while restart == 1:
    figureNum = int(input("Hvor mange folk skal hÃ¥ndhilse? "))
    blockamount = figureNum * (figureNum - 1) / 2
    print("Det ble",blockamount,"Håndhilsnisnger")
    restart = input("vil du spille igjen? ")
    if restart == 'ja':
        restart = 1
    elif restart == 'nei':
        restart = 0