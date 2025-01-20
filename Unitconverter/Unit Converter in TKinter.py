import tkinter as tk
import customtkinter as ctk
import threading
do = 1


conversion_factors = {
    "Length": {
        "Meters": 1,
        "Kilometers": 1000,
        "Centimeters": 0.01,
        "Millimeters": 0.001,
        "Inches": 0.0254,
        "Feet": 0.3048,
        "Yards": 0.9144,
        "Miles": 1609.34, 
    },
    "Energy": {
        "Joules": 1,
        "Kilojoules": 1000,
        "Calories": 4.184,
        "Kilocalories": 4184,
        "Watt-hours": 3600,
        "Kilowatt-hours": 3600000,
    },
    "Weight": {
        "Grams": 1,
        "Kilograms": 1000,
        "Milligrams": 0.001,
        "Pounds": 453.592,
        "Ounces": 28.3495,
        "Metric Tons": 1000000,  
        "Megatons": 1000000000000,
    },
    "Temperature": {
        "Celsius to Fahrenheit": lambda c: (c * 9/5) + 32,
        "Fahrenheit to Celsius": lambda f: (f - 32) * 5/9,
        "Celsius to Kelvin": lambda c: c + 273.15,
        "Kelvin to Celsius": lambda k: k - 273.15,
        "Fahrenheit to Kelvin": lambda f: (f - 32) * 5/9 + 273.15,
        "Kelvin to Fahrenheit": lambda k: (k - 273.15) * 9/5 + 32,
    },
}


def update_options(*args):
    selected_option = selected_option_DropdownUnitTypeOptions.get()

    # Clear existing options
    menu_from = FromUnitDropDown["menu"]
    menu_from.delete(0, "end")
    
    menu_to = ToUnitDropDown["menu"]
    menu_to.delete(0, "end")
    
    if selected_option == "Length":
        units = list(conversion_factors["Length"].keys())
    elif selected_option == "Weight":
        units = list(conversion_factors["Weight"].keys())
    elif selected_option == "Temperature":
        units = ["Celsius", "Fahrenheit", "Kelvin"]
    elif selected_option == "Energy":
        units = list(conversion_factors["Energy"].keys())
    else:
        units = []  

    for unit in units:
        menu_from.add_command(label=unit, command=tk._setit(selected_option_FromUnitDropDown, unit))
        menu_to.add_command(label=unit, command=tk._setit(selected_option_ToUnitDropDown, unit))


def convert():
    try:
        # Get input value
        value = float(number1.get())  # Get the number to convert
        
        # Get selected units
        from_unit = selected_option_FromUnitDropDown.get()
        to_unit = selected_option_ToUnitDropDown.get()

        # Get the unit type (Length, Weight, etc.)
        unit_type = selected_option_DropdownUnitTypeOptions.get()

        # Conversion logic
        if unit_type == "Length":
            # Convert length (convert to meters first, then to the desired unit)
            value_in_meters = value * conversion_factors["Length"][from_unit]
            result = value_in_meters / conversion_factors["Length"][to_unit]
            formatted = f"{result:,}"
        elif unit_type == "Weight":
            # Convert weight (convert to grams first, then to the desired unit)
            value_in_grams = value * conversion_factors["Weight"][from_unit]
            result = value_in_grams / conversion_factors["Weight"][to_unit]
            formatted = f"{result:,}"
        elif unit_type == "Temperature":
            # Convert temperature using the appropriate function
            result = conversion_factors["Temperature"][from_unit + " to " + to_unit](value)
        elif unit_type == "Energy":
            # Convert energy (convert to joules first, then to the desired unit)
            value_in_joules = value * conversion_factors["Energy"][from_unit]
            result = value_in_joules / conversion_factors["Energy"][to_unit]
            formatted = f"{result:,}"
        else:
            result = "Invalid conversion type"

        # Update the result label
        convertedlabel.config(text=f"Converted: {formatted}")

    except ValueError:
        convertedlabel.config(text="Invalid input! Please enter a number.")

# Initialize the Tkinter window
root = tk.Tk()

root.geometry("500x500")
root.title("Unit Converter")

# Add labels, dropdowns, and inputs
Title = tk.Label(root, text="Welcome to UnitConverter", font=('Arial', 18))
Title.pack(padx=10, pady=10)

NumbersWarning = tk.Label(root, text="Remember to type only in numbers", font=('Arial', 10))
NumbersWarning.pack(padx=10, pady=10)

# Dropdown options for unit types
DropdownUnitTypeOptions = ["Select a unit type","Length", "Weight", "Temperature", "Energy"]
selected_option_DropdownUnitTypeOptions = tk.StringVar(value=DropdownUnitTypeOptions[0])  # Default value
DropdownUnitTypeOptionsMenu = tk.OptionMenu(root, selected_option_DropdownUnitTypeOptions, *DropdownUnitTypeOptions)
DropdownUnitTypeOptionsMenu.pack(padx=10, pady=10)

# Add trace to update dropdowns when unit type changes
selected_option_DropdownUnitTypeOptions.trace("w", update_options)

# Initialize FromUnitDropDown and ToUnitDropDown with placeholder options
selected_option_FromUnitDropDown = tk.StringVar(value="Select a unit")  # Set a default value
FromUnitDropDown = tk.OptionMenu(root, selected_option_FromUnitDropDown, "Meters", "Kilometers", "Centimeters")
FromUnitDropDown.pack(padx=10, pady=10)

selected_option_ToUnitDropDown = tk.StringVar(value="Select a unit") #   Set a default value
ToUnitDropDown = tk.OptionMenu(root, selected_option_ToUnitDropDown, "Meters", "Kilometers", "Centimeters")
ToUnitDropDown.pack(padx=10, pady=10)

# Input labels and fields
fromlabel = tk.Label(root, text="Amount:", font=('Arial', 10))
fromlabel.pack(padx=10, pady=10)

number1 = tk.Entry(root)
number1.pack(padx=10, pady=0)

# Label to show the conversion result
convertedlabel = tk.Label(root, text="", font=('Arial', 18))
convertedlabel.pack(padx=10, pady=10)


convertbutton = tk.Button(root, text="Convert", font=('Arial', 10), command=convert)
convertbutton.pack(padx=10, pady=10)

def update_text():
    while True:
        convert()

def start_dynamic_update():
    u = threading.Thread(target=update_text)
    u.daemon = True
    u.start()

start_dynamic_update()
# Run the Tkinter event loop
root.mainloop()
