from tkinter import *
from tkinter import filedialog

root=Tk();  root.attributes('-type', 'dialog')

def abreFichero():
    fichero=filedialog.askopenfilename(
        title="Abrir",
        initialdir="~",
        filetypes=(
            ("Ficheros de excel", "*.xlsx"),
            ("Archivos pdf", "*.pdf"),
            ("Ficheros de texto", "*.txt"),
            ("Todos los ficheros", "*.*")
        )
    )
    print(fichero)


Button(root, text="Abrir fichero", command=abreFichero).pack()








root.mainloop()