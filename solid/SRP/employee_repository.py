"""
    El Principio de Responsabilidad Única (Single Responsibility Principle o SRP) establece que una clase debería tener una única razón para cambiar, es decir, debería tener una sola responsabilidad o propósito. En Python, podemos implementar SRP dividiendo las responsabilidades en clases separadas.

    A continuación, te mostraré un ejemplo de cómo implementar SRP en un contexto de gestión de empleados.

    Ejemplo: Gestión de Empleados
    Supongamos que tenemos que implementar un sistema que gestiona la información de empleados, guarda esa información en una base de datos y envía notificaciones.

    Paso 1: Definir las Clases Separadas por Responsabilidad
    Clase EmployeeRepository: Responsable de manejar la persistencia de datos (almacenar y recuperar empleados).

    Clase EmployeeRepository:

    Maneja la persistencia de datos.
    Puede agregar, obtener y listar empleados.
"""

# employee.py
from employee import Employee

# employee_repository.py
class EmployeeRepository:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee: Employee) -> None:
        self.employees.append(employee)
        print(f"Employee {employee.name} added to the repository.")

    def get_employee(self, name: str) -> Employee:
        for employee in self.employees:
            if employee.name == name:
                return employee
        raise ValueError(f"Employee {name} not found")

    def list_employees(self) -> list:
        return self.employees


