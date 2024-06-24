"""
    Ejemplo sencillo de una clase abstracta en Python usando el módulo abc (Abstract Base Classes):
"""

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self) -> None:
        pass

class Dog(Animal):
    def make_sound(self) -> None:
        print("Woof!")

class Cat(Animal):
    def make_sound(self) -> None:
        print("Meow!")

# Uso de las clases
dog = Dog()
dog.make_sound()  # Output: Woof!

cat = Cat()
cat.make_sound()  # Output: Meow!

"""
    Descripción
    Animal(ABC): Animal es una clase abstracta que hereda de ABC. ABC es una clase base proporcionada por el módulo abc que permite definir métodos abstractos.

    @abstractmethod: El decorador @abstractmethod se usa para marcar el método make_sound como abstracto. Esto significa que cualquier subclase de Animal debe implementar este método.

    Dog y Cat: Estas son clases concretas que heredan de Animal. Cada una de ellas implementa el método make_sound, proporcionando su propia versión del método abstracto.

    Uso
    dog = Dog() y cat = Cat(): Aquí, se crean instancias de las clases Dog y Cat.
    dog.make_sound() y cat.make_sound(): Se llama al método make_sound de cada instancia, que ejecuta la implementación correspondiente de la subclase (Dog o Cat).
    Las clases abstractas son útiles cuando quieres definir una interfaz común para un grupo de subclases, asegurando que todas implementen ciertos métodos.
"""