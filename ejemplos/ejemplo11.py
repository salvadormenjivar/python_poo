from tkinter import *

ventana = Tk()
ventana.title("Ejemplo uso de grid")
ventana.geometry("220x150")

ventana.grid_columnconfigure(0, weight=1)
ventana.grid_rowconfigure(0,weight=1)

lbl_usuario = Label(ventana, text="Usuario", width=40, borderwidth=2)
lbl_usuario.grid(column=0, row=0, sticky="nsew")

txt_usuario = Entry()
txt_usuario.grid(column=0, row=1, padx=10, sticky=W)

lbl_pass = Label(ventana, text="Password")
lbl_pass.grid(column=0, row=2, padx=10, pady=5, sticky=W)

txt_pass = Entry(show="*")
txt_pass.grid(column=0, row=3, padx=10, sticky=W)

Button(text="Iniciar Sesion").grid(column=0, row=4, sticky=W, padx=10, pady=5)

ventana.mainloop()