from unittest.mock import MagicMock

import pytest

from samples.basic_code_design.src.interface_raw import (
    EmailNotificationSender,
    NotificationSender,
    Notificator,
    SMSNotificationSender,
)


@pytest.mark.notification_interface
class TestNotificationSenders:

    def test_cannot_instantiate_abstract_class(self):
        with pytest.raises(TypeError):
            NotificationSender()

    def test_email_notification_sender_prints_correctly(self, capsys):
        sender = EmailNotificationSender()
        sender.send_notification("Test email")
        captured = capsys.readouterr()
        assert "Email: Test email" in captured.out

    def test_sms_notification_sender_prints_correctly(self, capsys):
        sender = SMSNotificationSender()
        sender.send_notification("Test SMS")
        captured = capsys.readouterr()
        assert "SMS: Test SMS" in captured.out


@pytest.mark.notificator_tests
class TestNotificator:

    def test_send_calls_send_notification(self):
        mock_sender = MagicMock()
        notificator = Notificator(mock_sender)
        notificator.send("Hello!")
        mock_sender.send_notification.assert_called_once_with("Hello!")
