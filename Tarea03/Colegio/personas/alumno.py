from personas.persona import Persona

#Clase derivada de Alumno
class Alumno(Persona):
    def __init__(self, nombre, edad, telefono, genero, grado,n_matricula,iq):
        super().__init__(nombre, edad, telefono, genero)
        self.grado = grado
        self.n_matricula = n_matricula
        self.iq = iq
    
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"grado: {self.grado}")
        print(f"Numero de Maquicula: {self.n_matricula}")
        print(f"IQ : {self.iq}")

    def estudiar(self):
        print(f"Esta estudiando mucho el {self.nombre} que esta en {self.grado}") 
    
    def hacer_tarea(self):
        print(f"Empezo a realizar su tarea")

    def aprobar(self):
        print(f"Su mision de {self.nombre} es aprobar")