import pickle
class Persona:
    def __init__(self, nombre, genero, edad):
        self.nombre=nombre
        self.genero=genero
        self.edad=edad
        print("Se ha creado una persona nueva con el nombre de:", self.nombre)
    
    def __str__(self): #devuelve la info del objeto en str
        return "{} {} {}".format(self.nombre, self.genero, self.edad)

class ListaPersonas: #hago una clase llamada ListaPersonas
    personas=[]

    def __init__(self):
        # en el constructor, hago que me abra un fichero externo, y dentro del codigo lo voy
        # a llamar como listaDePersonas.
        # listaDePersonas va a ser lo que hay en el fichero externo
        listaDePersonas=open("ficheroExterno", "ab+")
        listaDePersonas.seek(0)
        
        try:
            # dentro del atributo personas guardo el contenido del fichero externo 
            self.personas=pickle.load(listaDePersonas)
            print("Se cargaron {} personas del fichero externo".format(len(self.personas)))
            # dentro del {} se va a imprimir lo que se declaro dentro del format(), en este caso
            # la longitud de personas, que es igual a la longitud del fichero externo
        except:
            print("--- Warning: El fichero esta vacio ---")
        finally:
            listaDePersonas.close()
            del(listaDePersonas)

    def agregarPersonas(self, persona):
        # esto hace 2 cosas:
        # 1- guarda en la lista personas la persona pasada como parametro
        # 2- guarda en el fichero externo la persona pasada como parametro
        self.personas.append(persona)
        self._guardarPersonasEnFicheroExterno()

    def mostrarPersonas(self):
        #imprime todas las personas
        for i in self.personas:
            print(i)
    
    def _guardarPersonasEnFicheroExterno(self):
        # esto abre el fichero externo en modo lectura, agarra personas[] y lo dumpea dentro del
        # fichero externo
        listaDePersonas=open("ficheroExterno", "wb")
        pickle.dump(self.personas, listaDePersonas)
        listaDePersonas.close()
        del(listaDePersonas)
    
    def mostrarInfoFicheroExterno(self):
        print("La info del fichero externo es la siguiente: ")
        for i in self.personas:
            print(i)

miLista = ListaPersonas()
miPersona=Persona("Ramiro", "Masculino", 17)
miLista.agregarPersonas(miPersona)

miLista.mostrarInfoFicheroExterno()
