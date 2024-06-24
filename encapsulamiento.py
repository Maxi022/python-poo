"""
Definición de Encapsulamiento
En Python, el encapsulamiento se realiza principalmente mediante el uso de guiones bajos (_) y dobles guiones bajos (__) al comienzo del nombre de los atributos y métodos:

Atributos/Métodos Públicos: Se puede acceder desde cualquier lugar. No tienen guiones bajos al comienzo.
Atributos/Métodos Protegidos: Se recomienda acceder a ellos solo desde la clase misma o sus subclases. Se denotan con un guion bajo (_) al comienzo.
Atributos/Métodos Privados: Se recomienda acceder a ellos solo desde la clase misma. Se denotan con dos guiones bajos (__) al comienzo.
"""

class Persona:
    def __init__(self, nombre: str, edad: int) -> None:
        self.nombre = nombre          # Atributo público
        self._edad = edad             # Atributo protegido
        self.__saldo = 0              # Atributo privado

    # API Publica
    def obtener_edad(self) -> int:
        """Método público para obtener la edad."""
        return self._edad

    def incrementar_edad(self) -> None:
        """Método público para incrementar la edad."""
        self._edad += 1

    def mostrar_saldo(self) -> None:
        """Método público para mostrar el saldo privado."""
        print(f"Saldo: {self.__saldo}")

    def incrementar_saldo(self, cantidad: int) -> None:
        """Método público para incrementar el saldo privado."""
        if cantidad > 0:
            self.__saldo += cantidad

    # API Privada
    def _metodo_protegido(self) -> None:
        """Método protegido."""
        print("Este es un método protegido")

    def __metodo_privado(self) -> None:
        """Método privado."""
        print("Este es un método privado")



# Ejemplo de uso
persona = Persona("Maximiliano", 32)

# Acceso a atributos y métodos públicos
print(persona.nombre)
persona.incrementar_edad()
print(persona.obtener_edad())

# Acceso a atributos y métodos protegidos (no recomendado pero posible)
print(persona._edad)
persona._metodo_protegido()

# Intento de acceso a atributos y métodos privados (no posible directamente)
# print(persona.__saldo)             # Error
# persona.__metodo_privado()         # Error

# Acceso a atributos y métodos privados a través de métodos públicos
persona.mostrar_saldo()
persona.incrementar_saldo(100)
persona.mostrar_saldo()