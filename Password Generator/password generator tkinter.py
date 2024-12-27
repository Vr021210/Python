import tkinter as tk
import string
import random

# Initialize root window
root = tk.Tk()
root.geometry("500x500")
root.title("Password Generator")

# Function to generate a password
def generate_password():
    length = int(slider.get())
    # Define the character sets
    all_characters = string.ascii_letters + string.digits + string.punctuation
    
    # Randomly choose characters from the combined character set
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    # Display the generated password
    password_label.config(text=f"Generated Password: {password}")

# Function to show the current value of the slider
def show_value(value):
    label.config(text=f"Current Value: {value}")

# Slider to select password length
slider = tk.Scale(root, from_=0, to=100, orient="horizontal", command=show_value)
slider.pack(padx=20, pady=20)

# Label to display the slider's current value
label = tk.Label(root, text="Current Value: 0")
label.pack(padx=20, pady=0)

# Button to generate a password
button = tk.Button(root, text="Generate Password", font=('Arial', 10), command=generate_password)
button.pack(padx=20, pady=20)

# Label to display the generated password
password_label = tk.Label(root, text="Generated Password: ", font=('Arial', 10))
password_label.pack(padx=20, pady=20)

# Run the application
root.mainloop()
