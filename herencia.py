
class Person: 
    def __init__(self, name: str, age: int) -> None:
        """
        Inicializa una instancia de Person.
        """
        self.name = name
        self.age = age

    @classmethod
    def create(cls, name: str, age: int) -> 'Person':
        """
        Crea una instancia de Person usando el método de clase.
        Returns:
            Person: Una instancia de la clase Person.
        """
        return cls(name, age)
    
    def display_info(self) -> None:
        """
        Muestra la información de la persona.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


class Employee(Person):
    def __init__(self, name: str, age: int, profession: str, company: str) -> None:
        """
        Inicializa una instancia de Employee.
        """
        super().__init__(name, age)
        self.profession = profession
        self.company = company

    @classmethod
    def create(cls, name: str, age: int, profession: str, company: str) -> 'Employee':
        """
        Crea una instancia de Employee usando el método de clase.
        Returns:
            Employee: Una instancia de la clase Employee.
        """
        return cls(name, age, profession, company)
    
    def display_info(self) -> None:
        """
        Muestra la información del empleado.
        """
        super().display_info()
        print(f"Profession: {self.profession}")
        print(f"Company: {self.company}")

# Ejemplo de uso
employee = Employee.create("Maximiliano", 32, "Arquitecto de Software", "Telecom")
employee.display_info()