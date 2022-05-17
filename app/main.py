"""
    Main module of payment gateway backend.
"""

import uvicorn as uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.user.route import user


def create_app() -> FastAPI:
    app = FastAPI(title='User Demo', debug=False)

    app.include_router(user.router)

    return app


app = create_app()
origins = [
    "*"
    # "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run(app, port=8000)
