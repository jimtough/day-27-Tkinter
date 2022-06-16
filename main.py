# import tkinter
from tkinter import *

# REFERENCES:
#  * https://docs.python.org/3/library/tkinter.html
#  * https://replit.com/@appbrewery/tkinter-widget-demo#main.py
window = Tk()
window.title("My First GUI Program!")
window.minsize(width=500, height=300)
window.config(padx=30, pady=30)

# label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
# my_label.pack()
# my_label.pack(side="bottom")
# my_label.pack(side="left")
# my_label.place(x=100, y=0)
my_label.grid(column=0, row=0)
# two ways to do the same thing...
my_label["text"] = "My New Text"
my_label.config(text="My Even Newer Text")
my_label.config(padx=50, pady=50)


# button
def button_clicked():
    print("I got clicked")
    # my_label.config(text="Button got CLICKED")
    my_label.config(text=input.get())


button_a = Button(text="Click Me!", command=button_clicked)
button_a.grid(column=1, row=1)

button_b = Button(text="also click me", command=button_clicked)
button_b.grid(column=2, row=0)


# entry (single line text input)
input = Entry(width=10)
# input.pack()
input.grid(column=3, row=2)


window.mainloop()
