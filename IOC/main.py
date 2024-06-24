"""
    Existen contenedores de inyección de dependencias que facilitan la gestión de dependencias y ayudan a seguir los principios SOLID en el desarrollo de software. Algunas bibliotecas populares para este propósito incluyen injector, punq y dependency_injector. Vamos a ver un ejemplo usando dependency_injector, que es una biblioteca muy potente y flexible.
"""

"""
    Ejemplo usando dependency_injector
    Primero, instala la biblioteca dependency_injector:

    pip install punq
"""

"""
    Ejemplo de punq
    Aquí hay un ejemplo sencillo que muestra cómo registrar y resolver dependencias en punq, similar a lo que harías con awilix:
"""

import punq

# Crear el contenedor de inyección de dependencias
container = punq.Container()

# Definir una interfaz (abstract class) y clases concretas
from abc import ABC, abstractmethod

class Notifier(ABC):
    @abstractmethod
    def send(self, message: str):
        pass

class EmailNotifier(Notifier):
    def send(self, message: str):
        print(f"Sending email with message: {message}")

class SMSNotifier(Notifier):
    def send(self, message: str):
        print(f"Sending SMS with message: {message}")

# Registrar las dependencias
container.register(Notifier, EmailNotifier)

# Definir una clase que depende de Notifier
class NotificationService:
    def __init__(self, notifier: Notifier):
        self.notifier = notifier

    def notify(self, message: str):
        self.notifier.send(message)

# Resolver las dependencias y crear la instancia
notification_service = container.resolve(NotificationService)

# Enviar una notificación
notification_service.notify("Hello via Email!")

"""
const { createContainer, asClass } = require('awilix');

// Crear el contenedor de inyección de dependencias
const container = createContainer();

// Definir una interfaz y clases concretas
class EmailNotifier {
    send(message) {
        console.log(`Sending email with message: ${message}`);
    }
}

class SMSNotifier {
    send(message) {
        console.log(`Sending SMS with message: ${message}`);
    }
}

// Registrar las dependencias
container.register({
    notifier: asClass(EmailNotifier).singleton(),
});

// Definir una clase que depende de Notifier
class NotificationService {
    constructor({ notifier }) {
        this.notifier = notifier;
    }

    notify(message) {
        this.notifier.send(message);
    }
}

// Resolver las dependencias y crear la instancia
const notificationService = container.resolve('notificationService');

// Enviar una notificación
notificationService.notify('Hello via Email!');

"""