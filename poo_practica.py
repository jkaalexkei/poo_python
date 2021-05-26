
class Persona():

    def __init__(self):
        self.nombre = "alex"
        self.apellido = "varela"
        self.edad = 0


    def info(self):

        print("mi nombre es: ", self.nombre , " apellido: ", self.apellido, " edad: ",self.edad)
    

    def procesamiento_info (self,miedad):

        self.edad = miedad

        if(self.edad == 37):
            self.info()
            print("edad correcta")
        else:
            print("edad no permitida")


persona = Persona()

edad = int(input("ingrese la edad: "))

persona.procesamiento_info(edad)



        