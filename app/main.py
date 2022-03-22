import uvicorn
from fastapi import FastAPI

from app.infrastructure.app_controller import AppController
from app.usecase.app_usecase import UseCase, ProductionUseCase


def startup(use_case: UseCase = ProductionUseCase()):
    app = FastAPI()
    AppController(app, use_case)
    return app


if __name__ == "__main__":
    uvicorn.run(startup(), host="0.0.0.0", port=8080)
