from tkinter import *
import math


def leftClickButton(event):
    height = int(textBoxHeight.get())
    weight = int(textBoxWeight.get())
    BMI = round((weight / (math.pow(height / 100, 2))), 2)

    labelResult.configure(text=BMI)

    if BMI < 18.5:
        labelBMI.configure(text="Thin")
    elif BMI < 23:
        labelBMI.configure(text="Normal")
    elif BMI < 25:
        labelBMI.configure(text="Lots of Weight")
    elif BMI < 30:
        labelBMI.configure(text="Fat Level 1")
    else:
        labelBMI.configure(text="Fat Level 2")


Mainwindow = Tk()
labelHeight = Label(Mainwindow, text="Height (Cm.)")
labelHeight.grid(row=0, column=0)

textBoxHeight = Entry(Mainwindow)
textBoxHeight.grid(row=0, column=1)

labelWeight = Label(Mainwindow, text="Weight (Kg.)")
labelWeight.grid(row=1, column=0)

textBoxWeight = Entry(Mainwindow)
textBoxWeight.grid(row=1, column=1)

calculateButton = Button(Mainwindow, text="Calculate")
calculateButton.bind('<Button-1>', leftClickButton)
calculateButton.grid(row=2, column=0)

labelResult = Label(Mainwindow, text="Result")
labelResult.grid(row=2, column=1)

labelBMI = Label(Mainwindow, text="BMI")
labelBMI.grid(row=3, column=1)

Mainwindow.mainloop()
