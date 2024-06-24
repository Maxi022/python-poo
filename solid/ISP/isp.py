"""
    El principio de Segregación de Interfaces (ISP) establece que los clientes no deberían verse obligados a depender de interfaces que no utilizan. En otras palabras, es mejor tener varias interfaces específicas y pequeñas en lugar de una sola interfaz grande y general.
"""

"""
    A continuación, se muestra un ejemplo básico en Python para implementar el principio ISP. Imaginemos una aplicación que maneja operaciones de impresión y escaneo para diferentes dispositivos. En lugar de tener una interfaz grande que obligue a todos los dispositivos a implementar tanto impresión como escaneo, se pueden definir interfaces separadas para cada funcionalidad.

    Ejemplo sin ISP (violando el principio)
"""

from abc import ABC, abstractmethod

# Interfaz grande que fuerza a los dispositivos a implementar todas las funcionalidades
class MultifunctionDevice(ABC):
    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass

class OldPrinter(MultifunctionDevice):
    def print(self, document):
        print(f"Printing document: {document}")

    def scan(self, document):
        raise NotImplementedError("This device cannot scan")

"""
    En el ejemplo anterior, OldPrinter se ve obligado a implementar el método scan() incluso si no lo necesita, lo que viola el principio ISP.
"""

"""
    jemplo con ISP
"""

# Interfaces separadas y específicas
class Printer(ABC):
    @abstractmethod
    def print(self, document):
        pass

class Scanner(ABC):
    @abstractmethod
    def scan(self, document):
        pass

class SimplePrinter(Printer):
    def print(self, document):
        print(f"Printing document: {document}")

class SimpleScanner(Scanner):
    def scan(self, document):
        print(f"Scanning document: {document}")

class MultifunctionPrinter(Printer, Scanner):
    def print(self, document):
        print(f"Printing document: {document}")

    def scan(self, document):
        print(f"Scanning document: {document}")

# Ejemplo de uso
printer = SimplePrinter()
printer.print("My Document")

scanner = SimpleScanner()
scanner.scan("My Document")

multi_device = MultifunctionPrinter()
multi_device.print("My Document")
multi_device.scan("My Document")

"""
    Explicación:
    Definición de Interfaces Separadas: Se definen interfaces específicas Printer y Scanner, cada una con un único método abstracto.
    Implementación de Clases Concretas:
    SimplePrinter implementa solo la interfaz Printer.
    SimpleScanner implementa solo la interfaz Scanner.
    MultifunctionPrinter implementa ambas interfaces Printer y Scanner.
    Con esta estructura, las clases SimplePrinter y SimpleScanner solo dependen de las interfaces que realmente utilizan, cumpliendo así con el principio ISP.
"""