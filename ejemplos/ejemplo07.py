# Ejemplo de uso del metodo pack para ubicar los widgets

from tkinter import *

ventana = Tk()
ventana.title("Ejemplo de uso de pack")
ventana.geometry("300x250") # equivalente a ventana.minsize(width=300, height=250)

# Label 1 con colores
lbl_etiqueta1 = Label(ventana, text="Caja 1", bg="#EFBC9B", fg="#B5C18E")
lbl_etiqueta1.pack(ipadx=10, ipady=10, expand=True, anchor=N)

# Label 2 con colores
lbl_etiqueta2 = Label(ventana, text="Caja 2", bg="#D37676", fg="#EBC49F")
lbl_etiqueta2.pack(ipadx=10, ipady=10, expand=True, anchor=S)

ventana.mainloop()

