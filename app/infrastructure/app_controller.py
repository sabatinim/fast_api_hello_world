from typing import Optional

from fastapi import FastAPI

from app.usecase.app_usecase import UseCase


class AppController:

    def __init__(self, app: FastAPI, use_case: UseCase):
        @app.get("/items/{item_id}")
        def read_item(item_id: int, q: Optional[str] = None):
            return {
                "item_id": item_id, "q": q, "use_case": use_case.run()
            }
