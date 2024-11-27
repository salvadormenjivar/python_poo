from tkinter import *

def ver_seleccionados():
    resultado = ""
    if programacion.get() == 1:
        resultado += " Programacion "
        # resultado = resultado + " Programacion "
    if redes.get() == 1:
        resultado += " Redes "
    if bases_datos.get() == 1:
        resultado += " Bases datos "
    lbl_resultado.config(text=resultado)

# En este ejemplo aprenderemos el uso de checkbox
ventana = Tk()
ventana.title("Uso de checkbox")
ventana.config(width=500, height=500)
ventana.config(padx=20, pady=20)

lbl_pregunta = Label(text="Seleccione el area de tu conocimiento")
lbl_pregunta.grid(column=0, row=0)

# Para los checkbox vamos a usar chk para asignar un nombre
# Para obtener el valor de un checkbox tkinter me provee de 4 clases:
# IntVar()    StringVar()    DoubleVar()   BooleanVar
programacion=IntVar()
chk_programacion = Checkbutton(text="Programacion", variable=programacion, onvalue=1, offvalue=0)
chk_programacion.grid(column=0, row=1, sticky=W)

redes = IntVar()
chk_redes = Checkbutton(text="Redes", variable=redes, onvalue=1, offvalue=0)
chk_redes.grid(column=0, row=2, sticky = W)

bases_datos = IntVar()
chk_bases_datos = Checkbutton(text="Bases de datos", variable=bases_datos, onvalue=1, offvalue=0)
chk_bases_datos.grid(column=0, row=3, sticky=W)

btn_aceptar = Button(text="Aceptar", command=ver_seleccionados)
btn_aceptar.grid(column=0, row=4, sticky=W)

lbl_resultado = Label(text="")
lbl_resultado.grid(column=0, row=5, sticky=W)

ventana.mainloop()

















