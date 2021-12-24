import sqlite3

miConexion = sqlite3.connect("Segunda_bbdd.sqlite3")
miCursor = miConexion.cursor()

miCursor.execute('''
	CREATE TABLE productos (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		nombre_articulo VARCHAR(50) UNIQUE,
		precio INTEGER,
		seccion VARCHAR(20)
	)
''')

productos=[
	("pelota", 20, "jugueteria"),
	("pantalón", 15, "confeccion"),
	("destornillador", 25, "ferreteria"),
	("jarrón", 45, "ceramica")
]

miCursor.executemany("INSERT INTO productos VALUES (NULL,?,?,?)", productos)

miConexion.commit()
miConexion.close()