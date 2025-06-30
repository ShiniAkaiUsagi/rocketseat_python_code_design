from abc import ABC, abstractmethod


class NotificationSender(ABC):

    @abstractmethod
    def send_notification(self, message: str) -> None:
        pass  # pragma: no cover


# Definir a regra de construção das demais classes em que ela é implementada /herança


class EmailNotificationSender(NotificationSender):
    def send_notification(self, message: str) -> None:
        print(f"Email: {message}")


class SMSNotificationSender(NotificationSender):
    def send_notification(self, message):
        print(f"SMS: {message}")


class Notificator:
    def __init__(self, notification_sender: NotificationSender) -> None:
        self.__notification_sender = notification_sender

    def send(self, message: str) -> None:
        # TODO: implementar validação
        self.__notification_sender.send_notification(message)


obj = EmailNotificationSender()
obj.send_notification("Olá, mundo!")

obj = SMSNotificationSender()
obj.send_notification("Olás, mundos!")


# Injeção de dependência
obj = Notificator(EmailNotificationSender())
obj.send("Olá, mundo!")

obj = Notificator(SMSNotificationSender())
obj.send("Olás, mundos!")

# obj = NotificationSender()
# obj.send_notification("Olá, mundo!")
