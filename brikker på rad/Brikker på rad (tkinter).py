import tkinter as tk
root = tk.Tk()

def kalkuler_action():
    global antall_på_rad_entrybox, farger_entrybox
    farger_antall = int(farger_entrybox.get())
    antall_på_rad = int(antall_på_rad_entrybox.get())
    result = farger_antall ** antall_på_rad
    convertedlabel.config(text=f"Det er 1/{result}, sjanse for å få {antall_på_rad} brikker på rad")

root.title("Brikker på rad")
root.geometry("500x600")

welcomelabel = tk.Label(root, text="Brikker på rad", font=('Arial', 18))
welcomelabel.pack(padx=10,pady=10)

hvor_mange_farger_label = tk.Label(root, text="Hvor mange farger?", font=('Arial', 10))
hvor_mange_farger_label.pack(padx=10,pady=10)

farger_entrybox = tk.Entry()
farger_entrybox.pack(padx=0,pady=0)

antall_på_rad_label = tk.Label(root, text="Hvor Mange På Rad?", font=('Arial', 10))
antall_på_rad_label.pack(padx=10,pady=10)

antall_på_rad_entrybox = tk.Entry()
antall_på_rad_entrybox.pack(padx=0,pady=10)

kalkuler_button = tk.Button(root, text="Kalkuler", font=('Arial', 10), command=kalkuler_action)
kalkuler_button.pack(padx=10,pady=10)

convertedlabel = tk.Label(root, text="", font=('Arial', 18))
convertedlabel.pack(padx=10,pady=10)

root.mainloop()