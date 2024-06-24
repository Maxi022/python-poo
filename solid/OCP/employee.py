from abc import ABC, abstractmethod

# employee.py
class Employee(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def calculate_salary(self) -> float:
        pass