class HttpUnprocessableEntityError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message
        self.name = "UnprocessableEntity"
        self.status_code = 422


try:
    print("Try block")
    raise HttpUnprocessableEntityError("Exception raised - eg")
except Exception as exception:
    print(exception.name)
    print(exception.status_code)
