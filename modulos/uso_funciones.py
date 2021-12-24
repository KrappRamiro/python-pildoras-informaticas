# import funciones_matematicas

# funciones_matematicas.sumar(7,5)
# funciones_matematicas.sumar(2,1)
# funciones_matematicas.sumar(9,4)

# Resulta que hacerlo asi es muy engorroso, porque hay que poner
# funciones_matematicas todo el rato.


# Hay una forma mejor que es la siguiente
# from funciones_matematicas import sumar

# sumar(7,5)
# sumar(2,1)
# sumar(9,4)

# Pero si quiero hacer restar(7,5) no puedo


# Hay otra forma que es esta, que importa todo todo todo
from funciones_matematicas import *
sumar(7,5)
restar(3,2)
