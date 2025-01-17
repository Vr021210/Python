import customtkinter as ctk
root = ctk.CTk()

root.title("Kvadrat")
root.geometry("1300x400")

breddeinput = ctk.CTkEntry(root,placeholder_text="Bredde")
breddeinput.pack()

hoydeinput = ctk.CTkEntry(root,placeholder_text="Høyde")
hoydeinput.pack()

def kalkuler():
    bredde = int(breddeinput.get())
    hoyde = int(hoydeinput.get())
    areal = bredde * hoyde
    arealLabel.configure(text="Areal: " + str(areal)) 

    omkrets = 2 * bredde + 2 * hoyde
    omkretsLabel.configure(text="Omkrets: " + str(omkrets))


kalkulerButton = ctk.CTkButton(root, text="Kalkuler", command=kalkuler)
kalkulerButton.pack()

arealLabel = ctk.CTkLabel(root, text="Areal: ")
arealLabel.pack()

omkretsLabel = ctk.CTkLabel(root, text="Omkrets: ")
omkretsLabel.pack()





root.mainloop()