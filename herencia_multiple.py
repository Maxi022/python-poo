
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

class Artist:
    def __init__(self, skills: str) -> None:
        """
        Inicializa una instancia de Artist.
        """
        self.skills = skills

    @classmethod
    def create(cls, skills: str) -> 'Artist':
        """
        Crea una instancia de Artist usando el método de clase.
        Returns:
            Artist: Una instancia de la clase Artist.
        """
        return cls(skills)
    
    def display_info(self) -> None:
        """
        Muestra la información del artista.
        """
        print(f"Skills: {self.skills}")

class Employee(Person, Artist):
    def __init__(self, name: str, age: int, skills: str, profession: str, company: str) -> None:
        """
        Inicializa una instancia de Employee.
        """
        Person.__init__(self, name, age)
        Artist.__init__(self, skills)
        self.profession = profession
        self.company = company

    @classmethod
    def create(cls, name: str, age: int, skills: str, profession: str, company: str) -> 'Employee':
        """
        Crea una instancia de Employee usando el método de clase.
        Returns:
            Employee: Una instancia de la clase Employee.
        """
        return cls(name, age, skills, profession, company)
    
    def display_info(self) -> None:
        """
        Muestra la información del empleado.
        """
        Person.display_info(self)
        Artist.display_info(self)
        print(f"Profession: {self.profession}")
        print(f"Company: {self.company}")



# Ejemplo de uso
employee = Employee.create(name="Maximiliano", age=32, skills="Cantante", profession="Arquitecto de Software", company="Telecom")
employee.display_info()

# Como saber si una clase utiliza herencia
instance = isinstance(employee, Employee)
inheritance = issubclass(Employee, Person)
inheritance2 = issubclass(Employee, Artist)
print(instance)
print(inheritance)
print(inheritance2)