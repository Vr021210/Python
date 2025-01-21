import customtkinter as ctk
import threading

# Initialize main application window
root = ctk.CTk()
root.geometry("500x500")

# Initialize the area variable
areal = 1

# Create and pack input fields and labels
grunnlinjeinput = ctk.CTkEntry(root, placeholder_text="Grunnlinje: ")
grunnlinjeinput.pack()

høydeinput = ctk.CTkEntry(root, placeholder_text="Høyde: ")
høydeinput.pack()

areallabel = ctk.CTkLabel(root, text=f"Result: {areal}")
areallabel.pack()

# Function to calculate area
def kalkuler():
    try:
        grunnlinje = int(grunnlinjeinput.get())
        hoyde = int(høydeinput.get())

        areal = grunnlinje * hoyde
        areallabel.configure(text=f"Result: {areal}")
    except ValueError:
        areallabel.configure(text="Please Enter a Valid Input")

# Function to dynamically update the result
def update_text():
    while True:
        kalkuler()

# Start a thread for dynamic updates
def start_dynamic_update():
    u = threading.Thread(target=update_text)
    u.daemon = True
    u.start()

# Start the dynamic updates (this may not be ideal)
start_dynamic_update()

# Add a button to manually calculate
kalkulerbutton = ctk.CTkButton(root, text="Kalkuler", command=kalkuler)
kalkulerbutton.pack()

# Start the main loop
root.mainloop()
