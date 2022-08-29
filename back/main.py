from fastapi import FastAPI
from back.crud import library
from back.exceptions import exception_handler_wrapper
from starlette.responses import RedirectResponse

description = """
## Virtual-library Alexandria allows you to:

* Get all books
* Get all books by title coincidence
* Create books
* Delete a book by id
* Update books

"""

app = FastAPI(
    title="Virtual-library Alexandria API",
    description=description,
)

app.include_router(library)

exception_handler_wrapper(app)

@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/docs")
