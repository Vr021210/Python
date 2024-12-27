import tkinter as tk
root = tk.Tk()

light = 0

def light_switch():
    global light
    if light == 1:
        light = 0
        lightlabel.config(text="Off")
    elif light == 0:
        light = 1
        lightlabel.config(text="On")

lightlabel = tk.Label(root,text=f"{light}", font=('Arial', 18))
lightlabel.pack(padx=10,pady=10)

button = tk.Button(root, text="Trigger Light", font=('Arial', 18), command=light_switch)
button.pack(padx=10,pady=10)

root.mainloop()