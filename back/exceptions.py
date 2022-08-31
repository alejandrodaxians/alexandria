from fastapi import Request, FastAPI
from fastapi.responses import JSONResponse

class BookNotFoundException(Exception):
    def __init__(self, name: str):
        self.keyword = name

class IdNotFoundException(Exception):
    def __init__(self, id: int):
        self.id = id

def exception_handler_wrapper(app: FastAPI):
    @app.exception_handler(BookNotFoundException)
    async def book_exception_handler(request: Request, exc: BookNotFoundException):
        return JSONResponse(
            status_code=404,
            content={"message": f"No coincidences found with {exc.keyword}"},
        )

    @app.exception_handler(IdNotFoundException)
    async def id_exception_handler(request: Request, exc: IdNotFoundException):
        return JSONResponse(
            status_code=404,
            content={"message": f"No book with id {exc.id} found"},
        )