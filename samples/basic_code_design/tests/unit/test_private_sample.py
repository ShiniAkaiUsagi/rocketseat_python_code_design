from unittest.mock import patch

import pytest

from samples.basic_code_design.src.private import (
    MyClass,  # ajuste o import conforme seu projeto
)


@pytest.mark.my_private_class
class TestMyPrivateClass:

    @patch.object(MyClass, "_MyClass__verify")
    @patch.object(MyClass, "_MyClass__verify_registry")
    @patch.object(MyClass, "_MyClass__insert_data")
    def test_registry_calls_private_methods(
        self, mock_insert, mock_verify_registry, mock_verify
    ):
        obj = MyClass()

        obj.registry()

        mock_verify.assert_called_once()
        mock_verify_registry.assert_called_once()
        mock_insert.assert_called_once()

    def test_registry_prints(self, capsys):
        obj = MyClass()
        obj.registry()

        captured = capsys.readouterr()
        assert "Start process" in captured.out
        assert "Verify data" in captured.out
        assert "Verify registry" in captured.out
        assert "Insert in DB" in captured.out
