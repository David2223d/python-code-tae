from personas.persona import Persona

#Clase derivada de profesor
class Profesor(Persona):
    def __init__(self, nombre, edad, telefono, genero,materia,ocupacion):
        super().__init__(nombre, edad, telefono, genero)
        self.materia = materia
        self.ocupacion = ocupacion

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"La materia que da es: {self.materia}")
        print(f"La ocupacion que tiene es: {self.ocupacion}")

    def enseñar(self):
        print(f"El profesor {self.nombre} enseñado a sus alumnos")

    def educar(self):
        print(f"Esta educando a un alumno que se paso la raya llamando a sus papas")
