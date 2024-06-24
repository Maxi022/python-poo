"""
    Archivo main.py:

    Utiliza las tres clases para demostrar cómo interactúan entre sí sin violar el SRP.
"""

# main.py
from employee import Employee
from employee_repository import EmployeeRepository
from employee_notifier import EmployeeNotifier

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