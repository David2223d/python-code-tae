class Tigre:
    def __init__(self, raza, edad ,peso):
        self.raza = raza
        self.edad = edad
        self.peso = peso

    def mostrar_info(self):
        print(f"raza: {self.raza}")
        print(f"edad: {self.edad}")
        print(f"peso: {self.peso}")

    def levanto(self):
        print(f"El Tigre {self.raza} de: {self.edad} años, con peso de :{self.peso}  se ha levantado.")

    def detecto_presa(self):
        print(f"El Tigre {self.raza} con {self.peso}  vio a su presa.")

    def ataco(self):
        print(f"El Tigre {self.raza} con {self.peso} kilos ,de:{self.edad} años ,ataco a una presa")

tigre1 = Tigre("Siberiano", "19", "200")
tigre2 = Tigre("Mutante", "999", "300")

# Usar los métodos de los objetos
tigre1.levanto()
tigre1.detecto_presa()
tigre1.ataco()

print()  # Separador entre autos

tigre2.levanto()
tigre2.detecto_presa()
tigre2.ataco()