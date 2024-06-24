"""
    el principio de Inversión de Dependencias (DIP) establece que los módulos de alto nivel no deberían depender de módulos de bajo nivel. Ambos deberían depender de abstracciones (interfaces). 

    Supongamos que estamos creando un sistema de notificaciones que puede enviar notificaciones por correo electrónico y SMS. Queremos que el módulo de notificaciones sea flexible y no dependa directamente de las implementaciones concretas de los servicios de envío de notificaciones.
"""

from abc import ABC, abstractmethod

class Notifier(ABC):
    @abstractmethod
    def send(self, message: str):
        pass

"""
    Implementaciones Concretas
    Luego, implementamos las clases concretas para el envío de notificaciones por correo electrónico y SMS:
"""

class EmailNotifier(Notifier):
    def send(self, message: str):
        print(f"Sending email with message: {message}")

class SMSNotifier(Notifier):
    def send(self, message: str):
        print(f"Sending SMS with message: {message}")

class PushNotifier(Notifier):
    def send(self, message: str):
        print(f"Sending push notification with message: {message}")

"""
    Clase de Notificación
    Ahora, creamos una clase Notification que utiliza la abstracción Notifier para enviar mensajes:
"""

class Notification:
    def __init__(self, notifier: Notifier):
        self.notifier = notifier

    def notify(self, message: str):
        self.notifier.send(message)

"""
    Ejemplo de Uso
    A continuación, mostramos cómo utilizar la clase Notification con diferentes tipos de notificaciones:
"""

# Enviar notificación por correo electrónico
email_notifier = EmailNotifier()
email_notification = Notification(email_notifier)
email_notification.notify("Hello via Email!")

# Enviar notificación por SMS
sms_notifier = SMSNotifier()
sms_notification = Notification(sms_notifier)
sms_notification.notify("Hello via SMS!")

# Enviar notificación push
push_notifier = PushNotifier()
push_notification = Notification(push_notifier)
push_notification.notify("Hello via Push Notification!")