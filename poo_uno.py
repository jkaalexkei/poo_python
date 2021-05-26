
class Coche():#declaracion de la clase, se nombre con la primera letra en mayusculas
    #propiedades
    largochasis = 250
    anchoChasis = 120
    ruedas = 4
    enmarcha = False #para comprobar el estado del coche

    #metodos
    #self hace referencia al propio objeto o insstancia  de la clase (this)
    #self hace referencia a la instancia perteneciente a la clase.
    #self es obligatorio colocarlo
    

    def arrancar (self):
        self.enmarcha = True #cambia el estado a verdadero
               
    
    def estado(self):
        if(self.enmarcha):
            return "el coche esta en marcha"
        else:
            return "el coche esta parado"


#crear un instancia u objeto de tipo coche

miCoche = Coche()#Instanciamos la clases

print("El largo es: ", miCoche.largochasis)
print("El coche tiene ", miCoche.ruedas, " Ruedas")
miCoche.arrancar()
print(miCoche.estado())


#sintaxis
#nombreobjeto.propiedad
#nombreobjeto.metodo




#nstancia: ejemplar perteneciiente a la clase
 
