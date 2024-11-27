from tkinter import *

ventana = Tk()
ventana.title("Inicio de sesion")
ventana.geometry("250x150")

# Los nombres de las etiquetas van a iniciar con lbl
lbl_usuario = Label(ventana, text="Usuario", font=("Gill Sans MT", 12))
lbl_usuario.pack(padx=10, pady=5, anchor=W)

# Las cajas de texto van iniciar con txt
txt_usuario = Entry()
txt_usuario.pack(padx=10, anchor=W, fill=X) # 240 px de ancho

lbl_pass = Label(ventana, text="Password:", font=("Gill Sans MT", 12))
lbl_pass.pack(padx=10, pady=5, anchor=W)

txt_pass=Entry(show="*") # Con esta propiedad le indico que cuando se escriba muestra asteriscos
txt_pass.pack(padx=10, anchor=W, fill=X)

# Los botones van a iniciar con btn
btn_iniciar_sesion = Button(text="Iniciar Sesion")
btn_iniciar_sesion.pack(padx=10, pady=10, anchor=E)

ventana.mainloop()