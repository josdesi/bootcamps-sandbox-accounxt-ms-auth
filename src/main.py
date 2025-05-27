import os
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from fastapi.middleware.cors import CORSMiddleware

from app.controller import dummy_controller
from app.controller import login_controller

app = FastAPI()


metadata = {
    "title": "accounxt-ms-auth",
    "version": "1.0.0",
    "server": {"url": os.getenv("SWAGGER_CONFIG_SERVER_URL")},
}


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", include_in_schema=True)
def read_root():
    return metadata


def custom_openapi():
    openapi_schema = get_openapi(
        title=metadata["title"],
        version=metadata["version"],
        routes=app.routes,
    )
    openapi_schema["servers"] = [{"url": metadata["server"]["url"]}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema



app.include_router(dummy_controller.router)
app.include_router(login_controller.router)
app.openapi = custom_openapi