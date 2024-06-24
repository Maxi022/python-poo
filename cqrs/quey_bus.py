from pybus.core import Bus
from pybus.dispatchers import synchronous_dispatcher
from functools import wraps

# Definir el Query Bus
query_bus = Bus(dispatcher=synchronous_dispatcher)

# Decorador para suscribir una clase a un Query Handler
def query_handler(query_cls):
    def decorator(cls):
        query_bus.subscribe(query_cls, cls())
        return cls
    return decorator

# Definir los comandos y consultas
class GetSomethingQuery:
    pass

# Decorar la clase CasoDeUso para suscribirla al Query Handler
@query_handler(GetSomethingQuery)
class CasoDeUso:
    def execute(self, *args, **kwargs):
        print(f"Executing command or query with args: {args}, kwargs: {kwargs}")

# Ejecutar la consulta
query_bus.execute(GetSomethingQuery())

"""
    En este código:

    Definimos un decorador query_handler que toma una clase de consulta como argumento y devuelve otro decorador.
    El decorador devuelto envuelve la clase CasoDeUso, suscribiéndola al Query Handler correspondiente.
    Cuando se ejecuta la consulta GetSomethingQuery, se ejecutará automáticamente el método execute de la clase CasoDeUso.
    Este enfoque te permite definir la lógica de tu caso de uso en la clase CasoDeUso y automáticamente suscribirla al Query Handler deseado usando el decorador @query_handler.
"""