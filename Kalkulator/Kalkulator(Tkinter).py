import tkinter as tk

def calculate():
    try:
        a = int(number1.get())  # Convert the first number from Entry
        b = int(number2.get())  # Convert the second number from Entry
        operation = selected_option.get()  # Get the selected operation
        
        # Perform the operation
        if operation == "Multiplication":
            result = a * b
        elif operation == "Addition":
            result = a + b
        elif operation == "Subtraction":
            result = a - b
        elif operation == "Divide":
            result = "Error: Division by zero" if b == 0 else a / b
        elif operation == "Power":
            result = a ** b
        else:
            result = "Invalid Operation"
        
        # Update result label
        resultlabel.config(text=f"Result: {result}")
    except ValueError:
        resultlabel.config(text="Error: Invalid input. Please enter valid numbers.")

root = tk.Tk()
root.geometry("500x500")

welcomelabel = tk.Label(root, text="Welcome to my calculator", font=('Arial', 18))
welcomelabel.pack(padx=10, pady=10)

number1 = tk.Entry(root)
number1.pack(padx=30, pady=30)

option = ["Multiplication (*)", "Subtraction (-)", "Divide (/)", "Power (**)", "Addition (+)"]
selected_option = tk.StringVar(value=option[0])  # Default value
option_menu = tk.OptionMenu(root, selected_option, *option)
option_menu.pack(padx=10, pady=10)

number2 = tk.Entry(root)
number2.pack(padx=30, pady=30)

calculate_button = tk.Button(root, text="Calculate", font=('Arial', 14), command=calculate)
calculate_button.pack(padx=10, pady=10)

resultlabel = tk.Label(root, text="Result: ", font=('Arial', 18))
resultlabel.pack(padx=10, pady=10)

root.mainloop()
