from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse

from back.api.endpoints.crud import router
from back.api.exceptions import exception_handler_wrapper
from back.config.properties import APP_DESCRIPTION, APP_TITLE, BACKEND_URL

app = FastAPI(
    title=APP_TITLE,
    description=APP_DESCRIPTION,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[BACKEND_URL], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

exception_handler_wrapper(app)

@app.get("/", include_in_schema=False)
def root():
    # return {"message": "FastAPI app Running"}
    return RedirectResponse(url="/docs")
