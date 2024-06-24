from typing import Union

class CellPhone:
    def __init__(self, brand: str, price: Union[int, float], camera: str):
        self.brand = brand
        self.price = price
        self.camera = camera

    def __str__(self) -> str:
        return f"CellPhone(brand={self.brand}, price={self.price}, camera={self.camera})"
    
    def display_info(self) -> None:
        print(f"Brand: {self.brand}")
        print(f"Price: {self.price}")
        print(f"Camera: {self.camera}")


# Ejemplo de uso
cell = CellPhone(brand="Samsung", price=999.99, camera="12MP")
print(cell)
cell.display_info()