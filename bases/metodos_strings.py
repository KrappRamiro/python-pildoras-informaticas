#miString= "hola mundo!"
#miString.upper()        # Pasamos todo a MAYUSCULAS
#miString.lower()        # Pasamos todo a minusculas
#miString.capitalize()   # Ponemos el primer char en Mayuscula
#miString.count()        # Cuenta la cantidad de ocurrencias de un string 
#miString.find()         # Busca un string dentro del string (como un grep)
#miString.isdigit()      # Pregunta si es un valor numerico
#miString.isalum()       # Pregunta si es alfanumerico
#miString.isalpha()      # Pregunta si hay solo letras
#miString.split()        # Separa por palabras usando espacios
#miString.strip()        # Borrar los espacios sobrantes al principio y al final
#miString.replace()      # Remplaza una palabra por otra
#miString.rfind()        # Reverse find, devuelve el indice pero contando desde atras

nombreUsuario = input("Ingresa tu nombre de usuario: ")
print ("El nombre es:", nombreUsuario.capitalize())

edad = input ("Introduce tu edad: ")
print(edad.isdigit())
print("Programa finalizado")
