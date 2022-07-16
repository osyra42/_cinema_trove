import os, time, re
from tkinter import *
import analysis
cmd = os.system


window = Tk()

gui = ""
gui += "Just click the buttons in order to enjoy the app.\n"

output = Label(window, text=gui)
output.grid(row=0, column=0)

button = Button(window, text="Analyze", command=analysis.analysis)
button.grid(row=1, column=0)



window.mainloop()


