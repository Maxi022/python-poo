from employee import Employee

class ContractorEmployee(Employee):
    def __init__(self, name: str, hourly_rate: float, hours_worked: int):
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self) -> float:
        return self.hourly_rate * self.hours_worked