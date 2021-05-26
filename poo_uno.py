
class Coche():#declaracion de la clase
    #propiedades
    largochasis = 250
    anchoChasis = 120
    ruedas = 4
    enmarcha  = False

    #metodos
    #self hace referencia al propio objeto perteneciente a la clase (this)
    #self hace referencia a la instancia perteneciente a la clase.
    #self es obligatorio colocarlo
    

    def arrancar (self):
        self.enmarcha = True
        
    
    def estado(self):
        if(self.enmarcha):
            return "el coche esta en marcha"
        else:
            return "el coche esta parado"


#crear un instancia u objeto de tipo coche

miCoche = Coche()#Instanciamos la clases

print("El largo es: ", miCoche.largochasis)
print("El coche tiene ", miCoche.ruedas, " Ruedas")
print(miCoche.estado())
miCoche.arrancar()
miCoche.ruedas = 5

print(miCoche.ruedas)



 
