#Clase Base
class Pokemon:
    def __init__(self,num_pokedex,nombrePokemon,pesoPokemon,sexo,temporadaQueAparece,tipo):
        self.num_pokedex=num_pokedex
        self.nombrePokemon=nombrePokemon
        self.pesoPokemon=pesoPokemon
        self.sexo=sexo
        self.temporadaQueAparece=temporadaQueAparece
        self.tipo=tipo

    def mostrar_informacion(self):
        print(f"Numero pokedex:{self.num_pokedex}")
        print(f"Nombre del Pokemon es:{self.nombrePokemon}")
        print(f"Peso:{self.pesoPokemon}")
        print(f"Sexo:{self.sexo}")
        print(f"Temporada:{self.temporadaQueAparece}")
        print(f"Tipo:{self.tipo}")
    
    def atacarPlacaje(self):
        print(f"Soy {self.nombrePokemon} y estoy atacando con Placaje")
    
    def atacarArañazo(self):
        print(f"Soy {self.nombrePokemon} y estoy atacando con Arañazo")
    
    def atacarMordizco(self):
        print(f"Soy {self.nombrePokemon} y estoy atacando con Mordizco")

    