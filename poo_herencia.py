#LA HERENCIA:

# Consiste en la reutilizacion de codigo en caso de crear objetos similares

#caracteristicas en comun de los objetos
#comportamientos en comun de los objetos
#clase padre o superclase agrupa caracteristicas y comportamientos en comun

class Vehiculos():

    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False

    
    def arrancar(self):

        self.enmarcha = True

    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True

    def  estado(self):
        print("marca: ", self.marca, "\n Modelo: ",self.modelo,"\n En Marcha: ", self.enmarcha, "\n Acelerando: ",self.acelera,"\n Frenando: ", self.frena)


class Moto(Vehiculos):#Esta es la manera de heredar. Nombre de la clase y entre parentesis el nombre de la clase que va ha heredar
    pass

miMoto = Moto("Honda","CBR")
miMoto.estado()
        
        
