from tkinter import *
from tkinter import ttk

#Project uses code adapted from the following references:
# https://www.geeksforgeeks.org/python-grid-method-in-tkinter/
# https://www.tutorialspoint.com/python/tk_button.htm
# https://stackoverflow.com/questions/63299342/attributeerror-builtin-function-or-method-object-has-no-attribute-get
# Udemy course: 100 Days of Code: The Complete Python Pro Bootcamp
#Button Clicked Function
def button_clicked():
    userInput = entry.get()
    result = float(userInput) * 1.6
    return result

#Get user input
def miles_input():
    global entry 
    milesEntered = entry.get()
    kilometersCalc = Label(root, text=str(button_clicked()))
    kilometersCalc.grid(row=1, column=1, sticky=W, pady=2)


#Create Window
root = Tk()
root.title("Miles to Kilometer Converter")
root.minsize(width=500, height=300)

#Create user input field
entry= Entry(root, width=10)
entry.grid(row=0, column=1, sticky=W, pady=2)

#Create Labels
miles = Label(root, text="miles")
isEqualTo = Label(root, text="is Equal To")
kilometers = Label(root, text="kilometers")
inputLabel = Label(root, text="")

#Label grid layout
miles.grid(row=0, column=2, sticky=W, pady=2)
isEqualTo.grid(row=1, column=0,sticky=W, pady=2)
kilometers.grid(row=1, column=2, sticky=W, pady=2)
inputLabel.grid(row=1, column=1, sticky=W, pady=2)

#Create Button
button= Button(root, text="Calculate",command=miles_input, activebackground="blue", activeforeground="white")
button.grid(row=2, column=1, sticky=W, pady=2)


mainloop()