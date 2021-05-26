#Ejercicio sencillo funcionamiento de una moto
#propiedades de la moto: ruedas, asientos, marca, tipo
#comportamientos: arrancar, frenar, acelerar, estado

class Moto():

    def __init__(self):
        self.__ruedas = 2
        self.__pasajeros=2
        self.__marca = ["suzuki","empire","yamaha","ktm"]
        self.__tipo = ["paseo","alto cilindraje","en duro"]
        self.__encendido = ""
    
    def arrancar(self):

        estado = self.estado()

        if (estado == True):
            self.__encendido = True
        else:
            self.__encendido = False
            
        if (self.__encendido == True):
            print("La moto se ha encendido")
            self.acelerar()
        else:
            print("Algo anda Mal en el estado de la moto Verifica,\n Aceite,gasolina,luces o frenos")


    def infoMoto(self,marca,tipo):
        for elemento in self.__marca:
            if elemento == marca:
                self.__marca = marca
            else:
                self.__marca = "Marca no establecida"
        
        for elemento2 in self.__tipo:
            if elemento2 == tipo:
                self.__tipo = tipo
            else:
                self.__tipo = "Tipo no establecida"

        return print("La moto es tipo: ", self.__tipo, " Marca: ",self.__marca)
        
    def frenar(self):
        print("\n La moto se ha frenado por exceso de velocidad")

    def acelerar(self):
        print("La moto esta acelerando")
        self.velocidadmax = 70
        for i in range(self.velocidadmax):
            print(i,end=" ")
        
        if (self.velocidadmax > 60):
            self.frenar()
            print("Haz sobrepasado la velocidad maxima")
        else:
            print("Puedes andar con tranquilidad en tu moto")


    def estado(self):
        print("Verificando estado de funcionamiento de la moto")
        self.aceite = "ok"
        self.gasolina = "ok"
        self.luces = "ok"
        self.frenos = "ok"

        if (self.aceite=="ok" and self.gasolina=="ok" and self.luces=="ok" and self.frenos=="ok"):
            print("Todo esta en orden, puedes encender la moto")
            return True
        else:
            return False




miMoto = Moto()
marca = input("Que marca es la moto: ")
tipo = input("Que tipo es la moto: ")
miMoto.infoMoto(marca,tipo)
miMoto.arrancar()

