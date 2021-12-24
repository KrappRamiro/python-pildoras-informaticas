#Labels:
## text --> 	Texto que se muestra en el label
## anchor --> 	Controla la posicion, center x default
## bg --> 		Color de fondo
## bitmap --> 	Mapa de bits que se mostrara como grafico
## bd --> 		Grosor del borde
## font -->		Tipo de fuente
## fg --> 		Color de la fuente
## width --> 	Ancho del label en caracteres (NO PIXELES)
## height -->	Altura del label en caracteres (NO PIXELES)
## image --> 	Muestra imagen en el label en vez de texto
## justify --> 	Justifica el texto

from tkinter import *

root = Tk()
root.attributes('-type', 'dialog') #abrir en floating mode

miFrame=Frame(root,width=500, height=400)
miFrame.pack()

miImagen=PhotoImage(file="pepe_thinkpad.png")

# Version larga, en la que armamos una variable miLabel
## miLabel=Label(miFrame, text="Hola alumnos de python")
## miLabel.place(x=100, y=200)

# Si no vamos a usar miLabel en ninguna otra parte del codigo
# podemos hacer esto que es una version corta
## Label(miFrame, text="Hola alumnos de python", fg="red", font=("monospace",18)).place(x=100, y=200)

Label(miFrame, image=miImagen).place(x=100, y=200)

root.mainloop()