import pickle
# Escribir en binario  a un archivo
lista_nombres = ["Pedro", "Ana", "María", "Isabel"]
fichero_binario= open("lista_nombres", "wb")
pickle.dump(lista_nombres, fichero_binario)
fichero_binario.close()

# Leer un archivo binario
fichero=open("lista_nombres", "rb")
lista=pickle.load(fichero)
print(lista_nombres)