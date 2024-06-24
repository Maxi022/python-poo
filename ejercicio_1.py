
class Student:
    def __init__(self, name: str, age: int, degree: int) -> None:
        self.name = name
        self.age = age
        self.degree = degree

    @classmethod
    def create(cls, name: str, age: int, degree: int) -> 'Student':
        return cls(name, age, degree)

    def display_info(self) -> None:
        print(f"name={self.name}")
        print(f"age={self.age}")
        print(f"degree={self.degree}")

    def presentation(self) -> None:
        print(f"Hola soy {self.name}, tengo {self.age} años y voy en {self.degree} año.")

    def start_studying(self) -> None:
        print(f"Comence a estudiar en el {self.degree} año.")

    def stop_studying(self) -> None:
        print(f"Finalice mi {self.degree} año de estudio.")

# Ejemplo de uso
student = Student.create(name="Maximiliano", age=32, degree=4)
student.display_info()
student.presentation()
student.start_studying()
student.stop_studying()