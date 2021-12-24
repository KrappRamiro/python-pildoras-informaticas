from tkinter import*
root = Tk()
root.attributes('-type', 'dialog')  # abrir en floating mode

playa = IntVar()
montana = IntVar()
rural = IntVar()


def opcionesViaje():
    opcion_escogida = "Opciones escogidas: "
    if (playa.get() == 1):
        opcion_escogida += "playa, "
    if (montana.get() == 1):
        opcion_escogida += "montaña, "
    if (rural.get() == 1):
        opcion_escogida += "rural"
    textoFinal.config(text=opcion_escogida)


foto = PhotoImage(file="avion.png")
Label(root, image=foto).pack()

frame = Frame(root)
frame.pack()

Label(frame, text="Elige destinos", width=50).pack()
Checkbutton(
    frame,
    text="Playa",
    variable=playa,
    onvalue=1,
    offvalue=0,
    command=opcionesViaje
).pack()
Checkbutton(
    frame,
    text="Montaña",
    variable=montana,
    onvalue=1,
    offvalue=0,
    command=opcionesViaje
).pack()
Checkbutton(
    frame,
    text="Turismo rural",
    variable=rural,
    onvalue=1,
    offvalue=0,
    command=opcionesViaje
).pack()

textoFinal = Label(frame)
textoFinal.pack()


root.mainloop()
