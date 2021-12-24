import re

lista_nombres= [
	"Sandra 	Dominguez",
	"Sandra 	Lopez",
	"Miguel 	Martin",
	"Agustin 	Lopez",
	"Hernan 	Dominguez",
	"Carlos 	Dominguez",
	"Sandra 	Diaz"
]

#Devuelve todos los nombres que empiezan con Sandra
print("\nNombres que empiezan con Sandra:")
for nombre in lista_nombres:
	if re.findall("^Sandra", nombre): # ^Sandra --> Inicia con Sandra
		print (nombre)

print("\nNombres que terminan con Dominguez")
for nombre in lista_nombres:
	if re.findall("Dominguez$", nombre): # ^Sandra --> Inicia con Sandra
		print (nombre)

lista_generos=[
	'Hombres',
	'Mujeres',
	'mascotas',
	'niños',
	'niñas'
]

# si quiero matchear tanto niños como niñas, hago asi:
for buscando in lista_generos:
	if re.findall("niñ[oa]s", buscando): # ^Sandra --> Inicia con Sandra
		print (buscando)


lista_vehiculos=[
	'auto',
	'locomotora',
	'tren',
	'camion',
	'camión'
]

# Si quiero buscar tanto o como ó, es asi
for buscando in lista_vehiculos:
	if re.findall("cami[oó]n", buscando): # ^Sandra --> Inicia con Sandra
		print (buscando)