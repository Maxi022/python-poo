from pybus.core import Bus
from pybus.dispatchers import synchronous_dispatcher
from functools import wraps

# Definir el Command Bus
command_bus = Bus(dispatcher=synchronous_dispatcher)

# Decorador para suscribir una clase a un Command Handler
def command_handler(command_cls):
    def decorator(cls):
        command_bus.subscribe(command_cls, cls())
        return cls
    return decorator

# Definir los comandos y consultas
class DoSomethingCommand:
    pass

# Decorar la clase CasoDeUso para suscribirla al Command Handler
@command_handler(DoSomethingCommand)
class CasoDeUso:
    def execute(self, *args, **kwargs):
        print(f"Executing command or query with args: {args}, kwargs: {kwargs}")

# Ejecutar el comando
command_bus.execute(DoSomethingCommand())

"""
    En este código:

    Definimos un decorador command_handler que toma una clase de comando como argumento y devuelve otro decorador.
    El decorador devuelto envuelve la clase CasoDeUso, suscribiéndola al Command Handler correspondiente.
    Cuando se ejecuta el comando DoSomethingCommand, se ejecutará automáticamente el método execute de la clase CasoDeUso.
    Este enfoque te permite definir la lógica de tu caso de uso en la clase CasoDeUso y automáticamente suscribirla al Command Handler deseado usando el decorador @command_handler.
"""