from pokemons.pokemon import Pokemon

#Clase derivada de IElectrico
class IElectrico(Pokemon):
    def __init__(self, num_pokedex, nombrePokemon, pesoPokemon, sexo, temporadaQueAparece, tipo,voltaje,resistencia,nivel_energia):
        super().__init__(num_pokedex, nombrePokemon, pesoPokemon, sexo, temporadaQueAparece, tipo)
        self.voltaje=voltaje
        self.resistencia=resistencia
        self.nivel_energia=nivel_energia

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Su voltaje de ataque es:{self.voltaje}")
        print(f"Su resistencia es: {self.resistencia}")
        print(f"Su nivel de energia es :{self.nivel_energia}")

    def atacarImpacTrueno(self):
        print(f"Soy {self.nombrePokemon} y estoy atacando con Impac Trueno \U000026A1\U000026A1\U000026A1")

    def atacarPunioTrueno(self):
        print(f"Soy {self.nombrePokemon} y estoy atacando con Punio Trueno \U000026A1\U000026A1\U000026A1")

    def atacarRayoCarga(self):
        print(f"Soy {self.nombrePokemon} y estoy atacando con Rayo Carga \U000026A1\U000026A1\U000026A1")