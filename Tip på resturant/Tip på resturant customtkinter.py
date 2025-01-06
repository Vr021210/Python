import tkinter as tk
import customtkinter as ctk
from customtkinter import CTkSwitch, CTkComboBox

chosenColor = "system"

root = ctk.CTk()
root.geometry("700x500")
root.title("Tip på Resturant")
ctk.set_appearance_mode(chosenColor)  # Options: "light", "dark", "system"
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
    

titlelabel = ctk.CTkLabel(root, text="Tip på Resturant", font=('Oswald', 18))
titlelabel.pack(padx=10, pady=10)

costlabel = ctk.CTkLabel(root, text="Cost Amount:", font=('Oswald', 12))
costlabel.pack(padx=10, pady=0)

costentry = ctk.CTkEntry(root, placeholder_text="Enter Amount:", font=('Oswald', 12))
costentry.pack(padx=10, pady=5)

tiplabel = ctk.CTkLabel(root, text="Tip Percentage Amount:", font=('Oswald', 12))
tiplabel.pack(padx=10, pady=0)

tipentry = ctk.CTkEntry(root, placeholder_text="Enter Amount:", font=('Oswald', 12))
tipentry.pack(padx=10, pady=5)

def update_people():
    if peopleswitch.get() == 1:
        peopleComboBox.pack(padx=10, pady=5, before=calculate_button)
    else:
        peopleComboBox.pack_forget()

peopleswitch = ctk.CTkSwitch(root, text="Split the bill?", font=('Oswald', 12), command=update_people)
peopleswitch.pack(padx=10, pady=10)

peopleComboBox = CTkComboBox(root, values=[str(i) for i in range(1, 10)], font=('Oswald', 12))
peopleComboBox.pack_forget()  # Initially hide the combo box

calculate_button = ctk.CTkButton(root, text="Calculate", command=calculate, font=('Oswald', 12))
calculate_button.pack(padx=10, pady=10)

resultlabel = ctk.CTkLabel(root, text="", font=('Oswald', 12))
resultlabel.pack(padx=10, pady=10)

dev_frame = ctk.CTkFrame(root)
dev_frame.pack(side="bottom", fill="x", padx=10, pady=10)

devinput = ctk.CTkEntry(dev_frame, placeholder_text="Enter Password", show="*", font=('Oswald', 12))
devinput.pack(side="left", padx=5)

colorchoice = ctk.CTkComboBox(dev_frame, values=["light", "dark", "system"], font=('Oswald', 12))
colortheme = ctk.CTkComboBox(dev_frame, values=["blue", "Red", "green", "purple", "orange", "yellow", "pink", "grey", "black", "white"], font=('Oswald', 12))

def apply_color():
    chosenColor = colorchoice.get()
    ctk.set_appearance_mode(chosenColor)
    

apply_colorbutton = ctk.CTkButton(dev_frame, text="Apply Background/Button Color", command=apply_color, font=('Oswald', 12))

def apply_geometry():
    new_geometry = geometry_entry.get()
    root.geometry(new_geometry)

geometry_entry = ctk.CTkEntry(dev_frame, placeholder_text="Enter Geometry (e.g., 400x500)", font=('Oswald', 12))
geometry_entry.pack_forget()  # Initially hide the geometry entry

apply_geometry_button = ctk.CTkButton(dev_frame, text="Apply Geometry", command=apply_geometry, font=('Oswald', 12))

def devmode():
    global result
    if devinput.get() == "123besto":
        if not apply_colorbutton.winfo_ismapped():
            apply_colorbutton.pack(pady=5, padx=5)
        if not apply_geometry_button.winfo_ismapped():
            apply_geometry_button.pack(pady=5, padx=5)
        if not geometry_entry.winfo_ismapped():
            geometry_entry.pack(side="left", padx=5)

        result = "Dev Mode Enabled"
        
        colorchoice.pack(pady=5, padx=5)

        devbutton.configure(bg="green")
    else:
        result = "Incorrect Password"
        devbutton.configure(bg="red")
    devlabel.configure(text=result)

devbutton = ctk.CTkButton(dev_frame, text="Dev Mode", command=devmode, font=('Oswald', 12))
devbutton.pack(side="left", padx=5)

devlabel = ctk.CTkLabel(dev_frame, text="", font=('Oswald', 12))
devlabel.pack(side="left", padx=5)

root.mainloop()
