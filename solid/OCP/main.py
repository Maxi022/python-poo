"""
    El Principio de Abierto/Cerrado (Open/Closed Principle u OCP) establece que las entidades de software (clases, módulos, funciones, etc.) deben estar abiertas para la extensión, pero cerradas para la modificación. Esto significa que debemos poder extender el comportamiento de una clase sin modificar su código fuente original.

    A continuación, te mostraré un ejemplo de cómo implementar OCP en Python en el contexto de un sistema de cálculo de salario para diferentes tipos de empleados.

    Ejemplo: Sistema de Cálculo de Salario
    Supongamos que tenemos que implementar un sistema que calcula el salario de diferentes tipos de empleados: empleados regulares y empleados contratistas. Queremos poder añadir más tipos de empleados en el futuro sin modificar las clases existentes.

    Explicación
    Clase Employee:

    Es una clase base abstracta que define un método abstracto calculate_salary. Esto asegura que cualquier clase derivada debe implementar este método.
    Clase RegularEmployee:

    Extiende Employee e implementa el método calculate_salary para calcular el salario mensual de un empleado regular.
    Clase ContractorEmployee:

    Extiende Employee e implementa el método calculate_salary para calcular el salario de un contratista basado en su tarifa por hora y horas trabajadas.
    Archivo main.py:

    Crea instancias de RegularEmployee y ContractorEmployee.
    Calcula y muestra los salarios de los empleados.
"""

# main.py (update)
from typing import List
from employee import Employee
from regular_employee import RegularEmployee
from contractor_employee import ContractorEmployee
from part_time_employee import PartTimeEmployee
from freelancer_employee import FreelancerEmployee

# main.py
class Main:
    def __init__(self):
        self.employees = self._load_employees()

    def _load_employees(self) -> List[Employee]:
        # Recoge todos los métodos que empiezan con '_employee_' y los ejecuta para crear empleados
        employee_methods = [method for method in dir(self) if method.startswith('_employee_')]
        employees = []
        for method in employee_methods:
            employees.extend(getattr(self, method)())
        return employees

    def _employee_regular(self) -> List[Employee]:
        return [RegularEmployee(name="Alice", monthly_salary=3000)]

    def _employee_contractor(self) -> List[Employee]:
        return [ContractorEmployee(name="Bob", hourly_rate=50, hours_worked=120)]

    def _employee_part_time(self) -> List[Employee]:
        return [PartTimeEmployee(name="Charlie", hourly_rate=30, hours_worked=80)]
    
    def _employee_freelancer(self) -> List[Employee]:
        return [FreelancerEmployee(name="David", project_fee=5000)]

    def run(self):
        for employee in self.employees:
            print(f"Employee: {employee.name}, Salary: {employee.calculate_salary()}")

if __name__ == "__main__":
    main = Main()
    main.run()


"""
    Comparación y Opinión
    Lista de Empleados Directa:

    Modificación Directa: En la primera opción, agregar un nuevo tipo de empleado requeriría modificar una lista directamente en la clase principal, lo que violaría el principio de abierto/cerrado ya que la clase principal tendría que ser modificada cada vez que se añade un nuevo tipo de empleado.
    Desventajas: Este enfoque es menos modular y no escala bien. Cada vez que se añaden nuevos tipos de empleados, el código existente debe ser modificado, lo que puede introducir errores y dificultades de mantenimiento.
    Métodos Privados para Cargar Empleados:

    Carga Dinámica: Tu sugerencia permite agregar nuevas características (nuevos tipos de empleados) sin modificar el código existente de la clase principal. En lugar de modificar una lista, simplemente se añade un nuevo método que sigue una convención de nombres específica.
    Ventajas: Esto facilita la extensibilidad del código. La clase principal no necesita saber sobre los nuevos tipos de empleados que se están añadiendo. Solo necesita ejecutar todos los métodos que sigan la convención de nombres, lo cual es mucho más limpio y modular.
    OCP Adherencia: Este enfoque adhiere perfectamente al principio de abierto/cerrado, ya que el código existente no se modifica cuando se añade un nuevo tipo de empleado. Solo se extiende mediante nuevos métodos, manteniendo el código existente intacto.
"""