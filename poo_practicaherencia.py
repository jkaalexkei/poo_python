
class Persona():
    
    def __init__(self,cedula,nombre,apellido,edad):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    
    def InfoPersonal(self):
        print("Mis datos personales son: \nCedula: ",self.cedula,"\nNombre: ",self.nombre,"\nApellido: ",self.apellido,"\nEdad: ",self.edad)
    
    def Trabajar(self,nombre_empleo):
        self.empleo = nombre_empleo
        print("Tengo un trabajo como: ", self.empleo)
    
    def Caminar(self):
        print("Estoy caminando")

class Institucion(Persona):
    
    def __init__(self,institucion,cedula,nombre,apellido,edad):
        super().__init__(cedula,nombre,apellido,edad)
        self.nombreinstitucion = institucion

    
    def inscribirEstudiantes(self,matricula):
        self.matricula = matricula
        print("La escuela: ",self.nombreinstitucion, "\n tiene: ",self.matricula," Estudiantes")
        
    def infoPersonal(self):
        super().InfoPersonal()
        
class Docente(Institucion,Persona):
    
    def __init__(self,agnosdeservicio, cargoactual,institucion,cedula,nombre,apellido,edad):
        super().__init__(institucion,cedula,nombre,apellido,edad)
        
        self.agnosdeservicio = agnosdeservicio
        self.cargoactual = cargoactual
    
    def DarClases(self):
        print("Doy Clases en la escuela")
    
    def PrestarServicio(self):
        print("Presto servicio como docente")
    
    # def infoPersonal(self):
    #     super().infoPersonal()
        
class Estudiante(Persona):

    def __init__(self,grado,seccion,nivel):

        self.grado = grado
        self.seccion = seccion
        self.nivel = nivel

    def asistisClases(self):
        print("estudio ", self.grado, "\n seccion: ",self.seccion,"\n nivel: ",self.nivel)


maestro = Docente(3,"DOCENTE III","HOLA MUNDO",123456,"ALEX","VARELA",37)
maestro.InfoPersonal()
maestro.inscribirEstudiantes(200)
maestro.Trabajar("Profesor de Historia")


# nuevoEstudiante = Persona(16020494,"Alexander","Varela",15)
# nuevoEstudiante.InfoPersonal()
# nuevoEstudiante.Trabajar("Mecanico")










    