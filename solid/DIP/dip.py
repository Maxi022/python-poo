"""
    Ejemplo sin DIP (violando el principio)
    En este ejemplo, una clase Worker y una clase Manager donde Manager depende directamente de la implementación concreta de Worker.
"""

class Worker:
    def work(self):
        print("Worker is working")

class Manager:
    def __init__(self):
        self.worker = Worker()

    def manage(self):
        self.worker.work()

# Ejemplo de uso
manager = Manager()
manager.manage()

"""
    Ejemplo con DIP
    Ahora separamos las abstracciones (interfaces) de las implementaciones y hacemos que tanto los módulos de alto nivel como los de bajo nivel dependan de abstracciones.
"""

from abc import ABC, abstractmethod

# Definimos una abstracción
class Workable(ABC):
    @abstractmethod
    def work(self):
        pass

# Implementación concreta de la abstracción
class Worker(Workable):
    def work(self):
        print("Worker is working")

# Manager depende de la abstracción y no de la implementación concreta
class Manager:
    def __init__(self, worker: Workable):
        self.worker = worker

    def manage(self):
        self.worker.work()

# Ejemplo de uso
worker = Worker()
manager = Manager(worker)
manager.manage()

"""
    Explicación:
    Definición de la Abstracción: Creamos una interfaz Workable que define el método work().
    Implementación Concreta: Worker implementa la interfaz Workable.
    Dependencia de la Abstracción: Manager ahora depende de la interfaz Workable en lugar de la clase concreta Worker.
    Inyección de Dependencias: En el ejemplo de uso, inyectamos una instancia de Worker en el Manager.
    De esta manera, Manager puede trabajar con cualquier implementación de Workable sin conocer los detalles de la implementación concreta, cumpliendo así con el principio de Inversión de Dependencias (DIP).
"""