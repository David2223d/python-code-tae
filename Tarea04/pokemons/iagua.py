from pokemons.pokemon import Pokemon

#Clase devada de IAgua
class IAgua(Pokemon):
    def __init__(self, num_pokedex, nombrePokemon, pesoPokemon, sexo, temporadaQueAparece, tipo,profundidad_max,velocidad_de_nado,capacidad_de_purificacion):
        super().__init__(num_pokedex, nombrePokemon, pesoPokemon, sexo, temporadaQueAparece, tipo)
        self.profundidad_max=profundidad_max
        self.velocidad_de_nado=velocidad_de_nado
        self.capacidad_de_purificacion=capacidad_de_purificacion
    
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Profundidad de nadamiento maximo es:{self.profundidad_max}")
        print(f"Velocidad de nadamiento es:{self.velocidad_de_nado} m/s")
        print(f"Capacidad de purificacion es:{self.capacidad_de_purificacion}")

    def atacarHidrobomba(self):
        print(f"Soy {self.nombrePokemon} y estoy atacando con Hidrobomba \U0001F4A7")
    
    def atacarPistolaAgua(self):
        print(f"Soy {self.nombrePokemon} y estoy atacando con Pistola Agua \U0001F4A7")
    
    def atacarHidroPulso(self):
        print(f"Soy {self.nombrePokemon} y estoy atacando con Hidro Pulso \U0001F4A7")

    