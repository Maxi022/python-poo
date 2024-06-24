"""
    El Principio de Responsabilidad Única (Single Responsibility Principle o SRP) establece que una clase debería tener una única razón para cambiar, es decir, debería tener una sola responsabilidad o propósito. En Python, podemos implementar SRP dividiendo las responsabilidades en clases separadas.

    A continuación, te mostraré un ejemplo de cómo implementar SRP en un contexto de gestión de empleados.

    Ejemplo: Gestión de Empleados
    Supongamos que tenemos que implementar un sistema que gestiona la información de empleados, guarda esa información en una base de datos y envía notificaciones.

    Paso 1: Definir las Clases Separadas por Responsabilidad
    Clase Employee: Responsable de manejar los datos del empleado.

    Clase Employee:

    Maneja la información de los empleados.
    Tiene un método para mostrar la información del empleado.
"""

# employee.py
from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    age: int
    position: str

    def display_info(self) -> str:
        return f"Name: {self.name}, Age: {self.age}, Position: {self.position}"

