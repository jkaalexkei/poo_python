

#Aplicacion de la funcion super()

class Persona():
    def __init__(self,nombre,edad,lugar_residencia):
        self.nombre = nombre
        self.edad = edad
        self.residencia = lugar_residencia
    
    def descripcion(self):
        print("Nombre: ",self.nombre," Edad: ", self.edad," Lugar de residencia: ",self.residencia)
    
    def hola(self):
        print("Hola Mundo")

class Empleado(Persona):

    def __init__(self,salario,antiguedad,nombre_empleado,edad_empleado,residencia_empleado):

        super().__init__(nombre_empleado,edad_empleado,residencia_empleado)#Hace la llamada al constructor de la clase padre que esta heredando
        self.salario = salario
        self.antiguedad_persona=antiguedad

        super().hola()
    
    def descripcion(self):
        super().descripcion()
        print("Salario: "  ,self.salario, "Antiguedad: ",self.antiguedad_persona)


Antonio = Persona("Alex",23,"Merida")
Antonio.descripcion()

print(isinstance(Antonio,Empleado))


#Principio de sustitucion
#consiste en plantearse las siguientes preguntas:

#es siempre un o una

#funcion isinstance()--> nos informa si un objeto es instancia de una clase determinada devuelve verdadero o falso



