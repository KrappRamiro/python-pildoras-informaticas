import re

lista_nombres= [
	"sandra 	Dominguez",
	"Sandra 	Lopez",
	"Miguel 	Martin",
	"Agustin 	Lopez",
	"Hernan 	Dominguez",
	"Carlos 	Dominguez",
	"Sandra 	Diaz",
	"Lara		Dominguez",
	"Jara		Hernandez",
	"7Jorge		Fernandez"
]

#Buscar todas las sandras:
for i in range(len(lista_nombres)):
	if re.match("Sandra", lista_nombres[i], re.IGNORECASE): #ignore case hace que sea case-unsensitive
		print(f"Se encontro el nombre en la posicion {i}")

print("--------------------------------------------------------------")

#Buscar todas las personas con nombres de 4 char terminados en ara (Lara, Jara, Para)
for i in range(len(lista_nombres)):
	if re.match(".ara", lista_nombres[i], re.IGNORECASE): #ignore case hace que sea case-unsensitive
		print(f"Se encontro el nombre en la posicion {i}")

print("--------------------------------------------------------------")

#Buscar todas las personas que su nombre empieze con un numero (digito)
for i in range(len(lista_nombres)):
	if re.match("\d", lista_nombres[i], re.IGNORECASE): #ignore case hace que sea case-unsensitive
		print(f"Se encontro el nombre en la posicion {i}")

print("--------------------------------------------------------------")

#Buscar si x cosa aparece en un string
# Si encuentra dominguez en el string, devuelve true, en caso contrario devuelve false
if re.search("Dominguez",lista_nombres[4]): print("La persona es un Dominguez")
else: print("La persona no es un dominguez")