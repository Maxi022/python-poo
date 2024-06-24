"""
    En este caso, vamos a definir una clase base Bird que representará a todas las aves. Luego, crearemos dos clases derivadas: FlyingBird para las aves que pueden volar y NonFlyingBird para las aves que no pueden volar.
"""

class Bird:
    def __init__(self, species):
        self.species = species

# Definición de la clase FlyingBird
class FlyingBird(Bird):
    def __init__(self, species):
        super().__init__(species)

    def fly(self):
        return f"The {self.species} is flying"

# Definición de la clase NonFlyingBird
class NonFlyingBird(Bird):
    def __init__(self, species):
        super().__init__(species)

# Clase Penguin que hereda de NonFlyingBird
class Penguin(NonFlyingBird):
    def __init__(self):
        super().__init__("Penguin")

# Clase Hawk que hereda de FlyingBird
class Hawk(FlyingBird):
    def __init__(self):
        super().__init__("Hawk")

# Ejemplo de uso (En este caso al ser una ave no voladora el metodo fly() no estaría implimentado y daría un error.)
penguin = Penguin()

hawk = Hawk()
print(hawk.fly())  # Output: The Hawk is flying

"""
    Explicación:
    Clase Penguin: Esta clase hereda de NonFlyingBird y representa a los pingüinos, que son aves no voladoras. Por lo tanto, no proporciona una implementación para el método fly(), lo que resulta en una excepción cuando se intenta llamar a este método.

    Clase Hawk: Esta clase hereda de FlyingBird y representa a los halcones, que son aves voladoras. Proporciona una implementación concreta del método fly(), lo que permite que los halcones vuelen.

    Ejemplo de uso: Creamos instancias de Penguin y Hawk y llamamos al método fly() en ambas. Como se esperaba, la instancia de Penguin genera una excepción, ya que los pingüinos no pueden volar, mientras que la instancia de Hawk devuelve un mensaje indicando que el halcón está volando.
"""