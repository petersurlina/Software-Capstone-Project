# Name: Peter Surlina
# Description:
# Skeleton Outline of potential Drone GUI Controller
import tkinter as tk

# Top level window
root = tk.Tk()
root.title("Drone GUI")
root.geometry('1000x650')


# Function for getting Input from textboxes and printing it in label widget
def printInput():
    latInput = latTxt.get(1.0, "end-1c")
    longInput = longTxt.get(1.0, "end-1c")

    lbl2.config(text="Provided Coordinates: (" + latInput + " , " + longInput + ")")


def moveRight():
    directionLabel.config(text="Drone moved Right")
    return


def moveLeft():
    directionLabel.config(text="Drone moved Left")
    return


def moveBackward():
    directionLabel.config(text="Drone moved Backwards")
    return


def moveForward():
    directionLabel.config(text="Drone moved Forwards")
    return


def moveUp():
    directionLabel.config(text="Drone moved Upward")
    return


def moveDown():
    directionLabel.config(text="Drone moved Downward")
    return


def close():  # Must Include Condition that Drone is in flight so, we can't exit; wait until landed
    root.destroy()


# TextBox Creation
latTxt = tk.Text(root, height=2, width=30)
latTxt.place(x=110, y=215)

longTxt = tk.Text(root, height=2, width=30)
longTxt.place(x=110, y=265)

# Button Creation
printButton = tk.Button(root, text="Print Coordinates", command=printInput)
printButton.place(x=150, y=335)

forwardButton = tk.Button(root, text="Move Forward", command=moveForward)
forwardButton.place(x=600, y=170)

backwardButton = tk.Button(root, text="Move Backward", command=moveBackward)
backwardButton.place(x=600, y=320)

leftButton = tk.Button(root, text="Move Left", command=moveLeft)
leftButton.place(x=500, y=245)

rightButton = tk.Button(root, text="Move Right", command=moveRight)
rightButton.place(x=730, y=245)

upButton = tk.Button(root, text="Move Up", command=moveUp)
upButton.place(x=730, y=400)

downButton = tk.Button(root, text="Move Down", command=moveDown)
downButton.place(x=830, y=400)

exitButton = tk.Button(root, text="Exit", command=close)
exitButton.place(x=260, y=450)

# Label Creation
lbl = tk.Label(root, text="Place Coordinates")
lbl.place(x=150, y=160)

latLabel = tk.Label(root, text="Latitude: ")
latLabel.place(x=25, y=225)

longLabel = tk.Label(root, text="Longitude: ")
longLabel.place(x=25, y=275)

directionLabel = tk.Label(root, text="Which way are we going?")
directionLabel.place(x=445, y=400)

lbl2 = tk.Label(root)
lbl2.place(x=100, y=400)
root.mainloop()
