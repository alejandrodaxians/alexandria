from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse
from sqlalchemy import create_engine


from back.api.endpoints.books_ep import router
from back.api.excphandlers import server_excp_handler, book_not_found_excp_handler
from back.config.properties import APP_DESCRIPTION, APP_TITLE, BACKEND_URL, SQL_DB_URL
from back.api.exceptions import ServerError, BookNotFoundError
from back.models.book import Base

app = FastAPI(
    title=APP_TITLE,
    description=APP_DESCRIPTION,
)

engine = create_engine(SQL_DB_URL)
Base.metadata.create_all(engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[BACKEND_URL], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

app.add_exception_handler(ServerError, server_excp_handler)
app.add_exception_handler(BookNotFoundError, book_not_found_excp_handler)

@app.get("/", include_in_schema=False)
def root():
    # return {"message": "FastAPI app Running"}
    return RedirectResponse(url="/docs")
