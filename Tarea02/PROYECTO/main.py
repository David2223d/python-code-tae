# main.py
from vehiculos.motocicleta import Motocicleta
from vehiculos.automovil import Automovil
from vehiculos.autobus import Autobus
from vehiculos.vehiculo import Vehiculo

# Creando objetos de cada clase derivada
vehiculo = Vehiculo("General Motors", "Modelo X")
automovil = Automovil("Toyota", "Corolla", "Gasolina")
motocicleta = Motocicleta("Yamaha", "YZF-R3", 321)
autobus = Autobus("Mercedes-Benz", "Sprinter", 40)


# Mostrando información y usando métodos
vehiculo.mostrar_informacion()
vehiculo.encender()

automovil.mostrar_informacion()
automovil.conducir()

motocicleta.mostrar_informacion()
motocicleta.conducir()

autobus.mostrar_informacion()
autobus.conducir()