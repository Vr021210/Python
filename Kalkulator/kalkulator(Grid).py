import tkinter as tk
import customtkinter as ctk

root = ctk.CTk()
root.geometry("400x700")
ctk.set_appearance_mode("light")  # Options: "light", "dark", "system"
ctk.set_default_color_theme("blue")
result = ""

# Global variable to store the current text in the textbox
current_text = ""

# Function to update the textbox
def update_textbox():
    textbox.config(text=current_text)

# Button functions
def press_number(num):
    global current_text
    current_text += str(num)  # Append the number to the current text
    update_textbox()

def press_operator(op):
    global current_text
    if current_text and current_text[-1] not in "+-*/^√%":  # Avoid duplicate operators
        current_text += op  # Append the operator
        update_textbox()

def press_clear():
    global current_text
    current_text = ""  # Clear the textbox
    update_textbox()

def press_equal():
    global current_text
    try:
        # Safely evaluate the expression and update the textbox
        result = str(eval(current_text))
        current_text = result
    except Exception:
        current_text = "Error"  # Display error for invalid expressions
    update_textbox()

# UI Setup
textbox = tk.Label(root, text="Text displayed here", font=('Arial', 24), anchor="e", bg="white", relief="solid")
textbox.pack(padx=20, pady=20, fill=tk.X)

buttonframe = tk.Frame(root, bg=root.cget("bg"))
buttonframe.pack(fill=tk.X, padx=20, pady=(0, 20))

# Configure columns to expand
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)
buttonframe.columnconfigure(3, weight=1)

# Number Buttons
btn1 = ctk.CTkButton(buttonframe, text="1", font=('Arial', 18), command=lambda: press_number(1), width=120, height=100, hover_color="Green", text_color="Black", fg_color="Blue")
btn1.grid(row=0, column=0, sticky=tk.W+tk.E, pady=2, padx=2)

btn2 = ctk.CTkButton(buttonframe, text="2", font=('Arial', 18), command=lambda: press_number(2), width=120, height=100, hover_color="Green", text_color="Black", fg_color="Blue")
btn2.grid(row=0, column=1, sticky=tk.W+tk.E, pady=2, padx=2)

btn3 = ctk.CTkButton(buttonframe, text="3", font=('Arial', 18), command=lambda: press_number(3), width=120, height=100, hover_color="Green", text_color="Black", fg_color="Blue")
btn3.grid(row=0, column=2, sticky=tk.W+tk.E, pady=2, padx=2)

btn4 = ctk.CTkButton(buttonframe, text="4", font=('Arial', 18), command=lambda: press_number(4), width=120, height=100, hover_color="Green", text_color="Black", fg_color="Blue")
btn4.grid(row=1, column=0, sticky=tk.W+tk.E, pady=2, padx=2)

btn5 = ctk.CTkButton(buttonframe, text="5", font=('Arial', 18), command=lambda: press_number(5), width=120, height=100, hover_color="Green", text_color="Black", fg_color="Blue")
btn5.grid(row=1, column=1, sticky=tk.W+tk.E, pady=2, padx=2)

btn6 = ctk.CTkButton(buttonframe, text="6", font=('Arial', 18), command=lambda: press_number(6), width=120, height=100, hover_color="Green", text_color="Black", fg_color="Blue")
btn6.grid(row=1, column=2, sticky=tk.W+tk.E, pady=2, padx=2)

btn7 = ctk.CTkButton(buttonframe, text="7", font=('Arial', 18), command=lambda: press_number(7), width=120, height=100, hover_color="Green", text_color="Black", fg_color="Blue")
btn7.grid(row=2, column=0, sticky=tk.W+tk.E, pady=2, padx=2)

btn8 = ctk.CTkButton(buttonframe, text="8", font=('Arial', 18), command=lambda: press_number(8), width=120, height=100, hover_color="Green", text_color="Black", fg_color="Blue")
btn8.grid(row=2, column=1, sticky=tk.W+tk.E, pady=2, padx=2)

btn9 = ctk.CTkButton(buttonframe, text="9", font=('Arial', 18), command=lambda: press_number(9), width=120, height=100, hover_color="Green", text_color="Black", fg_color="Blue")
btn9.grid(row=2, column=2, sticky=tk.W+tk.E, pady=2, padx=2)

btn0 = ctk.CTkButton(buttonframe, text="0", font=('Arial', 18), command=lambda: press_number(0), width=120, height=100, hover_color="Green", text_color="Black", fg_color="Blue")
btn0.grid(row=3, column=1, sticky=tk.W+tk.E, pady=2, padx=2)

# Operator Buttons
btnAdd = ctk.CTkButton(buttonframe, text="+", font=('Arial', 18), command=lambda: press_operator("+"), width=120, height=100, hover_color="Green", text_color="Black", fg_color="Blue")
btnAdd.grid(row=0, column=3, sticky=tk.W+tk.E, pady=2, padx=2)

btnMinus = ctk.CTkButton(buttonframe, text="-", font=('Arial', 18), command=lambda: press_operator("-"), width=120, height=100, hover_color="Green", text_color="Black", fg_color="Blue")
btnMinus.grid(row=1, column=3, sticky=tk.W+tk.E, pady=2, padx=2)

btnMultiply = ctk.CTkButton(buttonframe, text="X", font=('Arial', 18), command=lambda: press_operator("*"), width=120, height=100, hover_color="Green", text_color="Black", fg_color="Blue")
btnMultiply.grid(row=2, column=3, sticky=tk.W+tk.E, pady=2, padx=2)

btnDivide = ctk.CTkButton(buttonframe, text="/", font=('Arial', 18), command=lambda: press_operator("/"), width=120, height=100, hover_color="Green", text_color="Black", fg_color="Blue")
btnDivide.grid(row=3, column=3, sticky=tk.W+tk.E, pady=2, padx=2)

btnPower = ctk.CTkButton(buttonframe, text="^", font=('Arial', 18), command=lambda: press_operator("**"), width=120, height=100, hover_color="Green", text_color="Black", fg_color="Blue")
btnPower.grid(row=4, column=0, sticky=tk.W+tk.E, pady=2, padx=2)

btnSquareroot = ctk.CTkButton(buttonframe, text="√", font=('Arial', 18), command=lambda: press_operator("**0.5"), width=120, height=100, hover_color="Green", text_color="Black", fg_color="Blue")
btnSquareroot.grid(row=4, column=1, sticky=tk.W+tk.E, pady=2, padx=2)

btnDecimal = ctk.CTkButton(buttonframe, text=".", font=('Arial', 18), command=lambda: press_number("."), width=120, height=100, hover_color="Green", text_color="Black", fg_color="Blue")
btnDecimal.grid(row=4, column=2, sticky=tk.W+tk.E, pady=2, padx=2)

btnEqual = ctk.CTkButton(buttonframe, text="=", font=('Arial', 18), command=press_equal, width=120, height=100, hover_color="Green", text_color="Black", fg_color="Blue")
btnEqual.grid(row=3, column=2, sticky=tk.W+tk.E, pady=2, padx=2)

btnClear = ctk.CTkButton(buttonframe, text="C", font=('Arial', 18), command=press_clear, width=120, height=100, hover_color="Green", text_color="Black", fg_color="Blue")
btnClear.grid(row=3, column=0, sticky=tk.W+tk.E, pady=2, padx=2)

root.mainloop()
