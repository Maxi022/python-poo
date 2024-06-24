"""
    Descripción de los métodos especiales
    __init__: Método constructor. Inicializa una nueva instancia de la clase.
    __repr__: Devuelve una representación oficial en cadena del objeto. Es útil para depuración y logging.
    __str__: Devuelve una representación legible en cadena del objeto. Es útil para mostrar información al usuario.
    __eq__: Compara dos objetos de la clase para ver si son iguales.
    __add__: Suma dos instancias de la clase.
    __sub__: Resta dos instancias de la clase.
    __mul__: Multiplica dos instancias de la clase.
    __truediv__: Divide dos instancias de la clase.
    __abs__: Devuelve el valor absoluto de la instancia.
    __len__: Devuelve la longitud del objeto. En este caso, devuelve el número de componentes del número complejo.
    __getitem__: Permite el acceso indexado al objeto.
    conjugate: Método personalizado que devuelve el conjugado del número complejo.
    Estos métodos especiales permiten que los objetos de la clase ComplexNumber se comporten de manera intuitiva con las operaciones y funciones integradas de Python, proporcionando una experiencia de usuario coherente y natural.
"""

class ComplexNumber:
    def __init__(self, real: float, imag: float) -> None:
        """
        Inicializa un número complejo.

        Args:
            real (float): Parte real del número complejo.
            imag (float): Parte imaginaria del número complejo.
        """
        self.real = real
        self.imag = imag

    def __repr__(self) -> str:
        """
        Devuelve una representación en cadena del número complejo.

        Returns:
            str: Representación en cadena del número complejo.
        """
        return f'ComplexNumber({self.real}, {self.imag})'

    def __str__(self) -> str:
        """
        Devuelve una cadena legible del número complejo.

        Returns:
            str: Cadena legible del número complejo.
        """
        return f'{self.real} + {self.imag}i'

    def __eq__(self, other: object) -> bool:
        """
        Compara dos números complejos para ver si son iguales.

        Args:
            other (object): Otro número complejo.

        Returns:
            bool: True si los números complejos son iguales, False de lo contrario.
        """
        if isinstance(other, ComplexNumber):
            return self.real == other.real and self.imag == other.imag
        return False

    def __add__(self, other: 'ComplexNumber') -> 'ComplexNumber':
        """
        Suma dos números complejos.

        Args:
            other (ComplexNumber): Otro número complejo.

        Returns:
            ComplexNumber: Resultado de la suma.
        """
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other: 'ComplexNumber') -> 'ComplexNumber':
        """
        Resta dos números complejos.

        Args:
            other (ComplexNumber): Otro número complejo.

        Returns:
            ComplexNumber: Resultado de la resta.
        """
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other: 'ComplexNumber') -> 'ComplexNumber':
        """
        Multiplica dos números complejos.

        Args:
            other (ComplexNumber): Otro número complejo.

        Returns:
            ComplexNumber: Resultado de la multiplicación.
        """
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return ComplexNumber(real, imag)

    def __truediv__(self, other: 'ComplexNumber') -> 'ComplexNumber':
        """
        Divide dos números complejos.

        Args:
            other (ComplexNumber): Otro número complejo.

        Returns:
            ComplexNumber: Resultado de la división.
        """
        denom = other.real ** 2 + other.imag ** 2
        real = (self.real * other.real + self.imag * other.imag) / denom
        imag = (self.imag * other.real - self.real * other.imag) / denom
        return ComplexNumber(real, imag)

    def __abs__(self) -> float:
        """
        Calcula el valor absoluto (módulo) del número complejo.

        Returns:
            float: Valor absoluto del número complejo.
        """
        return (self.real ** 2 + self.imag ** 2) ** 0.5

    def __len__(self) -> int:
        """
        Devuelve la longitud del vector del número complejo (número de componentes).

        Returns:
            int: Longitud del número complejo.
        """
        return 2  # ya que un número complejo tiene dos componentes: real e imaginaria

    def __getitem__(self, index: int) -> float:
        """
        Permite el acceso indexado al número complejo.

        Args:
            index (int): Índice de la componente (0 para la real, 1 para la imaginaria).

        Returns:
            float: La componente correspondiente del número complejo.
        """
        if index == 0:
            return self.real
        elif index == 1:
            return self.imag
        else:
            raise IndexError("Índice fuera de rango")

    def conjugate(self) -> 'ComplexNumber':
        """
        Calcula el conjugado del número complejo.

        Returns:
            ComplexNumber: Conjugado del número complejo.
        """
        return ComplexNumber(self.real, -self.imag)


# Ejemplo de uso
c1 = ComplexNumber(3, 4)
c2 = ComplexNumber(1, 2)

print(repr(c1))  # Output: ComplexNumber(3, 4)
print(str(c1))   # Output: 3 + 4i
print(c1 == c2)  # Output: False

c3 = c1 + c2
print(c3)        # Output: 4 + 6i

c4 = c1 - c2
print(c4)        # Output: 2 + 2i

c5 = c1 * c2
print(c5)        # Output: -5 + 10i

c6 = c1 / c2
print(c6)        # Output: 2.2 + 0.4i

print(abs(c1))   # Output: 5.0

print(len(c1))   # Output: 2

print(c1[0])     # Output: 3.0
print(c1[1])     # Output: 4.0

c7 = c1.conjugate()
print(c7)        # Output: 3 - 4i

"""
 En Python, los métodos especiales, también conocidos como métodos mágicos o "dunder methods" (por el doble subrayado que tienen antes y después de su nombre), permiten definir comportamientos específicos para las operaciones con objetos. Aquí hay una lista y una breve descripción de los métodos especiales más comunes:

    Métodos de Inicialización y Representación
    __init__(self, ...): Constructor de la clase, se llama cuando se crea una instancia.
    __new__(cls, ...): Crea y devuelve una nueva instancia de la clase. Se llama antes de __init__.
    __del__(self): Destructor de la clase, se llama cuando el objeto se va a eliminar.
    __repr__(self): Devuelve una representación oficial del objeto, útil para depuración.
    __str__(self): Devuelve una representación legible del objeto, útil para mostrar información al usuario.
    __bytes__(self): Devuelve una representación en bytes del objeto.
    __format__(self, format_spec): Devuelve una representación del objeto formateada según format_spec.
    Métodos de Comparación
    __lt__(self, other): Menor que (<).
    __le__(self, other): Menor o igual que (<=).
    __eq__(self, other): Igual que (==).
    __ne__(self, other): Distinto de (!=).
    __gt__(self, other): Mayor que (>).
    __ge__(self, other): Mayor o igual que (>=).
    Métodos de Operadores Aritméticos
    __add__(self, other): Suma (+).
    __sub__(self, other): Resta (-).
    __mul__(self, other): Multiplicación (*).
    __matmul__(self, other): Multiplicación de matrices (@).
    __truediv__(self, other): División (/).
    __floordiv__(self, other): División entera (//).
    __mod__(self, other): Módulo (%).
    __divmod__(self, other): Devuelve el par (cociente, resto) (divmod()).
    __pow__(self, other, modulo=None): Potencia (**).
    __lshift__(self, other): Desplazamiento a la izquierda (<<).
    __rshift__(self, other): Desplazamiento a la derecha (>>).
    __and__(self, other): AND bit a bit (&).
    __xor__(self, other): XOR bit a bit (^).
    __or__(self, other): OR bit a bit (|).
    Métodos de Operadores Aritméticos Reflejados
    __radd__(self, other): Reflejado suma (+).
    __rsub__(self, other): Reflejado resta (-).
    __rmul__(self, other): Reflejado multiplicación (*).
    __rmatmul__(self, other): Reflejado multiplicación de matrices (@).
    __rtruediv__(self, other): Reflejado división (/).
    __rfloordiv__(self, other): Reflejado división entera (//).
    __rmod__(self, other): Reflejado módulo (%).
    __rdivmod__(self, other): Reflejado divmod (divmod()).
    __rpow__(self, other): Reflejado potencia (**).
    __rlshift__(self, other): Reflejado desplazamiento a la izquierda (<<).
    __rrshift__(self, other): Reflejado desplazamiento a la derecha (>>).
    __rand__(self, other): Reflejado AND bit a bit (&).
    __rxor__(self, other): Reflejado XOR bit a bit (^).
    __ror__(self, other): Reflejado OR bit a bit (|).
    Métodos de Operadores Aritméticos Asignados
    __iadd__(self, other): Suma asignada (+=).
    __isub__(self, other): Resta asignada (-=).
    __imul__(self, other): Multiplicación asignada (*=).
    __imatmul__(self, other): Multiplicación de matrices asignada (@=).
    __itruediv__(self, other): División asignada (/=).
    __ifloordiv__(self, other): División entera asignada (//=).
    __imod__(self, other): Módulo asignado (%=).
    __ipow__(self, other, modulo=None): Potencia asignada (**=).
    __ilshift__(self, other): Desplazamiento a la izquierda asignado (<<=).
    __irshift__(self, other): Desplazamiento a la derecha asignado (>>=).
    __iand__(self, other): AND bit a bit asignado (&=).
    __ixor__(self, other): XOR bit a bit asignado (^=).
    __ior__(self, other): OR bit a bit asignado (|=).
    Métodos de Conversión
    __complex__(self): Convierte a número complejo (complex()).
    __int__(self): Convierte a entero (int()).
    __float__(self): Convierte a flotante (float()).
    __bool__(self): Convierte a booleano (bool()).
    __index__(self): Convierte a índice entero (operator.index).
    __round__(self, n=None): Redondea al número de decimales especificado (round()).
    __trunc__(self): Trunca el número (math.trunc()).
    __floor__(self): Devuelve el valor más grande entero menor o igual que el número (math.floor()).
    __ceil__(self): Devuelve el valor más pequeño entero mayor o igual que el número (math.ceil()).
    Métodos de Contenedor
    __len__(self): Devuelve la longitud del contenedor (len()).
    __getitem__(self, key): Obtiene un elemento del contenedor (obj[key]).
    __setitem__(self, key, value): Establece un elemento en el contenedor (obj[key] = value).
    __delitem__(self, key): Elimina un elemento del contenedor (del obj[key]).
    __iter__(self): Devuelve un iterador del contenedor (iter()).
    __reversed__(self): Devuelve un iterador inverso del contenedor (reversed()).
    __contains__(self, item): Comprueba si el contenedor contiene un ítem (item in obj).
    Otros Métodos Especiales
    __call__(self, *args, **kwargs): Permite que una instancia de la clase se pueda llamar como una función (obj(*args, **kwargs)).
    __enter__(self): Inicializa el contexto para el bloque with.
    __exit__(self, exc_type, exc_val, exc_tb): Finaliza el contexto para el bloque with.
    __copy__(self): Devuelve una copia superficial del objeto (copy.copy()).
    __deepcopy__(self, memo): Devuelve una copia profunda del objeto (copy.deepcopy()).
    Estos métodos especiales permiten que los objetos personalizados en Python se comporten de manera consistente con los tipos integrados, proporcionando una mayor flexibilidad y control sobre el comportamiento de los objetos en diversas situaciones.
"""