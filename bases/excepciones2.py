def evaluaEdad (edad):
    if edad < 0:
        raise TypeError ("No se permiten edades negativas")
    if edad < 20:
        return "Eres muy joven"
    if edad < 40:
        return "Eres joven"
    if edad < 65:
        return "Eres maduro"
    if edad < 100:
        return "Tas viejo mostro"

print (evaluaEdad(-1))
