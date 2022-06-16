import tkinter

window = tkinter.Tk()
window.title("My First GUI Program!")
window.minsize(width=500, height=300)

# label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
# REFERENCE: https://docs.python.org/3/library/tkinter.html?highlight=packer#the-packer
# my_label.pack(side="bottom")
my_label.pack()



window.mainloop()
