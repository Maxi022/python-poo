# freelancer_employee.py
from employee import Employee

class FreelancerEmployee(Employee):
    def __init__(self, name: str, project_fee: float):
        super().__init__(name)
        self.project_fee = project_fee

    def calculate_salary(self) -> float:
        return self.project_fee