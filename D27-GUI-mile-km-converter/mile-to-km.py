from tkinter import *

FONT = ("Arial", 10, "normal")

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

num_miles = Entry(width=10)
num_miles.grid(column=1, row=0)


miles = Label(text="Miles", font=FONT)
miles.grid(column=2, row=0)
km = Label(text="Km", font=FONT)
km.grid(column=2, row=1)
equal = Label(text="is equal to", font=FONT)
equal.grid(column=0, row=1)

result = Label(text=0, font=FONT)
result.grid(column=1, row=1)


def button_clicked():
    result.config(text=str(float(num_miles.get())*1.609))


button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

window.mainloop()
