from pokemons.pokemon import Pokemon

#Clase derivada de  IPlanta
class IPlanta(Pokemon):
    def __init__(self, num_pokedex, nombrePokemon, pesoPokemon, sexo, temporadaQueAparece, tipo,ritmo_de_crecimiento,capacidad_fotosintetica,resistencia_a_climas_extremos):
        super().__init__(num_pokedex, nombrePokemon, pesoPokemon, sexo, temporadaQueAparece, tipo)
        self.ritmo_de_crecimiento=ritmo_de_crecimiento
        self.capacidad_fotosintetica=capacidad_fotosintetica
        self.resistencia_a_climas_extremos=resistencia_a_climas_extremos
    
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Ritmo de Crecimiento es: {self.ritmo_de_crecimiento}")
        print(f"Capacidad Fotosintetica es: {self.capacidad_fotosintetica}")
        print(f"Resistencia a climas extremos es:{self.resistencia_a_climas_extremos}")
    
    def atacarParalizar(self):
        print(f"Soy {self.nombrePokemon} y estoy atacando con Paralizar 🌱")

    def atacarDrenaje(self):
        print(f"Soy {self.nombrePokemon} y estoy atacando con Drenaje 🌱")
    
    def atacarHojaAfilada(self):
        print(f"Soy {self.nombrePokemon} y estoy atacando con Hoja Afilada 🌱")
    
    def atacarLatigoCepa(self):
        print(f"Soy {self.nombrePokemon} y estoy atacando con Latigo Cepa 🌱")
    