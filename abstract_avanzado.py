from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Dict, Any

T = TypeVar('T')

class AbstractMapper(ABC, Generic[T]):
    @abstractmethod
    def to_dict(self, obj: T) -> Dict[str, Any]:
        """
        Convierte un objeto a un diccionario.

        Args:
            obj (T): El objeto a convertir.

        Returns:
            Dict[str, Any]: El diccionario resultante.
        """
        pass

    @abstractmethod
    def from_dict(self, data: Dict[str, Any]) -> T:
        """
        Convierte un diccionario a un objeto.

        Args:
            data (Dict[str, Any]): El diccionario a convertir.

        Returns:
            T: El objeto resultante.
        """
        pass

    def serialize(self, obj: T) -> str:
        """
        Serializa un objeto a una representación en cadena JSON.

        Args:
            obj (T): El objeto a serializar.

        Returns:
            str: La representación en cadena JSON del objeto.
        """
        import json
        return json.dumps(self.to_dict(obj))

    def deserialize(self, json_str: str) -> T:
        """
        Deserializa una cadena JSON a un objeto.

        Args:
            json_str (str): La cadena JSON a deserializar.

        Returns:
            T: El objeto deserializado.
        """
        import json
        data = json.loads(json_str)
        return self.from_dict(data)

# Ejemplo de una clase que queremos mapear
class User:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

# Implementación concreta de AbstractMapper para User
class UserMapper(AbstractMapper[User]):
    def to_dict(self, obj: User) -> Dict[str, Any]:
        return {
            'name': obj.name,
            'age': obj.age
        }

    def from_dict(self, data: Dict[str, Any]) -> User:
        return User(name=data['name'], age=data['age'])

# Ejemplo de uso
user = User(name="Alice", age=30)
mapper = UserMapper()

# Convertir el objeto a diccionario
user_dict = mapper.to_dict(user)
print(user_dict)  # Output: {'name': 'Alice', 'age': 30}

# Convertir el diccionario a objeto
new_user = mapper.from_dict(user_dict)
print(new_user.name)  # Output: Alice
print(new_user.age)   # Output: 30

# Serializar el objeto a una cadena JSON
user_json = mapper.serialize(user)
print(user_json)  # Output: '{"name": "Alice", "age": 30}'

# Deserializar la cadena JSON a un objeto
deserialized_user = mapper.deserialize(user_json)
print(deserialized_user.name)  # Output: Alice
print(deserialized_user.age)   # Output: 30

"""
    Explicación
    Métodos abstractos to_dict y from_dict:

    Estos métodos siguen siendo abstractos y deben ser implementados por cualquier subclase.
    Métodos concretos serialize y deserialize:

    serialize: Convierte un objeto a una cadena JSON utilizando el método to_dict.
    deserialize: Convierte una cadena JSON a un objeto utilizando el método from_dict.
    Ambos métodos utilizan la funcionalidad proporcionada por los métodos abstractos to_dict y from_dict para realizar sus tareas.
    UserMapper:

    Implementa los métodos abstractos to_dict y from_dict para la clase User.
    Hereda los métodos serialize y deserialize de la clase AbstractMapper.
    Ejemplo de uso:

    Se muestra cómo convertir un objeto User a un diccionario y viceversa.
    Además, se muestra cómo serializar un objeto User a una cadena JSON y deserializarlo de nuevo a un objeto User.
    Este enfoque permite definir métodos comunes en la clase abstracta que pueden ser utilizados por todas las subclases, proporcionando una funcionalidad común de manera centralizada.
"""

