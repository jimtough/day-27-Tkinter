# import tkinter
from tkinter import *

# REFERENCE: https://docs.python.org/3/library/tkinter.html
window = Tk()
window.title("My First GUI Program!")
window.minsize(width=500, height=300)

# label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack()
# my_label.pack(side="bottom")
# my_label.pack(side="left")
# two ways to do the same thing...
my_label["text"] = "My New Text"
my_label.config(text="My Even Newer Text")


# button
def button_clicked():
    print("I got clicked")
    # my_label.config(text="Button got CLICKED")
    my_label.config(text=input.get())


button = Button(text="Click Me!", command=button_clicked)
button.pack()


# entry (text input)

input = Entry(width=10)
input.pack()
print(input.get())


window.mainloop()
