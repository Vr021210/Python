import time
import threading
import customtkinter as ctk
Trafficlight = 1

root = ctk.CTk()
trafficlight1 = 0
trafficlight2 = 1
trafficlight3 = 1
trafficlight4 = 0

trafficlight1Label = ctk.CTkLabel(root, text="Trafficlight 1: ")
trafficlight2Label = ctk.CTkLabel(root, text="Trafficlight 2: ")
trafficlight3Label = ctk.CTkLabel(root, text="Trafficlight 3: ")
trafficlight4Label = ctk.CTkLabel(root, text="Trafficlight 4: ")


def stop_trafficlight():
    global Trafficlight
    Trafficlight = 0
    global trafficlight1
    global trafficlight2
    global trafficlight3
    global trafficlight4

    trafficlight1 = 0
    trafficlight2 = 0
    trafficlight3 = 0
    trafficlight4 = 0
    trafficlight1Label.configure(text="Trafficlight 1: " + str(trafficlight1))
    trafficlight2Label.configure(text="Trafficlight 2: " + str(trafficlight2))
    trafficlight3Label.configure(text="Trafficlight 3: " + str(trafficlight3))
    trafficlight4Label.configure(text="Trafficlight 4: " + str(trafficlight4))

def stop_trafficlight_for_certain_time():
    stoptime = int(stoptimeInput.get())

    global trafficlight1
    global trafficlight2
    global trafficlight3
    global trafficlight4
    stop_trafficlight()
    trafficlight1Label.configure(text="Trafficlight 1: " + str(trafficlight1))
    trafficlight2Label.configure(text="Trafficlight 2: " + str(trafficlight2))
    trafficlight3Label.configure(text="Trafficlight 3: " + str(trafficlight3))
    trafficlight4Label.configure(text="Trafficlight 4: " + str(trafficlight4))

    time.sleep(stoptime)

    StartTrafficLightForever()

def change_trafficlight():
    global Trafficlight
    Trafficlight = 1
    global trafficlight1
    global trafficlight2
    global trafficlight3
    global trafficlight4

    if trafficlight1 == 1:
        trafficlight1 = 0
        trafficlight2 = 1
        trafficlight3 = 1
        trafficlight4 = 0
    else:
        trafficlight1 = 1
        trafficlight2 = 0
        trafficlight3 = 0
        trafficlight4 = 1

    trafficlight1Label.configure(text="Trafficlight 1: " + str(trafficlight1))
    trafficlight2Label.configure(text="Trafficlight 2: " + str(trafficlight2))
    trafficlight3Label.configure(text="Trafficlight 3: " + str(trafficlight3))
    trafficlight4Label.configure(text="Trafficlight 4: " + str(trafficlight4))

def TrafficLightForever():

    intervaltime = int(changeintervalInput.get())
    change_trafficlight()
    time.sleep(intervaltime)
    if Trafficlight == 1:
        TrafficLightForever()

def StartTrafficLightForever():
    t = threading.Thread(target=TrafficLightForever)
    t.daemon = True
    t.start()

def start_stop_trafficlight_for_certaintime():
    u = threading.Thread(target=stop_trafficlight_for_certain_time)
    u.daemon = True
    u.start()

root.title("Trafikk lys")
root.geometry("1300x400")

controller = ctk.CTkFrame(root)
controller.pack(side="top", fill="x")

changeintervalInput = ctk.CTkEntry(controller, placeholder_text="Interval in seconds")
changeintervalInput.pack(in_=controller, side="left",padx=10)

startButton = ctk.CTkButton(controller, text="Start Forever", command=StartTrafficLightForever)
startButton.pack(in_=controller, side="left", padx=10)

fixstartforeverbutton = ctk.CTkButton(controller, text="Fix Start Forever", command=StartTrafficLightForever)
fixstartforeverbutton.pack(in_=controller, side="left", padx=10)

stopButton = ctk.CTkButton(controller, text="Stop Forever", command=stop_trafficlight)
stopButton.pack(in_=controller, side="left",padx=10)

stoptimeInput = ctk.CTkEntry(controller, placeholder_text="Time in seconds")
stoptimeInput.pack(in_=controller, side="left")

stop_for_certain_time = ctk.CTkButton(controller, text="Stop For (Input) Amount of time", command=start_stop_trafficlight_for_certaintime)
stop_for_certain_time.pack(in_=controller, side="left", padx=10)

changebutton = ctk.CTkButton(controller, text="Change", command=change_trafficlight)
changebutton.pack(in_=controller, side="left")

trafficlight1Label.pack(side="top")
trafficlight2Label.pack(side="top")
trafficlight3Label.pack(side="top")
trafficlight4Label.pack(side="top")


root.mainloop()
