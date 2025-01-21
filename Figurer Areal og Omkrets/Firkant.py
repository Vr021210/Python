import customtkinter as ctk
import threading
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



arealLabel = ctk.CTkLabel(root, text="Areal: ")
arealLabel.pack()

omkretsLabel = ctk.CTkLabel(root, text="Omkrets: ")
omkretsLabel.pack()

def update_text():
    while True:
        kalkuler()


def start_dynamic_update():
    u = threading.Thread(target=update_text)
    u.daemon = True
    u.start()





root.mainloop()
