"""
    Para implementar la funcionalidad de suscripción a eventos mediante un decorador en Python, puedes crear un decorador personalizado que registre métodos como manejadores de eventos en una instancia del Event Bus. 
    A continuación, te muestro cómo puedes hacerlo:

    Paso 1: Crear la Clase EventBus y el Decorador @subscriber
    Primero, crea una clase EventBus y el decorador @subscriber.
"""

from pyee import BaseEventEmitter
from typing import Callable

class EventBus:
    def __init__(self):
        self.emitter = BaseEventEmitter()

    def subscribe(self, event_name: str, handler: Callable) -> None:
        self.emitter.on(event_name, handler)

    def publish(self, event_name: str, *args, **kwargs) -> None:
        self.emitter.emit(event_name, *args, **kwargs)

event_bus = EventBus()

def subscriber(event_name: str):
    def decorator(func: Callable) -> Callable:
        event_bus.subscribe(event_name, func)
        return func
    return decorator

"""
    Paso 2: Usar el Decorador en una Clase
    Ahora, puedes utilizar el decorador @subscriber para suscribir métodos a eventos específicos.
"""

class UseCase:
    @subscriber('greet')
    def handle_greet(self, name: str) -> None:
        print(f'Hello, {name}!')

    @subscriber('farewell')
    def handle_farewell(self, name: str) -> None:
        print(f'Goodbye, {name}!')

# Crear una instancia del caso de uso (opcional según tu diseño)
use_case = UseCase()

# Publicar eventos para ver los resultados
event_bus.publish('greet', 'Alice')
event_bus.publish('farewell', 'Bob')

"""
    Explicación
    Clase EventBus y Decorador @subscriber:

    La clase EventBus gestiona la suscripción y publicación de eventos.
    El decorador @subscriber(event_name) toma el nombre del evento como argumento y suscribe la función decorada al evento correspondiente en el event_bus.
    Uso del Decorador en la Clase UseCase:

    Decoramos los métodos handle_greet y handle_farewell con @subscriber('greet') y @subscriber('farewell') respectivamente para suscribirlos a los eventos 'greet' y 'farewell'.
    Al crear una instancia de UseCase, los métodos decorados se suscriben automáticamente a los eventos correspondientes.
    Publicación de Eventos:

    Utilizamos event_bus.publish('greet', 'Alice') y event_bus.publish('farewell', 'Bob') para emitir los eventos y desencadenar los manejadores suscritos.
    Este enfoque permite una suscripción elegante a eventos mediante decoradores, similar a lo que puedes hacer en otros lenguajes y frameworks.
"""