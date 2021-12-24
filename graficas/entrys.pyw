from tkinter import *

root = Tk()
root.attributes('-type', 'dialog') #abrir en floating mode

miNombre=StringVar()

miFrame=Frame(root, width=800, height =600)
miFrame.pack()

Label(miFrame, text="Nombre")		.grid(row=0, column=0)
Label(miFrame, text="Contraseña")	.grid(row=1, column=0)
Label(miFrame, text="Apellido")		.grid(row=2, column=0)
Label(miFrame, text="Direccion")	.grid(row=3, column=0)
Label(miFrame, text="Comentarios")	.grid(row=4, column=0)

Entry(miFrame, textvariable=miNombre).grid(row=0, column=1, pady=10, padx=5)
passw=Entry(miFrame)
passw.grid(row=1, column=1, pady=10, padx=5)
passw.config(show="*")
Entry(miFrame).grid(row=2, column=1, pady=10, padx=5)
Entry(miFrame).grid(row=3, column=1, pady=10, padx=5)

comentario=Text(miFrame, width=25, height=5)
comentario.grid(row=4, column=1, pady=10, padx=5)
scrollVert=Scrollbar(miFrame, command=comentario.yview)
scrollVert.grid(row=4, column=2, sticky="nsew")
comentario.config(yscrollcommand=scrollVert.set)

def codigoBoton():
	miNombre.get

botonEnvio=Button(root, text="Enviar", command=codigoBoton)
botonEnvio.pack()
root.mainloop()