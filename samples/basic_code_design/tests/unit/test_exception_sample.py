import pytest

from samples.basic_code_design.src.exception_raw import HttpUnprocessableEntityError


@pytest.mark.exception
class TestException:

    def test_http_unprocessable_entity_error_attributes(self):
        msg = "Test error message"
        error = HttpUnprocessableEntityError(msg)

        assert error.message == msg
        assert error.name == "UnprocessableEntity"
        assert error.status_code == 422
        assert str(error) == msg
