from tkinter import *
root = Tk()
root.attributes('-type', 'dialog') #abrir en floating mode

def imprimir():
	if varOpcion.get()==1:
		print("Se ha elegido la opcion masculino")
		etiqueta.config(text="Se ha elegido la opcion masculino")
	elif varOpcion.get()==2:
		print("Se ha elegido la opcion femenino")
		etiqueta.config(text="Se ha elegido la opcion femenino")
varOpcion=IntVar()
Label(root, text="Genero: ").pack()
Radiobutton(
	root,
	text="Masculino",
	variable=varOpcion,
	value=1,
	command=lambda:imprimir()
).pack()
Radiobutton(
    root,
    text="Femenino",
    variable=varOpcion,
    value=2,
    command=lambda:imprimir()
).pack()

etiqueta=Label(root)
etiqueta.pack()
root.mainloop()