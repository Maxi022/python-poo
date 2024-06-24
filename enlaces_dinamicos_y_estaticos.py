"""
Enlaces Dinámicos y Estáticos
Enlaces Dinámicos:
Enlace dinámico, o dynamic binding, se refiere a la resolución de métodos en tiempo de ejecución. En Python, los métodos se enlazan dinámicamente, lo que significa que el método específico que se llamará se determina durante la ejecución del programa.
"""

class Animal:
    def sonido(self):
        raise NotImplementedError

class Perro(Animal):
    def sonido(self):
        return "Guau"

class Gato(Animal):
    def sonido(self):
        return "Miau"

def hacer_sonido(animal):
    print(animal.sonido())

perro = Perro()
gato = Gato()

hacer_sonido(perro)  # Imprime: Guau
hacer_sonido(gato)   # Imprime: Miau

"""
Enlaces Estáticos:
Enlace estático, o static binding, se refiere a la resolución de métodos en tiempo de compilación. Python no utiliza enlace estático, pero lenguajes como C++ sí lo hacen.

Punto Clave:
Python resuelve los métodos en tiempo de ejecución (enlace dinámico), lo que le da flexibilidad pero puede impactar en el rendimiento.
"""