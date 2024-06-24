from typing import Union

class CellPhone:
    def __init__(self, brand: str, price: Union[int, float], camera: str):
        self.brand = brand
        self.price = price
        self.camera = camera

    @classmethod
    def create(cls, brand: str, price: Union[int, float], camera: str) -> 'CellPhone':
        return cls(brand, price, camera)

    def __str__(self) -> str:
        return f"CellPhone(brand={self.brand}, price={self.price}, camera={self.camera})"
    
    def display_info(self) -> None:
        print(f"Brand: {self.brand}")
        print(f"Price: {self.price}")
        print(f"Camera: {self.camera}")

# Ejemplo de uso
telefono = CellPhone.create(brand="Samsung", price=999.99, camera="12MP")
print(telefono)
telefono.display_info()

"""
Explicación:
Constructor privado:

Aunque Python no soporta constructores privados de manera nativa, podemos simular este comportamiento mediante convención. El constructor __init__ se mantiene protegido al no ser llamado directamente desde fuera de la clase.
Método de clase create:

Se define un método de clase create usando el decorador @classmethod. Este método toma los mismos parámetros que el constructor __init__.
El método create llama internamente al constructor __init__ (a través de cls(...)) para crear una nueva instancia de CellPhone.
Uso del método create:

En lugar de llamar directamente a CellPhone(...), se utiliza CellPhone.create(...) para crear una instancia de CellPhone.
Tipado:

Se utiliza -> 'CellPhone' en la firma del método create para indicar que el método devuelve una instancia de CellPhone.
Ejemplo de uso:
El ejemplo muestra cómo crear una instancia de CellPhone utilizando el método create, en lugar de llamar al constructor directamente. Esto proporciona una capa adicional de abstracción y control sobre la creación de instancias.
"""