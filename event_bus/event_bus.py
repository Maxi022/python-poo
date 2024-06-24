"""
    Uso Avanzado
    Para un uso más avanzado, puedes crear clases que se suscriban a eventos y manejen la lógica de manera más estructurada. Aquí tienes un ejemplo:
"""

from pyee import BaseEventEmitter

class EventBus:
    def __init__(self):
        self.emitter = BaseEventEmitter()

    def subscribe(self, event_name, handler):
        self.emitter.on(event_name, handler)

    def publish(self, event_name, *args, **kwargs):
        self.emitter.emit(event_name, *args, **kwargs)

# Crear una instancia del EventBus
event_bus = EventBus()

# Definir manejadores
def greet_handler(name):
    print(f'Hello, {name}!')

def farewell_handler(name):
    print(f'Goodbye, {name}!')

# Suscribirse a eventos
event_bus.subscribe('greet', greet_handler)
event_bus.subscribe('farewell', farewell_handler)

# Publicar eventos
event_bus.publish('greet', 'Alice')
event_bus.publish('farewell', 'Bob')

"""
    Explicación
    Clase EventBus:

    Creamos una clase EventBus que encapsula la funcionalidad del emisor de eventos.
    Métodos subscribe y publish para suscribir manejadores y publicar eventos respectivamente.
    Creación y Uso de EventBus:

    Instanciamos EventBus.
    Definimos y suscribimos manejadores de eventos.
    Publicamos eventos para ver los resultados.
    Esta configuración te permite crear y gestionar un Event Bus en memoria de manera eficiente en Python, similar a las capacidades de NestJS en JavaScript.
"""