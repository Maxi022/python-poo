"""
    El Principio de Responsabilidad Única (Single Responsibility Principle o SRP) establece que una clase debería tener una única razón para cambiar, es decir, debería tener una sola responsabilidad o propósito. En Python, podemos implementar SRP dividiendo las responsabilidades en clases separadas.

    A continuación, te mostraré un ejemplo de cómo implementar SRP en un contexto de gestión de empleados.

    Ejemplo: Gestión de Empleados
    Supongamos que tenemos que implementar un sistema que gestiona la información de empleados, guarda esa información en una base de datos y envía notificaciones.

    Paso 1: Definir las Clases Separadas por Responsabilidad
    Clase Employee: Responsable de manejar los datos del empleado.
    Clase EmployeeRepository: Responsable de manejar la persistencia de datos (almacenar y recuperar empleados).
    Clase EmployeeNotifier: Responsable de manejar las notificaciones a los empleados.
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

# employee_notifier.py
class EmployeeNotifier:
    def notify(self, employee: Employee, message: str) -> None:
        print(f"Sending notification to {employee.name}: {message}")

# main.py
# from employee import Employee
# from employee_repository import EmployeeRepository
# from employee_notifier import EmployeeNotifier

def main():
    # Crear instancias de las clases
    repository = EmployeeRepository()
    notifier = EmployeeNotifier()

    # Crear y agregar empleados
    emp1 = Employee(name="Alice", age=30, position="Developer")
    emp2 = Employee(name="Bob", age=40, position="Manager")

    repository.add_employee(emp1)
    repository.add_employee(emp2)

    # Listar empleados
    for emp in repository.list_employees():
        print(emp.display_info())

    # Notificar a un empleado
    notifier.notify(emp1, "Your performance review is scheduled for next week.")

if __name__ == "__main__":
    main()