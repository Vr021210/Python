from random import randint
import tkinter as tk
root = tk.Tk()
root.geometry("500x600")
velkommenlabel = tk.Label(root, text="TerningKast", font=('Arial', 18))
velkommenlabel.pack()
def kast_terninger():
    try:
        n = int(entry.get())  # Retrieve the number of rolls from the entry
        if n <= 0:
            raise ValueError("Antall kast må være større enn 0.")
        
        ener = 0
        toer = 0
        treer = 0
        firer = 0
        femmer = 0
        sekser = 0
        en_av = 6 ** n
        fraction = 1 / en_av
        percentage = fraction * 100

        # Perform the dice rolls
        for _ in range(n):
            terning = randint(1, 6)  # Corrected randint range to (1, 6)
            if terning == 1:
                ener += 1
            elif terning == 2:
                toer += 1
            elif terning == 3:
                treer += 1
            elif terning == 4:
                firer += 1
            elif terning == 5:
                femmer += 1
            elif terning == 6:
                sekser += 1

        # Display results
        EnLabel.config(text=f"Du fikk {ener} Enere")
        toLabel.config(text=f"Du fikk {toer} toere")
        treLabel.config(text=f"Du fikk {treer} treere")
        fireLabel.config(text=f"Du fikk {firer} firere")
        femLabel.config(text=f"Du fikk {femmer} femmere")
        seksLabel.config(text=f"Du fikk {sekser} seksere")
        sjanselabel.config(text=f"Sjansen for å få det du fikk var en av {en_av}")
        prosentlabel.config(text=f"Prosentsjansen var {percentage:.10f} prosent")
    except ValueError as e:
        # Handle invalid input
        error_label.config(text=f"Feil: {e}")


entry = tk.Entry()
entry.pack(padx=10, pady=10)

button = tk.Button(root, text="Kast Terning", font=('Arial', 10), command=kast_terninger)
button.pack(padx=10, pady=10)

# Labels for displaying results
EnLabel = tk.Label(root, font=('Arial', 10))
EnLabel.pack(padx=10, pady=10)

toLabel = tk.Label(root, font=('Arial', 10))
toLabel.pack(padx=10, pady=10)

treLabel = tk.Label(root, font=('Arial', 10))
treLabel.pack(padx=10, pady=10)

fireLabel = tk.Label(root, font=('Arial', 10))
fireLabel.pack(padx=10, pady=10)

femLabel = tk.Label(root, font=('Arial', 10))
femLabel.pack(padx=10, pady=10)

seksLabel = tk.Label(root, font=('Arial', 10))
seksLabel.pack(padx=10, pady=10)

sjanselabel = tk.Label(root, font=('Arial', 10))
sjanselabel.pack(padx=10, pady=10)

prosentlabel = tk.Label(root, font=('Arial', 10))
prosentlabel.pack(padx=10, pady=10)

# Error message label
error_label = tk.Label(root, font=('Arial', 10), fg="red")
error_label.pack(padx=10, pady=10)

root.mainloop()
