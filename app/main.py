from abc import abstractmethod
from typing import Optional

import uvicorn
from fastapi import FastAPI


class UseCase:
    @abstractmethod
    def run(self):
        pass


class ProductionUseCase(UseCase):
    def run(self):
        return "Production Code"


class AppController:

    def __init__(self, app: FastAPI, use_case: UseCase):
        @app.get("/items/{item_id}")
        def read_item(item_id: int, q: Optional[str] = None):
            return {
                "item_id": item_id, "q": q, "use_case": use_case.run()
            }


def startup(use_case: UseCase = ProductionUseCase()):
    app = FastAPI()
    AppController(app, use_case)
    return app


if __name__ == "__main__":
    uvicorn.run(startup(), host="0.0.0.0", port=8080)
