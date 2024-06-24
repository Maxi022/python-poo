"""
    Pybus para implementar un Command Bus y un Query Bus en Python.
    Instalación de Pybus:
    pip install pybus
"""

"""
    Uso del Command Bus y Query Bus con Pybus:
"""

from pybus.core import Bus
from pybus.dispatchers import synchronous_dispatcher

# Definir el Command Bus y Query Bus
command_bus = Bus(dispatcher=synchronous_dispatcher)
query_bus = Bus(dispatcher=synchronous_dispatcher)

# Definir los comandos y consultas
class DoSomethingCommand:
    pass

class GetSomethingQuery:
    pass

# Definir manejadores de comandos
@command_bus.handler(DoSomethingCommand)
def handle_do_something():
    print("Doing something...")

# Definir manejadores de consultas
@query_bus.handler(GetSomethingQuery)
def handle_get_something():
    return "Something"

# Ejecutar comandos y consultas
command_bus.execute(DoSomethingCommand())
result = query_bus.execute(GetSomethingQuery())

print("Result:", result)

"""
    En este ejemplo:

    Creamos instancias de Bus para el Command Bus y el Query Bus.
    Definimos clases para los comandos y las consultas (DoSomethingCommand y GetSomethingQuery).
    Usamos los decoradores @command_bus.handler y @query_bus.handler para registrar los manejadores de comandos y consultas respectivamente.
    Finalmente, ejecutamos un comando y una consulta utilizando los buses correspondientes.
"""

@queryHandler(GetSomethingQuery)
class CasoDeUso():
    def execute(self, *args, **kwargs):
        print(f"Executing command or query with args: {args}, kwargs: {kwargs}")