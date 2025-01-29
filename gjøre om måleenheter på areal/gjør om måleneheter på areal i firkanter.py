import tkinter as tk
import customtkinter as ctk
import threading
import time
root = ctk.CTk()

root.title("gjør om målenheter på kvadratTall")
root.geometry("500x500")

kvadratframe = ctk.CTkFrame(root)
kvadratframe.pack(side="left",pady=10,padx=10)

explainframe = ctk.CTkLabel(kvadratframe,text="Her gjør du om fra lengde og bredde til areal")
explainframe.pack()

arealinput = ctk.CTkEntry(root,placeholder_text="Areal:")
arealinput.pack()

lengdeinputkvadratframe = ctk.CTkEntry(kvadratframe,placeholder_text="Lengde:")
lengdeinputkvadratframe.pack()

breddeinputkvadratframe = ctk.CTkEntry(kvadratframe,placeholder_text="Bredde:")
breddeinputkvadratframe.pack()

arealresultkvadratframe = ctk.CTkLabel(kvadratframe,text="Lengde: ")
arealresultkvadratframe.pack()

resultlabel = ctk.CTkLabel(root,text="Result Will be Displayed Here")
resultlabel.pack()

fromunitdropdown = ctk.CTkOptionMenu(root, values=["From","km^2","m^2","dm^2","cm^2","mm^2"])
fromunitdropdown.pack()

tounitdropdown = ctk.CTkOptionMenu(root, values=["To:","km^2","m^2","dm^2","cm^2","mm^2"])
tounitdropdown.pack()



def calculate(): #Do This Next
    try:
        areal=int(arealinput.get())
        
        resultlabel.configure(text="Areal:")

        if fromunitdropdown.get() == "m^2" and tounitdropdown.get() == "dm^2":
            resultlabel.configure(text=f"Areal: {areal*100}")
        elif fromunitdropdown.get() == "m^2" and tounitdropdown.get() == "cm^2":
            resultlabel.configure(text=f"Areal: {areal*10000}")
        elif fromunitdropdown.get() == "m^2" and tounitdropdown.get() == "mm^2":
            resultlabel.configure(text=f"Areal: {areal*1000000}")
        elif fromunitdropdown.get() == "m^2" and tounitdropdown.get() == "km^2":
            resultlabel.configure(text=f"Areal: {areal/1000000}")
        elif fromunitdropdown.get() == "dm^2" and tounitdropdown.get() == "m^2":
            resultlabel.configure(text=f"Areal: {areal/100}")
        elif fromunitdropdown.get() == "dm^2" and tounitdropdown.get() == "cm^2":
            resultlabel.configure(text=f"Areal: {areal*100}")
        elif fromunitdropdown.get() == "dm^2" and tounitdropdown.get() == "mm^2":
            resultlabel.configure(text=f"Areal: {areal*10000}")
        elif fromunitdropdown.get() == "dm^2" and tounitdropdown.get() == "km^2":
            resultlabel.configure(text=f"Areal: {areal/100000000}")
        elif fromunitdropdown.get() == "cm^2" and tounitdropdown.get() == "m^2":
            resultlabel.configure(text=f"Areal: {areal/10000}")
        elif fromunitdropdown.get() == "cm^2" and tounitdropdown.get() == "dm^2":
            resultlabel.configure(text=f"Areal: {areal/100}")
        elif fromunitdropdown.get() == "cm^2" and tounitdropdown.get() == "mm^2":
            resultlabel.configure(text=f"Areal: {areal*100}")
        elif fromunitdropdown.get() == "cm^2" and tounitdropdown.get() == "km^2":
            resultlabel.configure(text=f"Areal: {areal/10000000000}")
        elif fromunitdropdown.get() == "mm^2" and tounitdropdown.get() == "m^2":
            resultlabel.configure(text=f"Areal: {areal/1000000}")
        elif fromunitdropdown.get() == "mm^2" and tounitdropdown.get() == "dm^2":
            resultlabel.configure(text=f"Areal: {areal/10000}")
        elif fromunitdropdown.get() == "mm^2" and tounitdropdown.get() == "cm^2":
            resultlabel.configure(text=f"Areal: {areal/100}")
        elif fromunitdropdown.get() == "mm^2" and tounitdropdown.get() == "km^2":
            resultlabel.configure(text=f"Areal: {areal/1000000000000}")
        elif fromunitdropdown.get() == "km^2" and tounitdropdown.get() == "m^2":
            resultlabel.configure(text=f"Areal: {areal*1000000}")
        elif fromunitdropdown.get() == "km^2" and tounitdropdown.get() == "dm^2":
            resultlabel.configure(text=f"Areal: {areal*100000000}")
        elif fromunitdropdown.get() == "km^2" and tounitdropdown.get() == "cm^2":
            resultlabel.configure(text=f"Areal: {areal*10000000000}")
        elif fromunitdropdown.get() == "km^2" and tounitdropdown.get() == "mm^2":
            resultlabel.configure(text=f"Areal: {areal*1000000000000}")
    except ValueError:
        resultlabel.configure(text="Invalid input")

    root.after(1000,calculate)

def calculate_lengde_bredde():
    try:
        lengde = int(lengdeinputkvadratframe.get().strip())
        bredde = int(breddeinputkvadratframe.get().strip())
        areal = lengde * bredde
        arealresultkvadratframe.configure(text=f"Areal: {areal}")
    except ValueError:
        arealresultkvadratframe.configure(text="Feil: Vennligst skriv inn gyldige tall.")


    root.after(1000,calculate_lengde_bredde)


calculate_lengde_bredde()

calculate()
root.mainloop()