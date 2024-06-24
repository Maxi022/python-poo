"""
Python existen varias bibliotecas que te permiten trabajar con un Event Bus en memoria, similar a lo que proporciona NestJS en JavaScript. Una de las más populares y flexibles es pyee. Esta biblioteca es una implementación de los eventos de Node.js para Python, lo que facilita la creación de un sistema de eventos en memoria.
"""

"""
    Instalación
    Primero, instala pyee usando pip:
    pip install pyee

"""

"""
    Ejemplo Básico de Uso
    A continuación, te muestro un ejemplo básico de cómo utilizar pyee para crear un Event Bus en memoria:
"""

from pyee import BaseEventEmitter

# Crear una instancia del emisor de eventos
event_bus = BaseEventEmitter()

# Definir un manejador para el evento 'greet'
@event_bus.on('greet')
def handle_greet(name):
    print(f'Hello, {name}!')

# Emitir el evento 'greet'
event_bus.emit('greet', 'World')

# Definir otro manejador para el evento 'farewell'
@event_bus.on('farewell')
def handle_farewell(name):
    print(f'Goodbye, {name}!')

# Emitir el evento 'farewell'
event_bus.emit('farewell', 'World')

"""
    Explicación
    Importación y Creación del Emisor de Eventos:

    Importamos BaseEventEmitter desde pyee.
    Creamos una instancia de BaseEventEmitter llamada event_bus.
    Definición de Manejadores de Eventos:

    Utilizamos el decorador @event_bus.on('greet') para definir un manejador de eventos llamado handle_greet que se activa cuando se emite el evento 'greet'.
    Similarmente, definimos otro manejador de eventos para el evento 'farewell'.
    Emisión de Eventos:

    Utilizamos event_bus.emit('greet', 'World') para emitir el evento 'greet' con el argumento 'World'.
    Emisión del evento 'farewell' de manera similar.
"""