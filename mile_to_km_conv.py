from tkinter import *
import sys

window = Tk()
window.title(string='Program convert mile to km')
window.minsize(width=400, height=300)
window.config(pady=50, padx=50)
# window.grid(widthInc=20, heightInc=20)

PADX_Y = 5

# Boxa unde se introduce valoarea
entry_mile = Entry(width=10)
entry_mile.get()
entry_mile.grid(column=4, row=3, padx=PADX_Y, pady=PADX_Y)

# Valoarea inainte de convertire
valoarea = 0
text_mile = Label(text='Mile')
text_mile.grid(column=5, row=3, padx=PADX_Y, pady=PADX_Y)
text_km = Label(text='Km')
text_km.grid(column=5, row=4)


def command_b():
    """Comanda dupa ce se apasa
    butonul + convertirea valorii
    in km"""
    valoarea = round((float(entry_mile.get()) / 0.621371192), 4)
    text_rezultat.config(text=f'{valoarea}')


def exit_progr():
    sys.exit()


# Butonul
b_calculate = Button(text='Calculeaza', command=command_b)
b_calculate.grid(column=4, row=5)

b_exit = Button(text='Iesire', command=exit_progr)
b_exit.grid(column=4, row=6, padx=PADX_Y, pady=PADX_Y)

# Descrierea in label
text_primul = Label(text=f'Rezultatul este:')
text_primul.grid(column=2, row=4, padx=PADX_Y, pady=PADX_Y)

text_rezultat = Label(text=f'{valoarea}')
text_rezultat.grid(column=4, row=4, pady=PADX_Y, padx=PADX_Y)

window.mainloop()
