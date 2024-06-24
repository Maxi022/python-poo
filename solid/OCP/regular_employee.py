# regular_employee.py
from employee import Employee

class RegularEmployee(Employee):
    def __init__(self, name: str, monthly_salary: float):
        super().__init__(name)
        self.monthly_salary = monthly_salary

    def calculate_salary(self) -> float:
        return self.monthly_salary