"""
El Method Resolution Order (MRO, por sus siglas en inglés) es el orden en el que Python busca un método o un atributo en una jerarquía de clases cuando se llama. Esto es especialmente relevante en el contexto de la herencia múltiple, donde una clase puede heredar de múltiples clases base.

¿Por qué es Importante el MRO?
El MRO determina la manera en que se resuelven los métodos y atributos en una jerarquía de clases, lo cual es fundamental para evitar ambigüedades y para garantizar que el método correcto sea llamado. En Python, el MRO se basa en el algoritmo C3 linearization (también conocido como C3 superclass linearization).

Cómo Funciona el MRO
Orden de Resolución: Cuando se llama a un método de un objeto, Python primero busca el método en la clase del objeto. Si no lo encuentra, busca en la clase base, luego en la clase base de la clase base, y así sucesivamente, siguiendo el MRO.
Algoritmo C3: En Python 2.3 y versiones posteriores, el algoritmo C3 linearization es usado para calcular el MRO. Este algoritmo asegura que el orden de las clases base sea consistente y respete las relaciones de herencia.
"""

class A:
    def hello(self):
        print("Hello, I am A")

class B(A):
    def hello(self):
        print("Hello, I am B")

class C(A):
    def hello(self):
        print("Hello, I am C")

class D(B, C):
    pass

class E(C, B):
    pass

d = D()
d.hello()  # ¿Qué imprimirá esto? Hello, I am B
print(D.__mro__)
# O bien
print(D.mro())

e = E()
e.hello() # ¿Qué imprimirá esto? Hello, I am C
print(E.__mro__)
# O bien
print(E.mro())
