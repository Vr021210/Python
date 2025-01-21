import customtkinter as ctk
import threading


root = ctk.CTk()
root.geometry("500x500")


areal = 1


grunnlinjeinput = ctk.CTkEntry(root, placeholder_text="Grunnlinje: ")
grunnlinjeinput.pack()

høydeinput = ctk.CTkEntry(root, placeholder_text="Høyde: ")
høydeinput.pack()

areallabel = ctk.CTkLabel(root, text=f"Areal: {areal}")
areallabel.pack()


def kalkuler():
    try:
        grunnlinje = int(grunnlinjeinput.get())
        hoyde = int(høydeinput.get())

        areal = grunnlinje * hoyde
        areallabel.configure(text=f"Areal: {areal}")
    except ValueError:
        areallabel.configure(text="Please Enter a Valid Input")


def update_text():
    while True:
        kalkuler()


def start_dynamic_update():
    u = threading.Thread(target=update_text)
    u.daemon = True
    u.start()


start_dynamic_update()


root.mainloop()
