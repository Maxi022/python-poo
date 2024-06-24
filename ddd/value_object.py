"""
    Implementación de Value Objects
    Primero, definimos las clases Nombre y Edad como Value Objects.

    Explicación
        Value Objects (Nombre y Edad):

        Usamos la clase dataclass con frozen=True para hacerlos inmutables.
        Realizamos validaciones en __post_init__ para asegurarnos de que los valores son válidos.
"""

from dataclasses import dataclass

@dataclass(frozen=True)
class Nombre:
    valor: str

    def __post_init__(self):
        if not self.valor or len(self.valor) > 100:
            raise ValueError("El nombre debe ser una cadena no vacía y de menos de 100 caracteres.")
        if not self.valor.replace(" ", "").isalpha():
            raise ValueError("El nombre solo debe contener caracteres alfabéticos y espacios.")

@dataclass(frozen=True)
class Edad:
    valor: int

    def __post_init__(self):
        if not (0 <= self.valor <= 150):
            raise ValueError("La edad debe ser un valor entre 0 y 150.")