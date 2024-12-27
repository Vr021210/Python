import tkinter as tk
import customtkinter as ctk
root = ctk.CTk()

root.geometry("400x500")
ctk.set_appearance_mode("system")  # Options: "light", "dark", "system"
ctk.set_default_color_theme("blue")
result = ""

def calculate():
    # Get values from the entries, convert them to floats or integers
    cost = int(costentry.get())
    tip_percent = int(tipentry.get())
    people = int(peopleEntry.get())
    
    # Calculate the tip and total amount per person
    tip = cost * (tip_percent / 100)
    total = cost + tip
    result = total / people
    
    # Update the result label
    resultlabel.configure(text=f"Total per person: ${result:.2f}")

    

titlelabel = ctk.CTkLabel(root, text="Tip på Resturant", font=('Arial', 18))
titlelabel.pack(padx=10,pady=10)

costlabel = ctk.CTkLabel(root, text="Cost Amount:", font=('Arial', 12))
costlabel.pack(padx=10,pady=0)

costentry = ctk.CTkEntry(master=root,placeholder_text="Enter Amount:")
costentry.pack(padx=10,pady=0)

tiplabel = ctk.CTkLabel(root, text="Tip Percentage Amount:", font=('Arial', 12))
tiplabel.pack(padx=10,pady=0)

tipentry = ctk.CTkEntry(master=root, placeholder_text="Enter Amount:")
tipentry.pack(padx=10,pady=0)

PeopleLabel = ctk.CTkLabel(root, text="Amount of people:", font=('Arial', 12))
PeopleLabel.pack(padx=10,pady=0)

peopleEntry = ctk.CTkEntry(master=root, placeholder_text="Enter Amount:")
peopleEntry.pack(padx=10,pady=0)

calculatebutton = ctk.CTkButton(root, text="Calculate", font=('Arial', 18), command=calculate)
calculatebutton.pack(padx=10,pady=10)

resultlabel = ctk.CTkLabel(root, text="Total per person is $0", font=('Arial', 18))
resultlabel.pack(padx=10,pady=0)


root.mainloop()