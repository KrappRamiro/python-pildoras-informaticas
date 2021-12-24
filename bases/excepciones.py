def divide():
    try:
        n1=float(input("Introduce el n1: "))
        n2=float(input("Introduce el n2: "))
        print ("Resultado: " + str(n1/n2))
    except ValueError:
        print("El valor introducido es erroneo")
    except ZeroDivisionError:
        print("No se puede dividir por 0")
    except:
        print("Ha ocurrido un error inesperado :(")
    finally:
        print("calculo finalizado")

divide()
