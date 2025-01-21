import customtkinter as ctk
import threading

root = ctk.CTk()
root.title("KarakterSnitt Kalkulator")
root.geometry("600x400")

enere = 0
toere = 0
treere = 0
firere = 0
femmere = 0
seksere = 0


values_list = []

def reset():
    values_list.clear()

def button1remove():
    values_list.remove(1)

def button2remove():
    values_list.remove(2)

def button3remove():
    values_list.remove(3)

def button4remove():
    values_list.remove(4)

def button5remove():
    values_list.remove(5)

def button6remove():
    values_list.remove(6)

def button1():
    values_list.append(1)
    enere += 1

def button2():
    values_list.append(2)
    toere += 1

def button3():
    values_list.append(3)
    treere += 1

def button4():
    values_list.append(4)
    firere += 1

def button5():
    values_list.append(5)
    femmere += 1

def button6():
    values_list.append(6)
    seksere += 1

leggtilgrid = ctk.CTkFrame(root)
leggtilgrid.pack(side="left",pady=50)

amountgrid = ctk.CTkFrame(root)
amountgrid.pack(side="right",pady=50)

fjerngrid = ctk.CTkFrame(root)
fjerngrid.pack(side="left",pady=50,padx=10)

leggtil = ctk.CTkLabel(leggtilgrid, text="Legg til karakter")
leggtil.grid(row=0, column=0)

fjern = ctk.CTkLabel(fjerngrid, text="karakter")
fjern.grid(row=0, column=0)

btn1 = ctk.CTkButton(leggtilgrid, text="1",command=button1)
btn1.grid(row=1, column=0,pady=3)

btn2 = ctk.CTkButton(leggtilgrid, text="2",command=button2)
btn2.grid(row=2, column=0,pady=3)

btn3 = ctk.CTkButton(leggtilgrid, text="3",command=button3)
btn3.grid(row=3, column=0,pady=3)

btn4 = ctk.CTkButton(leggtilgrid, text="4",command=button4)
btn4.grid(row=4, column=0,pady=3)

btn5 = ctk.CTkButton(leggtilgrid, text="5",command=button5)
btn5.grid(row=5, column=0,pady=3)

btn6 = ctk.CTkButton(leggtilgrid, text="6",command=button6)
btn6.grid(row=6, column=0,pady=3)

fjernbtn1 = ctk.CTkButton(fjerngrid, text="1",command=button1remove)
fjernbtn1.grid(row=1, column=0,pady=3)

fjernbtn2 = ctk.CTkButton(fjerngrid, text="2",command=button2remove)
fjernbtn2.grid(row=2, column=0,pady=3)

fjernbtn3 = ctk.CTkButton(fjerngrid, text="3",command=button3remove)
fjernbtn3.grid(row=3, column=0,pady=3)

fjernbtn4 = ctk.CTkButton(fjerngrid, text="4",command=button4remove)
fjernbtn4.grid(row=4, column=0,pady=3)

fjernbtn5 = ctk.CTkButton(fjerngrid, text="5",command=button5remove)
fjernbtn5.grid(row=5, column=0,pady=3)

fjernbtn6 = ctk.CTkButton(fjerngrid, text="6",command=button6remove)
fjernbtn6.grid(row=6, column=0,pady=3)

enerelabel = ctk.CTkLabel(amountgrid, text=f"Enere: {enere}")
enerelabel.grid(row=0, column=0)

toerelabel = ctk.CTkLabel(amountgrid, text=f"Toere: {toere}")
toerelabel.grid(row=1, column=0)

treerelabel = ctk.CTkLabel(amountgrid, text=f"Treere: {treere}")
treerelabel.grid(row=2, column=0)

firerelabel = ctk.CTkLabel(amountgrid, text=f"Firere: {firere}")
firerelabel.grid(row=3, column=0)

femmerelabel = ctk.CTkLabel(amountgrid, text=f"Femmere: {femmere}")
femmerelabel.grid(row=4, column=0)

sekserelabel = ctk.CTkLabel(amountgrid, text=f"Seksere: {seksere}")
sekserelabel.grid(row=5, column=0)

snittlabel = ctk.CTkLabel(root, text="Snitt: ")
snittlabel.pack(side="bottom")

resetbtn = ctk.CTkButton(root, text="Reset",command=reset)
resetbtn.pack(side="bottom")

def kalkuler():
    if values_list:  # Check if the list is not empty
        average = sum(values_list) / len(values_list)
        snittlabel.configure(text=f"Snitt: {average}")
    else:
        snittlabel.configure(text="Snitt: 0")  # Message when no values are present


def update_text():
    while True:
        kalkuler()
        enere = values_list.count(1)
        toere = values_list.count(2)
        treere = values_list.count(3)
        firere = values_list.count(4)
        femmere = values_list.count(5)
        seksere = values_list.count(6)
        enerelabel.configure(text=f"Enere: {enere}")
        toerelabel.configure(text=f"Toere: {toere}")
        treerelabel.configure(text=f"Treere: {treere}")
        firerelabel.configure(text=f"Firere: {firere}")
        femmerelabel.configure(text=f"Femmere: {femmere}")
        sekserelabel.configure(text=f"Seksere: {seksere}")

def start_dynamic_update():
    u = threading.Thread(target=update_text)
    u.daemon = True
    u.start()

start_dynamic_update()

root.mainloop()