from tkinter import *
import pandas

window = Tk()
window.minsize(width=500, height=600)
window.title(string='Prima aplicatie')
window.config(padx=20, pady=20)

eticheta = Label(text='Inca nu afiseaza nimic')
eticheta.grid(column=0, row=0)


def click_button1():
    display_name = button1_input.get().capitalize()
    if len(button1_input.get()) >= 1:
        print(button1_input.get())
        print(type(button1_input.get()))
        eticheta.config(text=f'{display_name}')
        button1.config(text=f'{display_name}')
    else:
        button1.config(text='Click me')
        eticheta.config(text='Hey vezi ca nu ai scris nimic:)')


button1 = Button(text='Click here', command=click_button1)
button1.grid(column=1, row=1)
button1_input = Entry(width=10)
button1_input.grid(column=2, row=2)

new_button = Button(text='New Button')
new_button.grid(row=0, column=3)

window.mainloop()
