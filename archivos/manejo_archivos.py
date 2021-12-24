from io import open

#Escritura de archivos
archivo_texto=open("archivo.txt", "w") #abro en modo write
frase = "Estupendo dia para estudiar python \nel miercoles"
archivo_texto.write(frase)
archivo_texto.close()

#Lectura de archivos
archivo_texto=open("archivo.txt", "r") #abro en modo read
texto=archivo_texto.read()
archivo_texto.close()
print(texto)

# Lectura de archivos por lineas 
archivo_texto=open("archivo.txt", "r") #abro en modo read
lineas_texto = archivo_texto.readlines() #lineas de texto es una lista[], lee linea x linea
archivo_texto.close()
print(lineas_texto) #imprimo toda la lista
print(lineas_texto[0]) #imprimo la primera linea

# Apertura en modo append
archivo_texto=open("archivo.txt", "a") #abro en modo append
archivo_texto.write("\nSiempre es un buen dia para usar Linux :)")
archivo_texto.close()

# Leer a partir del mitad del archivo
archivo_texto=open("archivo.txt", "r")
print("\n----------------------\n")
archivo_texto.seek(len( archivo_texto.read() )/2)
print(archivo_texto.read())
archivo_texto.close()

# Leer a partir del final de la primera linea
archivo_texto=open("archivo.txt", "r")
print("\n----------------------\n")
archivo_texto.seek (
    len(archivo_texto.readline())
)
print(archivo_texto.read())
archivo_texto.close()

# Leer a partir de un caracter
archivo_texto=open("archivo.txt", "r")
print("\n----------------------\n")
archivo_texto.seek (
    len(archivo_texto.readline())
)
print(archivo_texto.read())
archivo_texto.close()

# Abrir en read/write
archivo_texto=open("archivo.txt", "r+")
print("\n----------------------\n")
archivo_texto.close()

# Modificar una linea en especifico
archivo_texto=open("archivo.txt", "r+")
print("\n----------------------\n")

lista_texto=archivo_texto.readlines() # guardo el contenido del archivo en una lista llamada lista_texto
lista_texto[1] = "Esta linea fue modificada desde el exterior\n" # Modifico la linea 2 de esa lista
archivo_texto.seek(0) 
archivo_texto.writelines(lista_texto) # Sobreescribo los contenidos del archivo con mi lista modificada
archivo_texto.seek(0) 
print(archivo_texto.read())

archivo_texto.close()