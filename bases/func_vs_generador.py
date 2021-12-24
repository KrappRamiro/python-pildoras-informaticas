# Quiero una funcion que me devuelva una lista de numeros pares


# Una funcion normal
def generaPares(limite):
    num=1
    miLista=[]
    while num <= limite:
        miLista.append(num*2)
        num+=1
    return miLista

# Una funcion generadora
def generaPares_generadora(limite):
    num=1
    miLista=[]
    while num <= limite:
        yield num*2
        num+=1


# Llamo a la funcion normal
print(generaPares(6));

# Llamo a la funcion generadora para que me imprima la lista entera
devuelvePares=generaPares_generadora(5)
#for i in devuelvePares:
#    print (i)


# Llamo a la funcion generadora para que me vaya imprimiendo uno por uno
print(next(devuelvePares))
print(next(devuelvePares))
print(next(devuelvePares))
print(next(devuelvePares))
print(next(devuelvePares))
