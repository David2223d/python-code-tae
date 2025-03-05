from pokemons.pokemon  import Pokemon
from pokemons.ielectrico import IElectrico
from pokemons.iagua import IAgua
from pokemons.ifuego import IFuego
from pokemons.iplanta import IPlanta

pokemon = Pokemon(373,"Salamence",102.6,"Macho","tercera generacion","gragon volador")
pikachu = IElectrico(25,"Pikachu",6,"Macho","Primera temporada","Electrico","100.000 v","40/100","60/100")
squirtle = IAgua("007","Squirtle",9,"Hembra","Primera Temporada","Agua","Infinita","70/100","no tiene capacidad de purificacion")
charmander = IFuego("004","Charmander",8.5,"Macho","Primera Temporada","Fuego","90/100","85/100","85/100")
bulbasaur = IPlanta(1,"bulbasaur",6.9,"Macho","Primera Temporada","Agua","80/100","70/100","50/100")

pokemon.mostrar_informacion()
pokemon.atacarMordizco()
print("-----------------------------")
pikachu.mostrar_informacion()
pikachu.atacarImpacTrueno()
print("--------------------------------")
squirtle.mostrar_informacion()
squirtle.atacarPistolaAgua()
print("-------------------------------")
charmander.mostrar_informacion()
charmander.atacarAscuas()
print("---------------------------------")
bulbasaur.mostrar_informacion()
bulbasaur.atacarLatigoCepa()