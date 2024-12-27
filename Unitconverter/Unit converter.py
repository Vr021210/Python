restart = 1

while restart == 1:
    # The Unit everything is converted from
    print("0. Feet")
    print("1. Centimeter")
    print("2. Meter")
    print("3. Inches")
    print("4. Yards")
    print("5. Celsius")
    print("6. Fahrenheit")
    print("7. Kelvin")
    print("8. Kilograms")
    print("9. Pounds")
    print("10. Grams")
    print("11. Tons")
    print("12. Ounces")

    print("Remember to type in numbers")
    UnitConvertFrom = input("What unit do you want to convert from? ")

    # Feet block
    if UnitConvertFrom == '0':  
        print("1. Meter")
        print("2. Centimeter")
        print("3. Inches")
        print("4. Yards")
        UnitConvertTo = input("What unit do you want to convert to? ")
        Feet = float(input("How Many Feet? "))

        if UnitConvertTo == '2':
            result = Feet * 30.48
            formatted = f"{result:,}"
            print(f"{Feet} Feet is equal to {formatted} Centimeters")
        elif UnitConvertTo == '1':
            result = Feet * 0.3048
            formatted = f"{result:,}"
            print(f"{Feet} Feet is equal to {formatted} Meters")
        elif UnitConvertTo == '3':
            result = Feet * 12
            formatted = f"{result:,}"
            print(f"{Feet} Feet is equal to {formatted} Inches")
        elif UnitConvertTo == '4':
            result = Feet / 3
            formatted = f"{result:,}"
            print(f"{Feet} Feet is equal to {formatted} Yards")

    # Centimeters block
    if UnitConvertFrom == '1':  
        print("1. Yards")
        print("2. Inches")
        print("3. Feet")
        print("4. Meters")
        UnitConvertTo = input("What unit do you want to convert to? ")
        CentimeterAmount = float(input("How Many Centimeters? "))

        if UnitConvertTo == '2':
            result = CentimeterAmount * 0.393700787
            formatted = f"{result:,}"
            print(f"{CentimeterAmount} Centimeters is equal to {formatted} Inches")
        elif UnitConvertTo == '1':
            result = CentimeterAmount * 0.010936133
            formatted = f"{result:,}"
            print(f"{CentimeterAmount} Centimeters is equal to {formatted} Yards")
        elif UnitConvertTo == '3':
            result = CentimeterAmount * 0.032808399
            formatted = f"{result:,}"
            print(f"{CentimeterAmount} Centimeters is equal to {formatted} Feet")
        elif UnitConvertTo == '4':
            result = CentimeterAmount / 100
            formatted = f"{result:,}"
            print(f"{CentimeterAmount} Centimeters is equal to {formatted} Meters")

    # Meters block
    if UnitConvertFrom == '2':  
        print("1. Yards")
        print("2. Inches")
        print("3. Feet")
        print("4. Centimeters")
        UnitConvertTo = input("What unit do you want to convert to? ")
        MeterAmount = float(input("How Many Meters? "))

        if UnitConvertTo == '2':
            result = MeterAmount * 39.3700787
            formatted = f"{result:,}"
            print(f"{MeterAmount} Meters is equal to {formatted} Inches")
        elif UnitConvertTo == '1':
            result = MeterAmount * 1.0936133
            formatted = f"{result:,}"
            print(f"{MeterAmount} Meters is equal to {formatted} Yards")
        elif UnitConvertTo == '3':
            result = MeterAmount * 3.2808
            formatted = f"{result:,}"
            print(f"{MeterAmount} Meters is equal to {formatted} Feet")
        elif UnitConvertTo == '4':
            result = MeterAmount * 100
            formatted = f"{result:,}"
            print(f"{MeterAmount} Meters is equal to {formatted} Centimeters")

    # Inches block
    if UnitConvertFrom == '3':  
        print("1. Centimeter")
        print("2. Meter")
        print("3. Yards")
        print("4. Feet")
        UnitConvertTo = input("What unit do you want to convert to? ")
        InchesAmount = float(input("How Many Inches? "))

        if UnitConvertTo == '1':
            result = InchesAmount * 2.54
            formatted = f"{result:,}"
            print(f"{InchesAmount} Inches is equal to {formatted} Centimeters")
        elif UnitConvertTo == '2':
            result = InchesAmount * 0.0254
            formatted = f"{result:,}"
            print(f"{InchesAmount} Inches is equal to {formatted} Meters")
        elif UnitConvertTo == '3':
            result = InchesAmount * 0.0277777778
            formatted = f"{result:,}"
            print(f"{InchesAmount} Inches is equal to {formatted} Yards")
        elif UnitConvertTo == '4':
            result = InchesAmount / 12
            formatted = f"{result:,}"
            print(f"{InchesAmount} Inches is equal to {formatted} Feet")

    # Yards block
    if UnitConvertFrom == '4':  
        print("1. Centimeter")
        print("2. Meter")
        print("3. Feet")
        print("4. Inches")
        UnitConvertTo = input("What unit do you want to convert to? ")
        YardsAmount = float(input("How Many Yards? "))

        if UnitConvertTo == '1':
            result = YardsAmount * 91.44
            formatted = f"{result:,}"
            print(f"{YardsAmount} Yards is equal to {formatted} Centimeters")
        elif UnitConvertTo == '2':
            result = YardsAmount * 0.9144
            formatted = f"{result:,}"
            print(f"{YardsAmount} Yards is equal to {formatted} Meters")
        elif UnitConvertTo == '3':
            result = YardsAmount * 3
            formatted = f"{result:,}"
            print(f"{YardsAmount} Yards is equal to {formatted} Feet")
        elif UnitConvertTo == '4':
            result = YardsAmount * 36
            formatted = f"{result:,}"
            print(f"{YardsAmount} Yards is equal to {formatted} Inches")

    # Celsius block
    if UnitConvertFrom == '5':  
        print("1. Fahrenheit")
        print("2. Kelvin")
        UnitConvertTo = input("What unit do you want to convert to? ")
        CelsiusAmount = float(input("How Many Celsius? "))

        if UnitConvertTo == '1':
            result = (CelsiusAmount * 9 / 5) + 32
            formatted = f"{result:,}"
            print(f"{CelsiusAmount} Celsius is equal to {formatted} Fahrenheit")
        elif UnitConvertTo == '2':
            result = CelsiusAmount + 273.15
            formatted = f"{result:,}"
            print(f"{CelsiusAmount} Celsius is equal to {formatted} Kelvin")

    # Fahrenheit block
    if UnitConvertFrom == '6':  
        print("1. Celsius")
        print("2. Kelvin")
        UnitConvertTo = input("What unit do you want to convert to? ")
        FahrenheitAmount = float(input("How Many Fahrenheit? "))

        if UnitConvertTo == '1':
            result = (FahrenheitAmount - 32) / 1.8
            formatted = f"{result:,}"
            print(f"{FahrenheitAmount} Fahrenheit is equal to {formatted} Celsius")
        elif UnitConvertTo == '2':
            result = (FahrenheitAmount - 32) * 5 / 9 + 273.15
            formatted = f"{result:,}"
            print(f"{FahrenheitAmount} Fahrenheit is equal to {formatted} Kelvin")

    # Kelvin block
    if UnitConvertFrom == '7':  
        print("1. Celsius")
        print("2. Fahrenheit")
        UnitConvertTo = input("What unit do you want to convert to? ")
        KelvinAmount = float(input("How Much Kelvin? "))

        if UnitConvertTo == '1':
            result = KelvinAmount - 273.15
            formatted = f"{result:,}"
            print(f"{KelvinAmount} Kelvin is equal to {formatted} Celsius")
        elif UnitConvertTo == '2':
            result = (KelvinAmount - 273.15) * 9 / 5 + 32
            formatted = f"{result:,}"
            print(f"{KelvinAmount} Kelvin is equal to {formatted} Fahrenheit")

    # Kilograms block
    if UnitConvertFrom == '8':  
        print("1. Pounds/Lbs")
        print("2. Grams")
        print("3. Tons")
        print("4. Ounces")
        UnitConvertTo = input("What unit do you want to convert to? ")
        Kilos = float(input("How many Kilos? "))

        if UnitConvertTo == '1':
            result = Kilos * 2.2
            formatted = f"{result:,}"
            print(f"{Kilos} Kilos is equal to {formatted} Pounds")
        elif UnitConvertTo == '2':
            result = Kilos * 1000
            formatted = f"{result:,}"
            print(f"{Kilos} Kilos is equal to {formatted} Grams")
        elif UnitConvertTo == '3':
            result = Kilos / 1000
            formatted = f"{result:,}"
            print(f"{Kilos} Kilos is equal to {formatted} Tons")
        elif UnitConvertTo == '4':
            result = Kilos * 35.27
            formatted = f"{result:,}"
            print(f"{Kilos} Kilos is equal to {formatted} Ounces")

    # Pounds block
    if UnitConvertFrom == '9':  
        print("1. Kilos")
        print("2. Grams")
        print("3. Tons")
        print("4. Ounces")
        UnitConvertTo = input("What unit do you want to convert to? ")
        lbs = float(input("How Many Pounds/Lbs? "))

        if UnitConvertTo == '1':
            result = lbs * 0.45359237
            formatted = f"{result:,}"
            print(f"{lbs} Pounds is equal to {formatted} Kilograms")
        elif UnitConvertTo == '2':
            result = lbs * 453.59237
            formatted = f"{result:,}"
            print(f"{lbs} Pounds is equal to {formatted} Grams")
        elif UnitConvertTo == '3':
            result = lbs * 0.00045359237
            formatted = f"{result:,}"
            print(f"{lbs} Pounds is equal to {formatted} Tons")
        elif UnitConvertTo == '4':
            result = lbs * 16
            formatted = f"{result:,}"
            print(f"{lbs} Pounds is equal to {formatted} Ounces")

    # Grams block
    if UnitConvertFrom == '10':  
        print("1. Kilos")
        print("2. Pounds")
        print("3. Ounces")
        print("4. Tons")
        UnitConvertTo = input("What unit do you want to convert to? ")
        grams = float(input("How Many Grams? "))

        if UnitConvertTo == '1':
            result = grams / 1000
            formatted = f"{result:,}"
            print(f"{grams} Grams is equal to {formatted} Kilograms")
        elif UnitConvertTo == '2':
            result = grams / 453.59237
            formatted = f"{result:,}"
            print(f"{grams} Grams is equal to {formatted} Pounds")
        elif UnitConvertTo == '3':
            result = grams / 28.34952
            formatted = f"{result:,}"
            print(f"{grams} Grams is equal to {formatted} Ounces")
        elif UnitConvertTo == '4':
            result = grams / 1_000_000
            formatted = f"{result:,}"
            print(f"{grams} Grams is equal to {formatted} Tons")

    # Tons block
    if UnitConvertFrom == '11':  
        print("1. Kilograms")
        print("2. Grams")
        print("3. Ounces")
        print("4. Pounds")
        UnitConvertTo = input("What unit do you want to convert to? ")
        Tons = float(input("How Many Tons? "))

        if UnitConvertTo == '1':
            result = Tons * 1000
            formatted = f"{result:,}"
            print(f"{Tons} Tons is equal to {formatted} Kilograms")
        elif UnitConvertTo == '2':
            result = Tons * 1_000_000
            formatted = f"{result:,}"
            print(f"{Tons} Tons is equal to {formatted} Grams")
        elif UnitConvertTo == '3':
            result = Tons * 35_273.96195
            formatted = f"{result:,}"
            print(f"{Tons} Tons is equal to {formatted} Ounces")
        elif UnitConvertTo == '4':
            result = Tons * 2204.62262
            formatted = f"{result:,}"
            print(f"{Tons} Tons is equal to {formatted} Pounds")

    # Ounces block
    if UnitConvertFrom == '12':  
        print("1. Kilograms")
        print("2. Grams")
        print("3. Pounds")
        print("4. Tons")
        UnitConvertTo = input("What unit do you want to convert to? ")
        ounces = float(input("How Many Ounces? "))

        if UnitConvertTo == '1':
            result = ounces / 35.274
            formatted = f"{result:,}"
            print(f"{ounces} Ounces is equal to {formatted} Kilograms")
        elif UnitConvertTo == '2':
            result = ounces * 28.34952
            formatted = f"{result:,}"
            print(f"{ounces} Ounces is equal to {formatted} Grams")
        elif UnitConvertTo == '3':
            result = ounces / 16
            formatted = f"{result:,}"
            print(f"{ounces} Ounces is equal to {formatted} Pounds")
        elif UnitConvertTo == '4':
            result = ounces / 35_274
            formatted = f"{result:,}"
            print(f"{ounces} Ounces is equal to {formatted} Tons")

    restart = input("Do You Want To Do Another Calculation? Yes/No (1/3) ")
    if restart == 'Yes':
        restart = 1
    elif restart == 'No':
        print("Thanks For Using My Program")
        restart = 0
    else:
        print("Please Enter A Valid Input!")
        restart = input("Do You Want To Do Another Calculation? Yes/No (2/3) ")
    if restart == 'Yes':
        restart = 1
    elif restart == 'No':
        print("Thanks For Using My Program")
        restart = 0
    else:
        print("Please Enter A Valid Input!")
        restart = input("Do You Want To Do Another Calculation? Yes/No (3/3) ")
    if restart == 'Yes':
        restart = 1
    elif restart == 'No':
        print("Thanks For Using My Program")
        restart = 0
    else:
        print("You Have Used Up All Your Attempts, The Program Has Automatically Ended")


