from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost",
    "https://localhost",
    "http://localhost:3000",
    "https://localhost:3000",
    "http://localhost:8000",
    "https://localhost:8000",
]

middlewares = [
    {
        "object": CORSMiddleware,
        "args": {
            "allow_origins": origins,
            "allow_credentials": True,
            "allow_methods": ["*"],
            "allow_headers": ["*"],
        }
    }
]


def apply_middlewares(app: FastAPI):

    for middleware in middlewares:
        app.add_middleware(middleware["object"], **middleware["args"])
    return app