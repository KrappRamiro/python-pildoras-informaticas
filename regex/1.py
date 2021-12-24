import re

myString = "Vamos a aprender expresiones regulares. Python es un lenguaje de sintaxis sencilla el cual es sencillo de aprender. Por mi parte, aprenderlo me resulto algo muy facil"
print(re.search("aprender", myString)) # Devuelve match
print(re.search("apreeeeeender", myString)) # devuelve None



textoBuscar="aprender"
if re.search(textoBuscar, myString) is not None:
	print ("Encontre el texto")
else:
	print ("no he encontrado el texto")



textoEncontrado=re.search(textoBuscar, myString)
print(textoEncontrado.start()) 	#me dice en que caracter empieza lo que encontró, printea 8
print(textoEncontrado.end())	#me dice en que caracter termina lo que encontró, printea 16
print(textoEncontrado.span())	#me devuelve una tupla que contiene end() y start() --> (8, 16)

print(re.findall(textoBuscar, myString)) # Devuelve todas las ocurrencias del texto a buscar --> ['Python', 'Python']
print (f"Se ha encontrado", len(re.findall(textoBuscar,myString)), "veces")