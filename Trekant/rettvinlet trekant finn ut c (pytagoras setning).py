import customtkinter as ctk
root = ctk.CTk()

root.title("Rettvinklet trekant")
root.geometry("1300x400")

def kalkuler():
    a = int(aInput.get())
    b = int(bInput.get())

    c = (a**2 + b**2) **0.5

    cLabel.configure(text="C: " + str(c))



aInput = ctk.CTkEntry(root,placeholder_text="A")
aInput.pack()

bInput = ctk.CTkEntry(root,placeholder_text="B")
bInput.pack()

kalkulerButton = ctk.CTkButton(root, text="Kalkuler", command=kalkuler)
kalkulerButton.pack()

cLabel = ctk.CTkLabel(root, text="C: ")
cLabel.pack()

root.mainloop()