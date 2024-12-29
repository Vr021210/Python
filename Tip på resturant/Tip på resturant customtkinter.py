import tkinter as tk
import customtkinter as ctk
from customtkinter import CTkSwitch, CTkComboBox

root = ctk.CTk()
root.geometry("400x500")
ctk.set_appearance_mode("system")  # Options: "light", "dark", "system"
ctk.set_default_color_theme("blue")
result = ""

def calculate():
    try:
        # Get values from the entries, convert them to floats or integers
        cost = float(costentry.get())
        tip_percent = float(tipentry.get())
        people = int(peopleComboBox.get())
        
        # Calculate the tip and total amount per person
        tip = cost * (tip_percent / 100)
        total = cost + tip
        result = total / people
        
        # Update the result label
        resultlabel.configure(text=f"Total per person: ${result:.2f}")
    except ValueError:
        resultlabel.configure(text="Please enter valid numbers.")

titlelabel = ctk.CTkLabel(root, text="Tip på Resturant", font=('Arial', 18))
titlelabel.pack(padx=10, pady=10)

costlabel = ctk.CTkLabel(root, text="Cost Amount:", font=('Arial', 12))
costlabel.pack(padx=10, pady=0)

costentry = ctk.CTkEntry(root, placeholder_text="Enter Amount:")
costentry.pack(padx=10, pady=5)

tiplabel = ctk.CTkLabel(root, text="Tip Percentage Amount:", font=('Arial', 12))
tiplabel.pack(padx=10, pady=0)

tipentry = ctk.CTkEntry(root, placeholder_text="Enter Amount:")
tipentry.pack(padx=10, pady=5)

def update_people():
    if peopleswitch.get() == 1:
        peopleComboBox.pack(padx=10, pady=5, before=calculate_button)
    else:
        peopleComboBox.pack_forget()

peopleswitch = ctk.CTkSwitch(root, text="Split the bill?", font=('Arial', 12), command=update_people)
peopleswitch.pack(padx=10, pady=10)

peopleComboBox = CTkComboBox(root, values=[str(i) for i in range(1, 10)])
peopleComboBox.pack_forget()  # Initially hide the combo box

calculate_button = ctk.CTkButton(root, text="Calculate", command=calculate)
calculate_button.pack(padx=10, pady=10)

resultlabel = ctk.CTkLabel(root, text="", font=('Arial', 12))
resultlabel.pack(padx=10, pady=10)

root.mainloop()
