from tkinter import *
from random import randint, choice

def down():
    button.place(x=randint(-400,400),
                          y=randint(-1000,1000))
    
    global points
    if button["text"] != "Start?":
        points += 1
    pointLabel.config(text=f"Points: {points}")
    
    if button["text"] == "Start?":
        button.config(text="Click!")
    
    colors = ["blue", "red",
                   "yellow", "green",
                   "orange", "purple",
                   "pink", "grey",
                   "lime", "sky blue",
                   "brown", "dark red",
                   "white", "dark orange",
                   "turquoise", "#7f32a8",
                   "#4a2c1d", "#82a16a",
                   "#f6db5f", "#ffb554",
                   "#fe5e51", "#9e3d64",
                   "#36abb5", "#ffb3ba",
                   "#ffd2b3", "#fff8b3",
                   "#baffb3", "#bae1ff",
                   "#ff9305", "#f203ff",
                   "#543d2d"]
    button.config(bg=choice(colors),
                            activebackground=choice(colors))
    colr = ["sky blue", "light blue", "light sky blue",
               "light yellow", "light pink", "blue",
               "light green"]
    bgs = choice(colr)
    window["bg"] = bgs
    pointLabel["bg"] = bgs


window = Tk()

points = 0

pointLabel = Label(window,text=f"Points: {points}")
pointLabel.pack(pady=20)

button = Button(window,
                            text="Start?",
                            font=("",10),
                            bg="Light grey",
                            activebackground="dark grey",
                            activeforeground="white",
                            relief=RAISED,
                            bd=9,
                            command=down)
button.place(relx=0.5,rely=0.5,anchor=CENTER)

window.mainloop()