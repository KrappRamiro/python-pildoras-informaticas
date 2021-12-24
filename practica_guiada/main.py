from tkinter import *
from tkinter import messagebox
import sqlite3
import os

#TODO: Error handling
#TODO: Pasarlo a ingles y camel_case

print("-----------------------------------------------")
root = Tk()
root.attributes('-type', 'dialog')  # abrir en floating mode

user_id = IntVar()
user_firstname = StringVar()
user_lastname = StringVar()
user_password = StringVar()
user_city = StringVar()
user_street = StringVar()
user_streetnumber = IntVar()
user_postalcode = IntVar()
user_comments = StringVar()


def show_info():
	messagebox.showinfo("Interfaz grafica base de datos",
						"Krapp Ramiro, version 1.0 2021")


def show_license():
	messagebox.showwarning("Licencia", "Producto bajo licencia GNU GPL v2.0")


def exit_program():
	valor = messagebox.askquestion("Salir", "¿Deseas salir de la aplicacion?")
	if valor == "yes":
		root.destroy()


def borrar_campos():
	user_id.set(0)
	user_firstname.set("")
	user_lastname.set("")
	user_password.set("")
	user_city.set("")
	user_street.set("")
	user_streetnumber.set(0)
	user_postalcode.set(0)
	user_comments.set("")

def connect_to_database():
	print("Starting connection with database")
	# Check whether the specified path is an existing file
	path = './database.sqlite3'
	databaseExisted = os.path.isfile(path)

	# Creates the connection with the database, creates the file with the table if .sqlite3 does not exist
	db_connection = sqlite3.connect("database.sqlite3")
	db_cursor = db_connection.cursor()

	if (databaseExisted == False):
		print("Database not found, creating a new one")
	else:
		print("Database found")

	db_cursor.execute('''
		CREATE TABLE IF NOT EXISTS users (
			user_id 		INTEGER 	PRIMARY KEY AUTOINCREMENT,
			first_name		VARCHAR(30) NOT NULL,
			last_name		VARCHAR(30) NOT NULL,
			password 		VARCHAR(50) NOT NULL,
			comment VARCHAR(30)
		)'''
	)
	db_cursor.execute('''
		CREATE TABLE IF NOT EXISTS addresses (
			id 				INTEGER PRIMARY KEY AUTOINCREMENT,
			owner_id		INTEGER NOT NULL,
			city			VARCHAR(40) NOT NULL,
			street			VARCHAR(40) NOT NULL,
			street_number	INTEGER 	NOT NULL,
			postal_code 	INTEGER 	NOT NULL,
			FOREIGN KEY(owner_id) REFERENCES users(user_id) ON DELETE CASCADE
		)'''
	)



def create():
	db_connection= sqlite3.connect("database.sqlite3")
	db_cursor = db_connection.cursor()
	print(
		"Recieved the following arguments:\nName:", user_firstname.get(), 
		"\nSurname:", user_lastname.get(), 
		"\nPassword", user_password.get() #Habria que encriptar esto :/
	)
	db_cursor.execute('''
		INSERT INTO users
		VALUES(?,?,?,?,?)''',(None,user_firstname.get(),user_lastname.get(),user_password.get(), None)
	)
	db_connection.commit()

def read():
	db_connection= sqlite3.connect("database.sqlite3")
	db_cursor = db_connection.cursor()
	print("Buscando al usuario con la id: ", user_id.get())
	some_name="Eduardo"
	db_cursor.execute('''
		SELECT user_id,first_name,last_name, password
		FROM users
		WHERE user_id = ?''',(user_id.get(),)
	)
	user_data=db_cursor.fetchall()
	for user in user_data:
		user_id.set(user[0])
		user_firstname.set(user[1])
		user_lastname.set(user[2])
		user_password.set(user[3])
	db_connection.commit()

def update():
	db_connection= sqlite3.connect("database.sqlite3")
	db_cursor = db_connection.cursor()
	print(
		"Recieved the following arguments:\nName:", user_firstname.get(), 
		"\nSurname:", user_lastname.get(), 
		"\nPassword", user_password.get() #Habria que encriptar esto :/
	)
	db_cursor.execute('''
		UPDATE users
		SET first_name=?, last_name=?, password=?
		WHERE user_id=?''',(user_firstname.get(),user_lastname.get(),user_password.get(), user_id.get())
	)
	db_connection.commit()

def delete():
	db_connection= sqlite3.connect("database.sqlite3")
	db_cursor = db_connection.cursor()
	db_cursor.execute("DELETE FROM users WHERE user_id = ?",(user_id.get(),))
	print("deleted the user with the ID: ", user_id.get())
	db_connection.commit()

mi_frame = Frame(root)
mi_frame.config(
	width=300,
	height=400
)
mi_frame.pack()

frame_datainput = Frame(mi_frame)
frame_datainput.pack()

frame_buttons = Frame(mi_frame)
frame_buttons.pack()

barra_menu = Menu(root)
root.config(menu=barra_menu, width=500, height=300)

# ------------- Definicion de la parte de entrada de datos ---------------
# User_id
Label(frame_datainput, text="user_id").grid(row=0, column=0)
Entry(frame_datainput, textvariable=user_id).grid(
	row=0, column=1, pady=10, padx=5)

# Nombre
Label(frame_datainput, text="Nombre").grid(row=1, column=0)
Entry(frame_datainput, textvariable=user_firstname).grid(
	row=1, column=1, pady=10, padx=5)

# Apellido
Label(frame_datainput, text="Apellido").grid(row=2, column=0)
Entry(frame_datainput, textvariable=user_lastname).grid(
	row=2, column=1, pady=10, padx=5)

# Contraseña
Label(frame_datainput, text="Contraseña").grid(row=3, column=0)
passw = Entry(frame_datainput, textvariable=user_password)
passw.grid(row=3, column=1, pady=10, padx=5)
passw.config(show="*")

# Ciudad
Label(frame_datainput, text="Ciudad")	.grid(row=4, column=0)
Entry(frame_datainput, textvariable=user_city).grid(
	row=4, column=1, pady=10, padx=5)

# Calle
Label(frame_datainput, text="Calle")	.grid(row=5, column=0)
Entry(frame_datainput, textvariable=user_street).grid(
	row=5, column=1, pady=10, padx=5)

# Altura
Label(frame_datainput, text="Altura")	.grid(row=6, column=0)
Entry(frame_datainput, textvariable=user_streetnumber).grid(
	row=6, column=1, pady=10, padx=5)

# Codigo postal
Label(frame_datainput, text="Código\nPostal").grid(row=7, column=0)
Entry(frame_datainput, textvariable=user_postalcode).grid(
	row=7, column=1, pady=10, padx=5)

# Comentarios
Label(frame_datainput, text="Comentarios")	.grid(row=8, column=0)
comentario = Text(frame_datainput, width=25, height=5)
comentario.grid(row=8, column=1, pady=10, padx=5)
scrollVert = Scrollbar(frame_datainput, command=comentario.yview)
scrollVert.grid(row=8, column=2, sticky="nsew")
comentario.config(yscrollcommand=scrollVert.set)

# ----------------- Definicion de la parte de los botones CRUD -------------------
# TODO Faltan poner los commands!!!
button_create = Button(frame_buttons, text="Create", command=lambda:[create(),borrar_campos()])
button_create.grid(row=0, column=0)

button_read = Button(frame_buttons, text="Read", command=lambda:read())
button_read.grid(row=0, column=1)

button_update = Button(frame_buttons, text="Update", command=lambda:update())
button_update.grid(row=0, column=2)

button_delete = Button(frame_buttons, text="Delete", command=lambda:delete())
button_delete.grid(row=0, column=3)

# Definicion de los cascades
# ------------------- Menu BBDD ------------------
menu_bbdd = Menu(barra_menu, tearoff=0)
menu_bbdd.add_command(label="Conectar", command=connect_to_database)
menu_bbdd.add_command(label="Salir", 	command=exit_program)

# ------------------- Menu Borrar ------------------
menu_borrar = Menu(barra_menu, tearoff=0)
menu_borrar.add_command(label="borrar_campos", command=borrar_campos)

# ------------------- Menu Ayuda ------------------
menu_ayuda = Menu(barra_menu, tearoff=0)
menu_ayuda.add_command(label="Acerca de", command=show_info)
menu_ayuda.add_command(label="Licencia", command=show_license)


# Esto añade los cascades de la parte de arriba de la interfaz, los cuales ya fueron definidos
barra_menu.add_cascade(label="BBDD",	menu=menu_bbdd)
barra_menu.add_cascade(label="Borrar",	menu=menu_borrar)
barra_menu.add_cascade(label="Ayuda",	menu=menu_ayuda)


root.mainloop()
