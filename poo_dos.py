
class Coche():#declaracion de la clase, se nombre con la primera letra en mayusculas
    #propiedades

    #declaracion de constructor
    def __init__(self):#constructor y siempre se declara de esta manera
        self.largochasis = 250
        self.anchoChasis = 120
        self.ruedas = 4
        self.enmarcha = False #para comprobar el estado del coche
    #el parametro self siempre debe estar como argumento por defecto
    def arrancar (self,arrancamos):
        self.enmarcha = arrancamos

        if (self.enmarcha):
            return "El carro esta en marcha"
        else:
            return "El carro esta detenido"
               
    
    def estado(self):
        print("El largo del carro es: ", self.largochasis, " el ancho es de: ", self.anchoChasis, " y tiene ", self.ruedas, " ruedas")



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


 
