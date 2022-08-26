class BookInfoException(Exception):
    ...

class BookInfoNotFoundError(BookInfoException):
    def __init__(self):
        self.status_code = 404
        self.detail = "Book Info Not Found"

class BookInfoAlreadyExistsError(BookInfoException):
    def __init__(self):
        self.status_code = 409
        self.detail = "Car Info Already Exists"