# Ejemplo de uso del metodo pack para ubicar los widgets

from tkinter import *

from tkinter import font

ventana = Tk()
ventana.title("Ejemplo de uso de pack")
ventana.geometry("300x250") # equivalente a ventana.minsize(width=300, height=250)

lbl_etiqueta1 = Label(ventana, text="Caja 1", bg="#A5DD9B", fg="#F2C18D", font=("Garamond", 20))
lbl_etiqueta1.pack(ipadx=20, ipady=20, expand=True, fill=BOTH, side=LEFT)

lbl_etiqueta2 = Label(ventana, text="Caja 1", bg="#A5DD9B", fg="#F2C18D", font=("Garamond", 20))
lbl_etiqueta2.pack(ipadx=20, ipady=20, expand=True, fill=BOTH, side=RIGHT)

fuentes_disponibles = font.families()
print(fuentes_disponibles)

ventana.mainloop()