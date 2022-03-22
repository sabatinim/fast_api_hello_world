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


def app_controller(use_case: UseCase = ProductionUseCase()) -> FastAPI:
    app = FastAPI()

    @app.get("/items/{item_id}")
    def read_item(item_id: int, q: Optional[str] = None):
        return {
            "item_id": item_id, "q": q, "use_case": use_case.run()
        }

    return app


if __name__ == "__main__":
    uvicorn.run(app_controller(), host="0.0.0.0", port=8080)
