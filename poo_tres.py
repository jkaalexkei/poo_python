
#Se debe encapsular una variable o metodo cuando una clase asi lo necesite o dependiendo de las necesidades 

class Coche():#declaracion de la clase, se nombre con la primera letra en mayusculas
    #propiedades

    #declaracion de constructor
    def __init__(self):#constructor y siempre se declara de esta manera
        self.__largochasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4 #Para encapsular una variable y que no sea accesible desde fuera de la clase se le antepone dos guiones bajos antes del elemento a encapsular. Asi mismo se debe usar en el resto del codigo con los elementos encapsulados
        self.__enmarcha = False #para comprobar el estado del coche
    #el parametro self siempre debe estar como argumento por defecto
    def arrancar (self,arrancamos):

        self.__enmarcha = arrancamos#almacenamos en la variable enmarcha lo que reciba el argumento arrancamos puede ser true o false

        if (self.__enmarcha):#si la var en marcha es verdadera

            chequeo = self.__chequeo_interno()#a la variable chequeo le asignamos lo que devuelve el metodo chequeo_interno (true o false)
        

        if (self.__enmarcha and chequeo):#evaluamos si la variable enmarcha y chequeo son verdaderos
           return "El carro esta en marcha" #en ese caso retornamos un mensaje afirmativo
        elif (self.__enmarcha and chequeo == False):#en caso que no se cumpla alguna de las dos condiciones
            return "algo anda mal en el chequeo"     #retornamos un mensaje informando al usuario del problema      
        else:#en caso que no se cumplan las dos condiciones anteriores
            return "El carro esta detenido"#informamos que el objeto carro no se movido
               
    
    def estado(self):#metodo para informar el estado del coche
        print("El largo del carro es: ", self.__largochasis, " el ancho es de: ", self.__anchoChasis, " y tiene ", self.__ruedas, " ruedas")

    def __chequeo_interno(self):#metodo que evalua el chequeo interno del coche
        print("Realizando Chequeo Interno")
        self.gasolina = "no"
        self.aceite = "ok"
        self.puertas = "cerradas"

        if self.gasolina == "ok" and self.aceite == "ok"  and self.puertas=="cerradas":#evaluamos si las variables cumplen con las condiciones respectivas
            return True #en caso de cumplirlas retornamos verdadero para indicar que todo anda bien
        else:#en caso contrario
            return False#retornamos false lo que significa que algo fallo en el chequeo interno


#crear un instancia u objeto de tipo coche

miCoche = Coche()#Instanciamos la clases

# print("El largo es: ", miCoche.largochasis)
# print("El coche tiene ", miCoche.ruedas, " Ruedas")
print(miCoche.arrancar(True))
miCoche.estado()


print("---------- a continuacion creamos el segundo objeto------------")

miCoche2 = Coche()
# print("El largo es: ", miCoche2.largochasis)
# print("El coche tiene ", miCoche2.ruedas, " Ruedas")
print(miCoche.arrancar(False))
miCoche2.estado()
 
#constructor es un metodo que le da estado inicial los objetos, especifica el estado inicial de los objetos pertenecientes a un objeto


 
