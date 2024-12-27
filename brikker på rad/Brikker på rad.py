restart = 1
while restart == 1:
    antall_forskjellige_brikker = int(input("Hvor mange forskjellige farger vil du ha? "))
    antall_brikker_på_rad = int(input("Hvor mange brikker på rad? "))
    print("Det er 1 /",antall_forskjellige_brikker ** antall_brikker_på_rad, "sjanse for å få",antall_brikker_på_rad,"av den samme brikken på rad")
    restrt = int(input("vil du gjøre det igjen? "))
    if restrt == 'ja':
        restart = 1
    else:
        restart = 0
        print("Takk for at du spilte")