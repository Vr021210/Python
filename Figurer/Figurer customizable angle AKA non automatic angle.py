import customtkinter as ctk
import turtle 
turtle.speed("fastest")

numbers_1to10 = ["Figure Amount ","1","2","3","4","5","6","7","8","9","10"]

def draw():
    kanterMengde = int(kanteterinput.get())
    linjeLengde = int(linjeLengdeinput.get())
    vinkel = int(angleinput.get())
    antall_figurer = int(antall_figurerinput.get())

    def tegnFigur():
        for i in range(kanterMengde):
            turtle.forward(linjeLengde)
            turtle.left(vinkel)

    for i in range(antall_figurer):
        tegnFigur()
        turtle.left(360/antall_figurer)

def erease():
    turtle.clear()

root = ctk.CTk()
root.title("Turtle")
root.geometry("800x300")


canvas = ctk.CTkCanvas(root)
canvas.pack()

controller = ctk.CTkFrame(root)
controller.pack()

kanteterinput = ctk.CTkEntry(controller,placeholder_text="Kanter")
kanteterinput.pack(side="left")

linjeLengdeinput = ctk.CTkEntry(controller,placeholder_text="Linje lengde")
linjeLengdeinput.pack(side="left")

antall_figurerinput = ctk.CTkComboBox(controller,values=numbers_1to10)
antall_figurerinput.pack(side="left")

angleinput = ctk.CTkEntry(controller,placeholder_text="Angle")
angleinput.pack(side="left")

tegn = ctk.CTkButton(controller, text="Tegn", command=draw)
tegn.pack(side="left")

slett = ctk.CTkButton(controller, text="Slett", command=erease)
slett.pack(side="left")


root.mainloop()