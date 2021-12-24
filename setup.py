from setuptools import setup

#solamente name, version, desc, author y packages son obligatorios
setup(
    name= "Paquete_calculos",
    version="1.1",
    desc="Paquete de calculos",
    author="Krapp Ramiro",
    author_email="krappramiro.jpg@gmail.com",
    url="www.krappramiro.com",
    packages=["calculos", "calculos.redondeo_potencia", "calculos.basicos"]
)