"""
    Implementación de la Clase Persona
    Luego, usamos estos Value Objects en la clase Persona.
"""

from dataclasses import dataclass
from value_object import Nombre, Edad

@dataclass
class Persona:
    nombre: Nombre
    edad: Edad

    def __post_init__(self):
        # Se pueden agregar validaciones adicionales aquí si es necesario
        pass

    def cambiar_nombre(self, nuevo_nombre: Nombre):
        return Persona(nombre=nuevo_nombre, edad=self.edad)

    def cambiar_edad(self, nueva_edad: Edad):
        return Persona(nombre=self.nombre, edad=nueva_edad)

    def mostrar_info(self) -> str:
        return f"Nombre: {self.nombre.valor}, Edad: {self.edad.valor}"
    
"""
    Clase Persona:

    Usamos dataclass para simplificar la definición de la clase.
    Métodos como cambiar_nombre y cambiar_edad devuelven una nueva instancia de Persona con los valores actualizados, manteniendo la inmutabilidad.
    El método mostrar_info se utiliza para presentar la información de la persona.
    En esta implementación, los Value Objects garantizan que Nombre y Edad se definan correctamente y la clase Persona se asegura de que las instancias sean inmutables, lo que es una práctica común en DDD para evitar efectos secundarios inesperados.
"""