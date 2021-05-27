#Ejercicio sencillo funcionamiento de una moto
#propiedades de la moto: ruedas, asientos, marca, tipo
#comportamientos: arrancar, frenar, acelerar, estado

class Moto():#creamos la clase Moto

    def __init__(self):#inicializamos el constructor con los valores iniciales de las propiedades
        self.__ruedas = 2
        self.__pasajeros=2
        self.__marca = ["suzuki","empire","yamaha","ktm"]
        self.__tipo = ["paseo","alto cilindraje","en duro"]
        self.__encendido = ""
    
    def arrancar(self):#definimos el metodo arrancar

        estado = self.estado()#asignamos lo que devuelve el metodo estado a la variable estado 

        if (estado == True):#si el metodo estado devuelve verdadero
            self.__encendido = True#iniciamos la variable encendido en verdadero indicando que la moto ha encendido
        else:#en caso contrario
            self.__encendido = False#asignamos falso a la variable encendido debido a que fallo algo en la veriificacion del estado de la moto
            
        if (self.__encendido == True):#en caso de ser verdadera la variable encendido se informa que la moto ha encedido
            print("La moto se ha encendido")
            self.acelerar()#se llama al metodo acelerar para que indicar la moto ya esta en movimiento
        else:#en caso contrario que no este encedida el objeto moto se informa que algo anda mal
            print("Algo anda Mal en el estado de la moto Verifica,\n Aceite,gasolina,luces o frenos")


    def infoMoto(self,marca,tipo): #definimos este metodo para informacion de las caracteristicas de la moto
        for elemento in self.__marca:#recorremos los elementos de la propiedad marca
            if elemento == marca:#si consigue un elemento similar
                self.__marca = marca#a la variable se le asigna lo que reciba el parametro marca
            else:#en caso contrario
                self.__marca = "Marca no establecida"#es una marca no establecida
        
        for elemento2 in self.__tipo:#se aplica el mismo procedimiento del bucle anterior
            if elemento2 == tipo:
                self.__tipo = tipo
            else:
                self.__tipo = "Tipo no establecida"

        return print("La moto es tipo: ", self.__tipo, " Marca: ",self.__marca)#devolvemos la descripcion del objeto moto
        
    def frenar(self): #definimos el metodo frenar para indicar que el objeto moto se ha frenado
        print("\n La moto se ha frenado por exceso de velocidad")

    def acelerar(self):##definimos el metodo acelerar para indicar que el objeto moto esta acelerando
        print("La moto esta acelerando")#se informa que el objeto moto esta acelerando
        self.velocidadmax = 70#definimos una variable para almacenar la velocidad  maxima
        for i in range(self.velocidadmax):#defnimos este bucle para simular el avance del acelerador
            print(i,end=" ")
        
        if (self.velocidadmax > 60):#si la velocidad maxima supera los 60 km/h
            self.frenar()#hacemos la llamada al metodo frenar para indicar que el objeto moto supero el limite de velocidad y que debe frenar
            print("Haz sobrepasado la velocidad maxima")
        else:
            print("Puedes andar con tranquilidad en tu moto")


    def estado(self): #definimos el metodo estado para verificar el funcionamiento de la moto
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

