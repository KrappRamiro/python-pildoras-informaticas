from tkinter import *

root=Tk()
root.attributes('-type', 'dialog') #abrir en floating mode
miFrame=Frame(root)
miFrame.pack()

operacion=""
resultado=0

#------------------ Pantalla -------------------
numeroPantalla=StringVar()
pantalla=Entry(miFrame, textvariable = numeroPantalla) #esta va a ser la pantalla principal de la calculadora
pantalla.grid(row=1, column=1, padx=5, pady=10, columnspan=4) #columnspan me dice cuantas columnas ocupa el elemento
pantalla.config(background="black", fg="#03f943", justify="right")

#--------------- Pulsaciones teclado ---------------------
numeroPantalla.set("0")
def numeroPulsado(num):
#	print("Numero ingresado: " + num)
#	if numeroPantalla.get() == "0":
#		if num==",":
#			numeroPantalla.set("0,")
#		else:
#			numeroPantalla.set(num)
#	else:
#		numeroPantalla.set(numeroPantalla.get() + num)
	global operacion
	if operacion!= "":
		numeroPantalla.set(num)
		operacion=""
	else:
		numeroPantalla.set(numeroPantalla.get() + num)

def limpiarPantalla():
	numeroPantalla.set("0")

#-------------- Funciones -----------------
def suma(num):
	global operacion
	global resultado
	resultado+=float(num)
	operacion="suma"
	numeroPantalla.set(resultado)

def elResultado():
	global resultado
	numeroPantalla.set(resultado+float(numeroPantalla.get()))
#--------------- Fila 1 -----------------------
boton7=Button(miFrame, text="7", width=3, command=lambda:numeroPulsado("7"))
boton7.grid(row=2, column=1)

boton8=Button(miFrame, text="8", width=3, command=lambda:numeroPulsado("8"))
boton8.grid(row=2, column=2)

boton9=Button(miFrame, text="9", width=3, command=lambda:numeroPulsado("9"))
boton9.grid(row=2, column=3)

botonDiv=Button(miFrame, text="/", width=3, command=lambda:numeroPulsado("/"))
botonDiv.grid(row=2, column=4)

#------------ Fila 2 -----------------------
# No anda:
# boton4=Button(miFrame, text="4", width=3, command=numeroPulsado("4")) #command llama a una funcion cada vez que
# se pulsa la tecla, le agrega funcionalidad

# Si anda:
boton4=Button(miFrame, text="4", width=3, command=lambda:numeroPulsado("4")) 
boton4.grid(row=3, column=1)

boton5=Button(miFrame, text="5", width=3, command=lambda:numeroPulsado("5"))
boton5.grid(row=3, column=2)

boton6=Button(miFrame, text="6", width=3, command=lambda:numeroPulsado("6"))
boton6.grid(row=3, column=3)

botonMult=Button(miFrame, text="x", width=3, command=lambda:numeroPulsado("*"))
botonMult.grid(row=3, column=4)

#------------ Fila 3 -----------------------
boton1=Button(miFrame, text="1", width=3, command=lambda:numeroPulsado("1"))
boton1.grid(row=4, column=1)

boton2=Button(miFrame, text="2", width=3, command=lambda:numeroPulsado("2"))
boton2.grid(row=4, column=2)

boton3=Button(miFrame, text="3", width=3, command=lambda:numeroPulsado("3"))
boton3.grid(row=4, column=3)

botonRestar=Button(miFrame, text="-", width=3, command=lambda:numeroPulsado("-"))
botonRestar.grid(row=4, column=4)

#------------ Fila 4 -----------------------
boton0=Button(miFrame, text="0", width=3, command=lambda:numeroPulsado("0"))
boton0.grid(row=5, column=1)

botonComa=Button(miFrame, text=",", width=3, command=lambda:numeroPulsado("."))
botonComa.grid(row=5, column=2)

botonIgual=Button(miFrame, text="=", width=3, command=lambda:elResultado())
botonIgual.grid(row=5, column=3)

botonSuma=Button(miFrame, text="+", width=3, command=lambda:suma(numeroPantalla.get()))
botonSuma.grid(row=5, column=4)

# --------------- Fila 5 -----------
botonClear=Button(miFrame, text="C", width=3, command=limpiarPantalla)
botonClear.grid(row=6, column=1)


root.mainloop()