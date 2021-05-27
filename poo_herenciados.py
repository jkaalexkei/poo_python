#Herencia:

#sobreescritura de metodos
# Herencia simple y multiple


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

class Furgoneta(Vehiculos):
    
    def carga(self,cargar):
        self.cargado = cargar

        if(self.cargado):
            return "esta cargado"
        else:
            return "no esta cargado"


class Moto(Vehiculos):#Esta es la manera de heredar. Nombre de la clase y entre parentesis el nombre de la clase que va ha heredar
    
    #propiedad propia de Moto
    caballito = ""

    #metodo unico para moto
    def hace_caballito(self):
        self.caballito = "Voy haciendo caballito"
    
    def estado(self):#sobreescritura de metodo y a la hora de la llamada se ejecutara el metodo correspondiente al objeto que la realiza
        print("marca: ", self.marca, "\n Modelo: ",self.modelo,"\n En Marcha: ", self.enmarcha, "\n Acelerando: ",self.acelera,"\n Frenando: ", self.frena, "\n ", self.caballito)

class VehiculosElectricos():

    def __init__(self):
        self.autonomia = 100

    def cargarEnergia(self):
        self.cargando = True
    


miMoto = Moto("Honda","CBR")
miMoto.hace_caballito()
miMoto.estado()


furgoneta = Furgoneta("Renault","Kangoo")
furgoneta.arrancar()
furgoneta.estado()
print(furgoneta.carga(True))

class BicicletaElectrica(VehiculosElectricos,Vehiculos):#Python permite la herencia multiiple lo que significa que puede heredar de una o mas clases y le da preferencia la primera clase que se indique en la zona de parametros en cuanto al constructor de la clase.
    pass

miBici = BicicletaElectrica()




        

