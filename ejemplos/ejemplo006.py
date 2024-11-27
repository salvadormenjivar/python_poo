# Usamos tkinter para agregar una aplicacion de escritorio
import tkinter

# Creamos un objeto a partir de la clase Tk
# main o root es el nombre que generalmente se usa para esta ventana
ventana = tkinter.Tk()

# Definimos el tamano de la ventana
ventana.minsize(width=500, height=500)

# Le agregamos un titulo a la ventana
ventana.title("Ejemplo 1")

# Agregamos widgets, componentes o elementos a un formulario de esta forma:
lbl_titulo = tkinter.Label(ventana, text="Salvador")

# El metodo pack es una de las formas para ubicar los widgets dentro de nuestra ventana:
lbl_titulo.pack()

# Agregar una imagen como etiqueta
# Cargamos la imagen:
logo = tkinter.PhotoImage(file="img.png")
logo_redimensionado = logo.subsample(2) # Redimensionando a la mitad de la imagen
lbl_logo = tkinter.Label(ventana, image=logo_redimensionado)
lbl_logo.pack()

# pillow

# LLamamos a este metodo para mantener la ventana activa
# Generalmente esta linea va al final del codigo
ventana.mainloop()