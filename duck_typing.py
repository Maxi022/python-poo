"""
Duck Typing
Explicación Rápida:
Duck Typing es un principio en el que el tipo de un objeto se determina por sus métodos y propiedades, en lugar de por su herencia o clase explícita. En otras palabras, si algo se comporta como un pato (duck), se considera un pato.
"""

class Pato:
    def quack(self):
        print("Quack")

class Persona:
    def quack(self):
        print("Quack, como un pato")

def haz_quack(duck):
    duck.quack()

pato = Pato()
persona = Persona()

haz_quack(pato)    # Imprime: Quack
haz_quack(persona) # Imprime: Quack, como un pato

"""
Punto Clave:
No importa la clase del objeto, si tiene un método quack, puede ser pasado a haz_quack
"""