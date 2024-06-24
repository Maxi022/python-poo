"""
En Python, los getters y setters se utilizan para controlar el acceso a los atributos de una clase, proporcionando una forma de encapsular la lógica de acceso y modificación de los mismos. Aunque no son estrictamente necesarios, ya que los atributos en Python son públicos por defecto, se utilizan para implementar lógica adicional al acceder o modificar un atributo.

La forma idiomática de definir getters y setters en Python es mediante el uso del decorador property y los decoradores @property.setter y @property.deleter.
"""
"""
Explicación
Getter: El método @property define un método que se puede usar para acceder a un atributo como si fuera una propiedad. En el ejemplo, el método nombre con el decorador @property se utiliza para acceder al atributo _nombre.
Setter: El método @property.setter define un método que se puede usar para modificar el valor de un atributo. En el ejemplo, el método nombre con el decorador @nombre.setter se utiliza para modificar el valor del atributo _nombre.
Deleter: El método @property.deleter define un método que se puede usar para eliminar un atributo. En el ejemplo, el método edad con el decorador @edad.deleter se utiliza para eliminar el atributo _edad.
Ventajas del Uso de Getters y Setters
Encapsulación: Permiten ocultar la implementación interna de los atributos y exponer solo lo necesario.
Validación: Permiten agregar lógica de validación al establecer un valor.
Control: Permiten controlar el acceso a los atributos, como hacerlos de solo lectura o solo escritura.
Flexibilidad: Permiten cambiar la implementación interna sin cambiar la interfaz pública.
"""


class Persona:
    def __init__(self, nombre: str, edad: int) -> None:
        self._nombre = nombre   # Atributo protegido
        self._edad = edad       # Atributo protegido

    """
      ***********************************************************
        Getters
      ***********************************************************
    """
    # Getter para 'nombre'
    @property
    def nombre(self) -> str:
        return self._nombre
    
    # Getter para 'edad'
    @property
    def edad(self) -> int:
        return self._edad
    
    """
      ***********************************************************
        Setters
      ***********************************************************
    """

    # Setter para 'nombre'
    @nombre.setter
    def nombre(self, nombre: str) -> None:
        if not nombre:
            raise ValueError("El nombre no puede estar vacío")
        self._nombre = nombre

    # Setter para 'edad'
    @edad.setter
    def edad(self, edad: int) -> None:
        if edad < 0:
            raise ValueError("La edad no puede ser negativa")
        self._edad = edad

    """
      ***********************************************************
        Deleters
      ***********************************************************
    """

    # Deleter para 'edad' (opcional)
    @edad.deleter
    def edad(self) -> None:
        print("Eliminando la edad")
        del self._edad


# Ejemplo de uso
persona = Persona("Maximiliano", 32)

# Usando el getter
print(persona.nombre)  # Maximiliano
print(persona.edad)    # 32

# Usando el setter
persona.nombre = "Sol"
persona.edad = 35

print(persona.nombre)  # Juan
print(persona.edad)    # 35

# Intento de asignar un valor inválido
try:
    persona.edad = -5
except ValueError as e:
    print(e)  # La edad no puede ser negativa

# Usando el deleter
del persona.edad
