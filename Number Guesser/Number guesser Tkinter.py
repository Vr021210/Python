import tkinter as tk
root = tk.Tk()
from random import randint

guesses = 0
correct_answer = randint(1,101)


root.geometry("500x600")

def start():
    global correct_answer, guesses
    correct_answer = randint(1,101)
    guesses = 10
    guessesleft.config(text=f"{guesses}")


def check_answer():
    global guesses
    if int(guessbox.get()) < correct_answer:
        aboveorbelow.config(text="You Guessed Below")
        guesses = guesses -1
        guessesleft.config(text=f"{guesses}")
    
    
    elif int(guessbox.get()) > correct_answer:
        aboveorbelow.config(text="You Guessed Above")
        guesses = guesses -1
        guessesleft.config(text=f"{guesses}")
    
    
    elif int(guessbox.get()) == correct_answer:
        aboveorbelow.config(text="You Guessed Correct! Press Start to go again.")
        guesses = guesses -1
        guessesleft.config(text=f"{guesses}")

    elif guesses == 0:
        aboveorbelow.config(text="You Ran Out of Guesses!")
    
    else:
        aboveorbelow.config(text="Invalid Input!")

welcomelabel = tk.Label(root,text="Welcome to the Number Guessing Game", font=('Arial', 18))
welcomelabel.pack(padx=10,pady=10)

startbutton = tk.Button(root, text="Start/Restart", font=('Arial, 10'), command=start)
startbutton.pack(padx=10,pady=10)

guessbox = tk.Entry()
guessbox.pack(padx=10,pady=10)

guessbutton = tk.Button(root, text="Guess", font=('Arial', 10), command=check_answer)
guessbutton.pack()

aboveorbelow = tk.Label(root, text="Take A Guess", font=('Arial', 18))
aboveorbelow.pack()

guessesleft = tk.Label(root, text=f"{guesses}")
guessesleft.pack()

root.mainloop()