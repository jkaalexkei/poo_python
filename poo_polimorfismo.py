
#polimorfismo -> un objeto puede cambiar de formas y comportamientos dependiendo del contexto en el que se utilice

class Coche():

    def desplazamiento(self):
        print("Me desplazo utiilizando 4 ruedas")

class Moto():


    def desplazamiento(self):
        print("Me desplazo utilizando 2 ruedas")


class Camion():

    def desplazamiento(self):
        print("Me desplazo utilizando 6 ruedas")


# miVehiculo = Coche()
# miVehiculo.desplazamiento()

# miMoto = Moto()
# miMoto.desplazamiento()

# miCamion= Camion()
# miCamion.desplazamiento()

def desplazamientoVehiculo(vehiculo):#funcion que recibe como parametro un objeto para verificar que metodos debe usar y que comportamiento de tener

    vehiculo.desplazamiento()

miCamion = Camion()
desplazamientoVehiculo(miCamion)

