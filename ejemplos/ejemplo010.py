from tkinter import *
# Ejemplo del uso de place
ventana = Tk()

ventana.title("Ejemplo del uso de place")
ventana.geometry("300x100")

lbl_nombre = Label(ventana, text="Nombre")
lbl_nombre.place(x=10, y=10)

ventana.mainloop()