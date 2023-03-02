from tkinter import *
import pandas

window = Tk()
window.minsize(width=500, height=600)
window.title(string='Prima aplicatie')

eticheta = Label(text='Inca nu afiseaza nimic')
eticheta.pack()


def click_button1():
    if len(button1_input.get()) >= 1:
        eticheta.config(text=f'{button1_input.get().capitalize()}')
        button1.config(text=f'{button1_input.get().capitalize()}')
    else:
        button1.config(text='Click me')
        eticheta.config(text='Hey vezi ca nu ai scris nimic:)')


button1 = Button(text='Click here', command=click_button1)
button1.pack()
button1_input = Entry(width=10)
button1_input.pack()

window.mainloop()
