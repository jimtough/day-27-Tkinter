import traceback
import logging
from tkinter import *


window = Tk()
window.title("Miles to Kilometers Converter")
window.minsize(width=500, height=300)
window.config(padx=30, pady=30)

miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)
print(miles_input.config())

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)
miles_label.config(padx=5, pady=5)

is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column=0, row=1)
is_equal_to_label.config(padx=5, pady=5)

km_value_label = Label(text="?")
km_value_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)
km_label.config(padx=5, pady=5)


def calculate_button_clicked():
    try:
        miles_value = float(miles_input.get())
        km_value = round(miles_value * 1.60934, 1)
        km_value_label.config(text=f"{km_value}")
    except Exception as e:
        logging.error(traceback.format_exc())
        km_value_label.config(text="?")


calculate_button = Button(text="Calculate", command=calculate_button_clicked)
calculate_button.grid(column=1, row=2)


window.mainloop()
