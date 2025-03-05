from pokemons.pokemon import Pokemon

#Clase derivada de IFuego
class IFuego(Pokemon):
    def __init__(self, num_pokedex, nombrePokemon, pesoPokemon, sexo, temporadaQueAparece, tipo,temperatura_max,taza_de_incendio,intensidad_de_llama):
        super().__init__(num_pokedex, nombrePokemon, pesoPokemon, sexo, temporadaQueAparece, tipo)
        self.temperatura_max=temperatura_max
        self.taza_de_incendio=taza_de_incendio
        self.intensidad_de_llama=intensidad_de_llama
    
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Temperatura max es: {self.temperatura_max}")
        print(f"Taza de incendio es: {self.taza_de_incendio}")
        print(f"Intensidad de llama es:{self.intensidad_de_llama}")
    
    def atacarPunioFuego(self):
        print(f"Soy {self.nombrePokemon} y estoy atacando con Punio Fuego 🔥")

    def atacarAscuas(self):
        print(f"Soy {self.nombrePokemon} y estoy atacando con Ascuas 🔥")
    
    def atacarLanzaLlamas(self):
        print(f"Soy {self.nombrePokemon} y estoy atacando con Lanza Llamas 🔥")
    
