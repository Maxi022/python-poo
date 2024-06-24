"""
    El Principio de Responsabilidad Única (Single Responsibility Principle o SRP) establece que una clase debería tener una única razón para cambiar, es decir, debería tener una sola responsabilidad o propósito. En Python, podemos implementar SRP dividiendo las responsabilidades en clases separadas.

    A continuación, te mostraré un ejemplo de cómo implementar SRP en un contexto de gestión de empleados.

    Ejemplo: Gestión de Empleados
    Supongamos que tenemos que implementar un sistema que gestiona la información de empleados, guarda esa información en una base de datos y envía notificaciones.

    Paso 1: Definir las Clases Separadas por Responsabilidad
    Clase EmployeeNotifier: Responsable de manejar las notificaciones a los empleados.

    Clase EmployeeNotifier:

    Maneja las notificaciones a los empleados.
"""

# employee.py
from employee import Employee

# employee_notifier.py
class EmployeeNotifier:
    def notify(self, employee: Employee, message: str) -> None:
        print(f"Sending notification to {employee.name}: {message}")

