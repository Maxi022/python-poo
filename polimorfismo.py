class Animal:
    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau"

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau"

def imprimir_sonido(animal):
    print(animal.hacer_sonido())

# Crear instancias de Perro y Gato
perro = Perro()
gato = Gato()

# Llamar a la función imprimir_sonido con diferentes objetos
imprimir_sonido(perro)  # Imprime: Guau
imprimir_sonido(gato)   # Imprime: Miau