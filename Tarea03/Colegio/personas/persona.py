#Clase Base
class Persona:
    def __init__(self,nombre,edad,telefono,genero):
        self.nombre = nombre
        self.edad = edad
        self.telefono = telefono
        self.genero = genero

    def mostrar_informacion(self):
        print(f"nombre: {self.nombre}")
        print(f"edad: {self.edad}")
        print(f"telefono: {self.telefono}")
        print(f"genero: {self.genero}")
    
    def presentacion(self):
        print(f"La {self.__class__.__name__} se esta presentando")