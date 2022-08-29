from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse

from back.crud import library
from back.exceptions import exception_handler_wrapper

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

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(library)

exception_handler_wrapper(app)

@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/docs")
