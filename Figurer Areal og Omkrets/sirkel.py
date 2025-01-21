import customtkinter as ctk
import threading
root = ctk.CTk()

root.title("Sirkel")
root.geometry("300x200")

Areal = ctk.CTkLabel(root, text="Areal:")
Areal.pack()

Omkrets = ctk.CTkLabel(root, text="Omkrets:")
Omkrets.pack()

def beregn():
    r = int(radius.get())
    A = 3.14*r*r
    O = 2*3.14*r
    Areal.configure(text="Areal: "+str(A))
    Omkrets.configure(text="Omkrets: "+str(O))

radius = ctk.CTkEntry(root, placeholder_text="Radius:")
radius.pack()

def update_text():
    while True:
        beregn()


def start_dynamic_update():
    u = threading.Thread(target=update_text)
    u.daemon = True
    u.start()

b = ctk.CTkButton(root, text="Beregn", command=beregn)
b.pack()

root.mainloop()
