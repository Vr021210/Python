def length_converter(): #finished

    def from_feet_convert():
        
        def to_centimeter():
            result = Feet * 30.48
            formatted = f"{result:,}"
            print(f"{Feet} Feet is equal to {formatted} Centimeters")
        
        def to_meter():
            result = Feet * 30.48
            formatted = f"{result:,}"
            print(f"{Feet} Feet is equal to {formatted} Centimeters")
        
        def to_inches():
            result = Feet * 12
            formatted = f"{result:,}"
            print(f"{Feet} Feet is equal to {formatted} Inches")

        def to_yards():
            result = Feet / 3
            formatted = f"{result:,}"
            print(f"{Feet} Feet is equal to {formatted} Yards")

        print("1. Meter")
        print("2. Centimeter")
        print("3. Inches")
        print("4. Yards")
        UCT = input("What unit do you want to convert to? ").lower()
        Feet = float(input("How Many Feet? "))

        if UCT == '2' or UCT == 'centimeter':
            to_centimeter()
        
        elif UCT == '1' or UCT == 'meter':
            to_meter()
        
        elif UCT == '3' or UCT == 'inches':
            to_inches()
        
        elif UCT == '4' or UCT == 'yards':
            to_yards()
    
    def from_centimeter_convert():
        
        def to_inches():
            result = CentimeterAmount * 0.393700787
            formatted = f"{result:,}"
            print(f"{CentimeterAmount} Centimeters is equal to {formatted} Inches")
        
        def to_yards():
            result = CentimeterAmount * 0.010936133
            formatted = f"{result:,}"
            print(f"{CentimeterAmount} Centimeters is equal to {formatted} Yards")
        
        def to_feet():
            result = CentimeterAmount * 0.032808399
            formatted = f"{result:,}"
            print(f"{CentimeterAmount} Centimeters is equal to {formatted} Feet")

        def to_meter():
            result = CentimeterAmount / 100
            formatted = f"{result:,}"
            print(f"{CentimeterAmount} Centimeters is equal to {formatted} Meters")


        print("1. Yards")
        print("2. Inches")
        print("3. Feet")
        print("4. Meter")
        UCT = input("What unit do you want to convert to? ").lower()
        CentimeterAmount = float(input("How Many Centimeters? "))

        if UCT == '2' or UCT == 'inches':
            to_inches()
        
        elif UCT == '1' or UCT == 'yards':
            to_yards()
        
        elif UCT == '3' or UCT == 'feet':
            to_feet()
       
        elif UCT == '4' or UCT == 'meter':
            to_meter()
    
    def from_meter_convert():

        def to_inches():
            result = MeterAmount * 39.3700787
            formatted = f"{result:,}"
            print(f"{MeterAmount} Meters is equal to {formatted} Inches")

        def to_yards():
            result = MeterAmount * 1.0936133
            formatted = f"{result:,}"
            print(f"{MeterAmount} Meters is equal to {formatted} Yards")

        def to_feet():
            result = MeterAmount * 3.2808
            formatted = f"{result:,}"
            print(f"{MeterAmount} Meters is equal to {formatted} Feet")

        def to_centimeter():
            result = MeterAmount * 100
            formatted = f"{result:,}"
            print(f"{MeterAmount} Meters is equal to {formatted} Centimeters")

        print("1. Yards")
        print("2. Inches")
        print("3. Feet")
        print("4. Centimeters")
        UCT = input("What unit do you want to convert to? ").lower()
        MeterAmount = float(input("How Many Meters? "))

        if UCT == '2' or UCT == 'inches':
            to_inches()
       
        elif UCT == '1' or UCT == 'yards' or UCT == 'yard':
            to_yards()
       
        elif UCT == '3' or UCT ==  'feet':
            to_feet()
       
        elif UCT == '4' or UCT == 'centimeters' or UCT == 'centimeter':
            to_centimeter()

    def from_inches_convert():

        def to_centimeter():
            result = InchesAmount * 2.54
            formatted = f"{result:,}"
            print(f"{InchesAmount} Inches is equal to {formatted} Centimeters")

        def to_meter():
            result = InchesAmount * 0.0254
            formatted = f"{result:,}"
            print(f"{InchesAmount} Inches is equal to {formatted} Meters")

        def to_yards():
            result = InchesAmount * 0.0277777778
            formatted = f"{result:,}"
            print(f"{InchesAmount} Inches is equal to {formatted} Yards")

        def to_feet():
            result = InchesAmount / 12
            formatted = f"{result:,}"
            print(f"{InchesAmount} Inches is equal to {formatted} Feet")

        print("1. Centimeter")
        print("2. Meter")
        print("3. Yards")
        print("4. Feet")
        UCT = input("What unit do you want to convert to? ").lower()
        InchesAmount = float(input("How Many Inches? "))

        if UCT == '1' or UCT == 'centimeter':
           to_centimeter()
       
        elif UCT == '2' or UCT == 'meter' or UCT == 'meters' or UCT == 'm':
            to_meter()
       
        elif UCT == '3' or UCT == 'yards':
            to_yards()
      
        elif UCT == '4' or UCT == 'feet':
            to_feet()

    def from_yards_convert():

        def to_centimeter():
            result = YardsAmount * 91.44
            formatted = f"{result:,}"
            print(f"{YardsAmount} Inches is equal to {formatted} Feet")

        def to_meter():
            result = YardsAmount * 0.9144
            formatted = f"{result:,}"
            print(f"{YardsAmount} Yards is equal to {formatted} Meters")

        def to_feet():
            result = YardsAmount * 3
            formatted = f"{result:,}"
            print(f"{YardsAmount} Yards is equal to {formatted} Feet")

        def to_inches():
            result = YardsAmount * 36
            formatted = f"{result:,}"
            print(f"{YardsAmount} Yards is equal to {formatted} Inches")
        
        print("1. Centimeter")
        print("2. Meter")
        print("3. Feet")
        print("4. Inches")
        UCT = input("What unit do you want to convert to? ").lower()
        YardsAmount = float(input("How Many Yards? "))

        if UCT == '1' or UCT == 'centimeter' or UCT == 'cm':
            to_centimeter()
      
        elif UCT == '2' or UCT == 'meter' or UCT == 'm':
            to_meter()
     
        elif UCT == '3' or UCT == 'feet':
            to_feet()
     
        elif UCT == '4' or UCT == 'inches':
            to_inches()

    print("1. Feet")
    print("2. Centimeter")
    print("3. Meter")
    print("4. inches")
    print("5. yards")
        
    print("Remember to type in numbers")
    UCF = input("What unit do you want to convert from? ").lower()
    print("")
        
    if UCF == '1' or UCF == 'feet':
        from_feet_convert()
        
    elif UCF == '2' or UCF == 'centimeter' or UCF == 'cm':
        from_centimeter_convert()
        
    elif UCF == '3' or UCF == 'meter' or UCF == 'meter':
        from_meter_convert()
            
    elif UCF == '4' or UCF == 'inches':
        from_inches_convert()
            
    elif UCF == '5' or UCF == 'yards':
        from_yards_convert()

def temprature_converter(): # finished
    
    def celcius_full_block(): #finished
        
        def to_fahrenheit():
            result = (CelsiusAmount * 9 / 5) + 32
            formatted = f"{result:,}"
            print(f"{CelsiusAmount} Celsius is equal to {formatted} Fahrenheit")
        
        def to_kelvin():
            result = CelsiusAmount + 273.15
            formatted = f"{result:,}"
            print(f"{CelsiusAmount} Celsius is equal to {formatted} Kelvin")

        print("1. Fahrenheit")
        print("2. Kelvin")
        UCT = input("What unit do you want to convert to? ").lower()
        CelsiusAmount = float(input("How Many Celsius? "))

        if UCT == '1' or UCT == 'fahrenheit' :
            to_fahrenheit()
     
        elif UCT == '2' or UCT == 'kelvin':
            to_kelvin()
    
    def fahrenheit_full_block(): #finished
        
        def to_celcius():
            result = (FahrenheitAmount - 32) / 1.8
            formatted = f"{result:,}"
            print(f"{FahrenheitAmount} Fahrenheit is equal to {formatted} Celsius")
        
        def to_kelvin():
            result = (FahrenheitAmount - 32) * 5 / 9 + 273.15
            formatted = f"{result:,}"
            print(f"{FahrenheitAmount} Fahrenheit is equal to {formatted} Kelvin")
        
        print("1. Celsius")
        print("2. Kelvin")
        UCT = input("What unit do you want to convert to? ").lower()
        FahrenheitAmount = float(input("How Many Fahrenheit? "))

        if UCT == '1' or UCT == 'celcius':
            to_celcius()
    
        elif UCT == '2' or UCT == 'kelvin':
            to_kelvin()

    def kelvin_full_block(): #finished
        
        def to_celcius():
            result = KelvinAmount - 273.15
            formatted = f"{result:,}"
            print(f"{KelvinAmount} Kelvin is equal to {formatted} Celsius")
        
        def to_fahrenheit():
            result = (KelvinAmount - 273.15) * 9 / 5 + 32
            formatted = f"{result:,}"
            print(f"{KelvinAmount} Kelvin is equal to {formatted} Fahrenheit")
        
        print("1. Celsius")
        print("2. Fahrenheit")
        UCT = input("What unit do you want to convert to? ").lower()
        KelvinAmount = float(input("How Much Kelvin? "))

        if UCT == '1' or UCT == 'celcius':
            to_celcius()
     
        elif UCT == '2' or UCT == 'fahrenheit':
            to_fahrenheit

    def temprature_converter_full_action():
        print("1. Celsius")
        print("2. Fahrenheit")
        print("3. Kelvin")
        
        print("Remember to type in numbers")
        UCF = input("What unit do you want to convert from? ").lower()
        print("")
        
        if UCF == '1' or UCF == 'celcius':  
            celcius_full_block()

        if UCF == '2' or UCF == 'fahrenheit':  
            fahrenheit_full_block()

        if UCF == '3' or UCF == 'kelvin':  
            kelvin_full_block()
    
    temprature_converter_full_action()

def weight_converter(): #finished
    
    def from_kilo(): #finished
        
        def to_lbs():
            result = Kilos * 2.2
            formatted = f"{result:,}"
            print(f"{Kilos} Kilos is equal to {formatted} Pounds")
        
        def to_gram():
            result = Kilos * 1000
            formatted = f"{result:,}"
            print(f"{Kilos} Kilos is equal to {formatted} Grams")

        def to_ton():
            result = Kilos / 1000
            formatted = f"{result:,}"
            print(f"{Kilos} Kilos is equal to {formatted} Tons")

        def to_oz():
            result = Kilos * 35.27
            formatted = f"{result:,}"
            print(f"{Kilos} Kilos is equal to {formatted} Ounces")

        print("1. Pounds/Lbs")
        print("2. Grams")
        print("3. Tons")
        print("4. Ounces")
        UCT = input("What unit do you want to convert to? ").lower()
        Kilos = float(input("How many Kilos? "))

        if UCT == '1' or UCT == 'pounds' or UCT == 'lbs':
            to_lbs()
     
        elif UCT == '2' or UCT == 'grams' or UCT == 'g':
            to_gram()
      
        elif UCT == '3' or UCT == 'Tons' or UCT == 't':
            to_ton()
       
        elif UCT == '4' or UCT == 'ounces' or UCT == 'oz':
            to_oz()
    
    def from_lbs(): #finished
        
        def to_kilo():
            result = lbs * 0.45359237
            formatted = f"{result:,}"
            print(f"{lbs} Pounds is equal to {formatted} Kilograms")
        
        def to_grams():
            result = lbs * 453.59237
            formatted = f"{result:,}"
            print(f"{lbs} Pounds is equal to {formatted} Grams")
        
        def to_tons():
            result = lbs * 0.00045359237
            formatted = f"{result:,}"
            print(f"{lbs} Pounds is equal to {formatted} Tons")

        def to_oz():
            result = lbs * 16
            formatted = f"{result:,}"
            print(f"{lbs} Pounds is equal to {formatted} Ounces")



        print("1. Kilograms")
        print("2. Grams")
        print("3. Tons")
        print("4. Ounces")
        UCT = input("What unit do you want to convert to? ").lower()
        lbs = float(input("How Many Pounds/Lbs? "))

        if UCT == '1' or UCT == 'kilo' or UCT == 'kilograms' or UCT == 'kg':
            to_kilo()
        
        elif UCT == '2' or UCT == 'grams' or UCT == 'g':
            to_grams()
        
        elif UCT == '3' or UCT == 'tons' or UCT == 't':
            to_tons()
        
        elif UCT == '4' or UCT == 'ounces' or UCT == 'oz':
            to_oz()

    def from_grams(): #finished
        
        def to_kilo():
            result = grams / 1000
            formatted = f"{result:,}"
            print(f"{grams} Grams is equal to {formatted} Kilograms")
        
        def to_lbs():
            result = grams / 453.59237
            formatted = f"{result:,}"
            print(f"{grams} Grams is equal to {formatted} Pounds")

        def to_oz():
            result = grams / 28.34952
            formatted = f"{result:,}"
            print(f"{grams} Grams is equal to {formatted} Ounces")

        def to_tons():
            result = grams / 1_000_000
            formatted = f"{result:,}"
            print(f"{grams} Grams is equal to {formatted} Tons")
        
        print("1. Kilos")
        print("2. Pounds")
        print("3. Ounces")
        print("4. Tons")
        UCT = input("What unit do you want to convert to? ").lower()
        grams = float(input("How Many Grams? "))

        if UCT == '1' or UCT == 'kilo' or UCT == 'kilograms' or UCT == 'kg':
            to_kilo()
        
        elif UCT == '2' or UCT == 'pounds' or UCT == 'lbs':
            to_lbs()
        
        elif UCT == '3' or UCT == 'ounces' or UCT == 'oz':
            to_oz()
        
        elif UCT == '4' or UCT == 'tons' or UCT == 't':
            to_tons()        
    
    def from_tons(): #finished
        
        def to_kg():
            result = Tons * 1000
            formatted = f"{result:,}"
            print(f"{Tons} Tons is equal to {formatted} Kilograms")
    
        def to_grams(): 
            result = Tons * 1_000_000
            formatted = f"{result:,}"
            print(f"{Tons} Tons is equal to {formatted} Grams")
    
        def to_oz():   
            result = Tons * 35_273.96195
            formatted = f"{result:,}"
            print(f"{Tons} Tons is equal to {formatted} Ounces")
    
        def to_lbs():
            result = Tons * 2204.62262
            formatted = f"{result:,}"
            print(f"{Tons} Tons is equal to {formatted} Pounds")
    
    
    
        print("1. Kilograms")
        print("2. Grams")
        print("3. Ounces")
        print("4. Pounds")
        UCT = input("What unit do you want to convert to? ").lower()
        Tons = float(input("How Many Tons? "))

        if UCT == '1' or UCT == 'kilo' or UCT == 'kilograms' or UCT == 'kg' :
            to_kg()
        
        elif UCT == '2' or UCT == 'grams' or UCT == 'g':
            to_grams()
        
        elif UCT == '3' or UCT == 'ounces' or UCT == 'oz':
            to_oz()
       
        elif UCT == '4' or UCT == 'pounds' or UCT == 'lbs':
            to_lbs()
    
    def from_ounces(): #finished
        
        def to_kg():
            result = ounces / 35.274
            formatted = f"{result:,}"
            print(f"{ounces} Ounces is equal to {formatted} Kilograms")
    
        def to_grams():
            result = ounces * 28.34952
            formatted = f"{result:,}"
            print(f"{ounces} Ounces is equal to {formatted} Grams")
        
        def to_lbs():
            result = ounces / 16
            formatted = f"{result:,}"
            print(f"{ounces} Ounces is equal to {formatted} Pounds")
        
        def to_tons():
            result = ounces / 35_274
            formatted = f"{result:,}"
            print(f"{ounces} Ounces is equal to {formatted} Tons")
            
            
            
            
            
        print("1. Kilograms")
        print("2. Grams")
        print("3. Pounds")
        print("4. Tons")
        UCT = input("What unit do you want to convert to? ").lower()
        ounces = float(input("How Many Ounces? "))

        if UCT == '1' or UCT == 'kilo' or UCT == 'kilograms' or UCT == 'kg':
            to_kg()
        
        elif UCT == '2' or UCT == 'grams' or UCT == 'g':
            to_grams()
        
        elif UCT == '3' or UCT == 'pounds' or UCT == 'lbs':
            to_lbs()
        
        elif UCT == '4' or UCT == 'tons' or UCT == 't':
            to_tons()
            
            
    print("1. Kilograms")
    print("2. Pounds")
    print("3. Grams")
    print("4. Tons")
    print("5. Ounces")
    
    print("Remember to type in numbers")
    UCF = input("What unit do you want to convert from? ").lower()
    print("")
    
    if UCF == '1' or UCF == 'kilo' or UCF == 'kilograms' or UCF == 'kg':  
        from_kilo()
    
    
    if UCF == '2' or UCF == 'pounds' or UCF == 'lbs':  
        from_lbs()

    
    if UCF == '3' or UCF == 'grams' or UCF == 'g':  
        from_grams()

    
    if UCF == '4' or UCF == 'tons' or UCF == 't':  
        from_tons()


    if UCF == '5' or UCF == 'ounces' or UCF == 'oz':  
        from_ounces()

def currency_converter(): #Unfinished
   print("Currency Converter is not available at this time")
   time.sleep(1)

def energy_converter(): #finished
    def from_Watt(): # finished
        
        def to_KW(): #Formula
            result = Watt / 1000
            formatted = f"{result:,}"
            print(f"{Watt} Watt is equal to {formatted} KiloWatt")

        def to_MW(): #Formula
            result = Watt / 1000000
            formatted = f"{result:,}"
            print(f"{Watt} Watt is equal to {formatted} MegaWatt")

        def to_GW(): #Formula
            result = Watt / 1000000000
            formatted = f"{result:,}"
            print(f"{Watt} Watt is equal to {formatted} GigaWatt")

        def to_HP(): #Formula
            result = Watt * 0.00134102209
            formatted = f"{result:,}"
            print(f"{Watt} Watt is equal to {formatted} Horsepower")

        print("1. KiloWatt")
        print("2. MegaWatt")
        print("3. GigaWatt")
        print("4. HorsePower")
        UCT = input("What unit do you want to convert to? ").lower()
        Watt = float(input("How Many Watt? "))

        if UCT == '1' or UCT == 'kilowatt' or UCT == 'kw':
            to_KW()

        elif UCT == '2' or UCT == 'megawatt' or UCT == 'mw':
            to_MW()
        
        elif UCT == '3' or UCT == 'gigawatt' or UCT == 'gw':
            to_GW()
        
        elif UCT == '4' or UCT == 'horsepower' or UCT == 'hp':
            to_HP()

    def From_KiloWatt(): #finished
            
            def to_watt():
                result = kilowatt * 1000
                formatted = f"{result:,}"
                print(f"{kilowatt} KiloWatt is equal to {formatted} watt")

            def to_MW():
                result = kilowatt / 1000
                formatted = f"{result:,}"
                print(f"{kilowatt} KiloWatt is equal to {formatted} megawatt")

            def to_GW():
                result = kilowatt / 1000000
                formatted = f"{result:,}"
                print(f"{kilowatt} KiloWatt is equal to {formatted} gigawatt")

            def to_hp():
                result = kilowatt * 1.34102209
                formatted = f"{result:,}"
                print(f"{kilowatt} KiloWatt is equal to {formatted} horsepower")


            print("1. Watt")
            print("2. MegaWatt")
            print("3. GigaWatt")
            print("4. HorsePower")
            UCT = input("What unit do you want to convert to? ").lower()
            kilowatt = float(input("How Many KiloWatt? "))

            if UCT == '1' or UCT == 'watt' or UCT == 'watt':
                to_watt()

            elif UCT == '2' or UCT == 'megawatt' or UCT == 'mw':
                to_MW()
            
            elif UCT == '3' or UCT == 'gigawatt' or UCT == 'gw':
                to_GW()
            
            elif UCT == '4' or UCT == 'horsepower' or UCT == 'hp':
                to_hp()

    def From_MegaWatt(): #finished           
            def to_watt():
                result = megawatt * 1000000
                formatted = f"{result:,}"
                print(f"{megawatt} MegaWatt is equal to {formatted} Watt")
            
            def to_kilowatt():
                result = megawatt / 1000
                formatted = f"{result:,}"
                print(f"{megawatt} MegaWatt is equal to {formatted} KiloWatt")
            
            def to_gigawatt():
                result = megawatt / 1000
                formatted = f"{result:,}"
                print(f"{megawatt} MegaWatt is equal to {formatted} GigaWatt")
            
            def to_hp():    
                result = megawatt * 1341.02209
                formatted = f"{result:,}"
                print(f"{megawatt} Megawatt is equal to {formatted} Horsepower")

            print("1. Watt")
            print("2. KiloWatt")
            print("3. GigaWatt")
            print("4. HorsePower")
            UCT = input("What unit do you want to convert to? ").lower()
            megawatt = float(input("How Many MegaWatt? "))

            if UCT == '1' or UCT == 'watt' or UCT == 'w':
                to_watt()

            elif UCT == '2' or UCT == 'kilowatt' or UCT == 'kw':
                to_kilowatt()
            
            elif UCT == '3' or UCT == 'gigawatt' or UCT == 'gw':
                to_gigawatt()
            
            elif UCT == '4' or UCT == 'horsepower' or UCT == 'hp':
                to_hp()
            
    def From_GigaWatt(): #finished
            
            def to_watt():
                result = gigawatt * 1000000000
                formatted = f"{result:,}"
                print(f"{gigawatt} GigaWatt is equal to {formatted} Watt")

            def to_kilowatt():
                result = gigawatt * 1000000
                formatted = f"{result:,}"
                print(f"{gigawatt} GigaWatt is equal to {formatted} KiloWatt")

            def to_megawatt():
                result = gigawatt * 1000
                formatted = f"{result:,}"
                print(f"{gigawatt} GigaWatt is equal to {formatted} MegaWatt")

            def to_hp():
                result = gigawatt * 1341022.09
                formatted = f"{result:,}"
                print(f"{gigawatt} GigaWatt is equal to {formatted} HorsePower")
            
            print("1. Watt")
            print("2. KiloWatt")
            print("3. MegaWatt")
            print("4. HorsePower")
            UCT = input("What unit do you want to convert to? ").lower()
            gigawatt = float(input("How Many GigaWatt? "))

            if UCT == '1' or UCT == 'watt' or UCT == 'w':
                to_watt()

            elif UCT == '2' or UCT == 'kilowatt' or UCT == 'kw':
                to_kilowatt()
            
            elif UCT == '3' or UCT == 'meagwatt' or UCT == 'mw':
                to_megawatt()
            
            elif UCT == '4' or UCT == 'horsepower' or UCT == 'hp':
                to_hp()
            
    def from_HorsePower(): #finished  
            
            def to_watt():
                result = hp * 745.699872
                formatted = f"{result:,}"
                print(f"{hp} HorsePower is equal to {formatted} Watt")

            def to_kilowatt():
                result = hp * 0.745699872
                formatted = f"{result:,}"
                print(f"{hp} HorsePower is equal to {formatted} KiloWatt")

            def to_megawatt():
                result = hp * 0.000745699872
                formatted = f"{result:,}"
                print(f"{hp} HorsePower is equal to {formatted} MegaWatt")

            def to_gigawatt():
                result = hp * 0.000745699872 / 1000
                formatted = f"{result:,}"
                print(f"{hp} HorsePower is equal to {formatted} MegaWatt")
        
                
            
            print("1. Watt")
            print("2. KiloWatt")
            print("3. MegaWatt")
            print("4. GigaWatt")
            UCT = input("What unit do you want to convert to? ").lower()
            hp = float(input("How Many HorsePower? "))

            if UCT == '1' or UCT == 'watt' or UCT == 'w':
                to_watt()

            elif UCT == '2' or UCT == 'kilowatt' or UCT == 'kw':
                to_kilowatt()
            
            elif UCT == '3' or UCT == 'meagwatt' or UCT == 'mw':
                to_megawatt()
            
            elif UCT == '4' or UCT == 'gigawatt' or UCT == 'gw':
                to_gigawatt()
    


    print("1. Watt")
    print("2. KiloWatt")
    print("3. MegaWatt")
    print("4. GigaWatt")
    print("5. Horsepower")

    print("")
    print("Remember to type in numbers")
    UCF = input("What unit do you want to convert from? ").lower()
    print("")

    if UCF == '1' or UCF == 'watt' or UCF == 'w':
        from_Watt()
    
    elif UCF == '2' or UCF == 'kilowatt' or UCF == 'kw':
        From_KiloWatt()

    elif UCF == '3' or UCF == 'megawatt' or UCF == 'mw':
        From_MegaWatt()
    
    elif UCF == '4' or UCF == 'gigawatt' or UCF == 'gw':       
        From_GigaWatt()

    elif UCF == '5' or 'horsepower' or UCF == 'hp' or UCF == 'horse':
        from_HorsePower()


import time

restart = 1

while restart == 1:
        print("1. Length Converter")
        print("2. Temprature Converter")
        print("3. Weight Converter")
        print("4. Currency Converter")
        print("5. Energy Converter")
    
        CT = input("What Unit Type do you want to convert? ").lower() #CT is short for ConvertType
        print("")
        
        if CT == '1' or CT == 'length' or CT == 'length converter':
            length_converter()
            
        elif CT == '2' or CT == 'temprature' or CT == 'temp' or CT == 'temprature converter':
            temprature_converter()
                
        elif CT == '3' or CT == 'weight' or CT == 'weight converter':
            weight_converter()
        
        elif CT == '4' or CT == 'currency converter' or CT == 'money' or CT == 'currency':
            currency_converter()

        elif CT == '5' or CT == 'energy':
            energy_converter()
        
        else:
            print("Invalid Input. Exiting Program")
            break
    
        restart = input("Do You Want To Do Another Calculation? Yes/No ").lower()
        if restart == 'yes':
            restart = 1
            print("Ok!")
            time.sleep(0.4)
            
        elif restart == 'no':
            print("Thanks For Using My Program")
            restart = 0
        else:
            print("Invalid Input. Exiting Program")
            break

