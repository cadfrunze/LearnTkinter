import tkinter as tk
import turtle

window = tk.Tk()
window.title(string='Prima fereastra')
window.minsize(width=500, height=500)

eticheta = tk.Label(text='Prima eticheta')
eticheta.pack()

tim = turtle.Turtle()
tim.write(arg='dsdsds')

window.mainloop()

