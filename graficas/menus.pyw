from tkinter import*
from tkinter import messagebox
root = Tk()
root.attributes('-type', 'dialog')

def infoAdicional():
    messagebox.showinfo("Editor de texto de Krapp", "Editor de texto de Krapp Ramiro, version 1.0 2021")
    
def avisoLicencia():
    messagebox.showwarning("Licencia", "Producto bajo licencia GNU GPL v2.0")

def salirAplicacion():
    valor=messagebox.askquestion("Salir", "¿Deseas salir de la aplicacion?")
    if valor=="yes":
        root.destroy()

# Esta seria una version alternativa, con "Ok" & "Cancel" en vez de "yes" & "no" 
def salirAplicacion2(): 
    valor=messagebox.askquestion("Salir", "¿Deseas salir de la aplicacion?")
    if valor==True:
        root.destroy()

def cerrarDocumento():
    valor=messagebox.askretrycancel("Reintentar", "No es posible cerrar. Documento Bloqueado")
    if valor==True:
        cerrarDocumento()
    else:
        root.destroy()

barraMenu=Menu(root)
root.config(menu=barraMenu, width=500, height=300)

menuArchivo=Menu(barraMenu, tearoff=0) # tearoff=0 saca la barra ---------
menuArchivo.add_command(label="Nuevo")
menuArchivo.add_command(label="Guardar")
menuArchivo.add_command(label="Guardar como")
menuArchivo.add_separator()
menuArchivo.add_command(label="Cerrar", command=cerrarDocumento)
menuArchivo.add_command(label="Salir", command=salirAplicacion)

menuEdicion=Menu(barraMenu, tearoff=0)
menuEdicion.add_command(label="Deshacer")
menuEdicion.add_command(label="Rehacer")
menuEdicion.add_separator()
menuEdicion.add_command(label="Copiar")
menuEdicion.add_command(label="Pegar")
menuEdicion.add_command(label="Cortar")
menuEdicion.add_separator()
menuEdicion.add_command(label="Buscar")
menuEdicion.add_command(label="Buscar y reemplazar")

menuHerramientas=Menu(barraMenu)

menuAyuda=Menu(barraMenu, tearoff=0)
menuAyuda.add_command(label="Introducción al programa")
menuAyuda.add_command(label="Mostrar todos los comandos")
menuAyuda.add_command(label="Ver videos explicatorios")
menuAyuda.add_separator()
menuAyuda.add_command(label="Licencia", command=avisoLicencia)
menuAyuda.add_command(label="Acerca de", command=infoAdicional)


barraMenu.add_cascade(label="Archivo", menu=menuArchivo)
barraMenu.add_cascade(label="Edicion", menu=menuEdicion)
barraMenu.add_cascade(label="Herramientas", menu=menuHerramientas)
barraMenu.add_cascade(label="Ayuda", menu=menuAyuda)







root.mainloop()