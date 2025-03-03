from personas.persona import Persona

#Clase dec¿rivada de Director
class Director(Persona):
    def __init__(self, nombre, edad, telefono, genero, ocupacion , turno, e_civil):
        super().__init__(nombre, edad, telefono, genero)
        self.ocupacion = ocupacion
        self.turno = turno
        self.e_civl = e_civil
    
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"su ocupacion es de : {self.ocupacion}")
        print(f" trabaja en turno de : {self.turno}")
        print(f"Su estado civil es: {self.e_civl}")

    def administrar(self):
        print(f"El {self.ocupacion} ahora administrando el colegio")
    
    def toma_desiciones(self):
        print(f"Esta tomando una deciones importante ")

    def decomisos(self):
        print("Decomiso 3 celulares ")