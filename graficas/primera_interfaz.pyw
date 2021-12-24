from tkinter import *

raiz=Tk() #creamos la raiz
raiz.attributes('-type', 'dialog') #abrir en floating mode
raiz.title("Primera ventana")
raiz.resizable(True, True) # resizable en: width, heigth
#app_icon = 'electronica.ico'
#raiz.iconbitmap('@' + app_icon)
raiz.geometry("650x350") #geometria, ancho x alto
raiz.config(bg="green") #fondo = verde

miFrame=Frame()
#miFrame.pack(side="right", anchor="n") # n de north, lado derecho al norte, esquina superior derecha
#miFrame.pack(fill="x") #redimensiona e el eje x
#miFrame.pack(fill="y", expand=True)
#miFrame.pack(fill="both", expand=True)
miFrame.pack()
miFrame.config ( # todo esto de aca se lo podria aplicar a la raiz
	bg="red",
	width="350",
	height="150",
	bd="35",
	relief="sunken",#cambio el borde por el modo sunken
	cursor="hand2",
)
raiz.mainloop() # loopeamos la ventana, esto siempre en el final