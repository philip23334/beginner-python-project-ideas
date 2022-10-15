# import the tkinter library
from tkinter import *
# create a window
window = Tk()
# create a function to add two numbers
def add():
    # get the numbers from the entry fields
    num1 = float(e1.get())
    num2 = float(e2.get())
    # add the numbers
    result = num1 + num2
    # display the result
    t1.insert(END, result)
# create a function to subtract two numbers
def subtract():
    # get the numbers from the entry fields
    num1 = float(e1.get())
    num2 = float(e2.get())
    # subtract the numbers
    result = num1 - num2
    # display the result
    t1.insert(END, result)
# create a function to multiply two numbers
def multiply():
    # get the numbers from the entry fields
    num1 = float(e1.get())
    num2 = float(e2.get())
    # multiply the numbers
    result = num1 * num2
    # display the result
    t1.insert(END, result)
# create a function to divide two numbers
def divide():
    # get the numbers from the entry fields
    num1 = float(e1.get())
    num2 = float(e2.get())
    # divide the numbers
    result = num1 / num2
    # display the result
    t1.insert(END, result)
# create a function to clear the entry fields
def clear():
    # clear the entry fields
    e1.delete(0, END)
    e2.delete(0, END)
    t1.delete(1.0, END)
# create a label
l1 = Label(window, text="Number 1")
# create a label
l2 = Label(window, text="Number 2")
# create a label
l3 = Label(window, text="Result")
# create an entry field
e1 = Entry(window)
# create an entry field
e2 = Entry(window)
# create a text field
t1 = Text(window, height=1, width=20)
# create a button
b1 = Button(window, text="Add", command=add)
# create a button
b2 = Button(window, text="Subtract", command=subtract)
# create a button
b3 = Button(window, text="Multiply", command=multiply)
# create a button
b4 = Button(window, text="Divide", command=divide)
# create a button
b5 = Button(window, text="Clear", command=clear)
# place the label
l1.grid(row=0, column=0)
# place the label
l2.grid(row=1, column=0)
# place the label
l3.grid(row=2, column=0)
# place the entry field
e1.grid(row=0, column=1)
# place the entry field
e2.grid(row=1, column=1)
# place the text field
t1.grid(row=2, column=1)
# place the button
b1.grid(row=0, column=2)
# place the button
b2.grid(row=1, column=2)
# place the button
b3.grid(row=2, column=2)
# place the button
b4.grid(row=3, column=2)
# place the button
b5.grid(row=4, column=2)
# create a main loop
window.mainloop()