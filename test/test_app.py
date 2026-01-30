import unittest

from fastapi import FastAPI
from fastapi.testclient import TestClient

from app.main import UseCase, ProductionUseCase, startup


class TestableUseCase(UseCase):
    def run(self):
        return "Test Code"


class TestApp(unittest.TestCase):

    def test_e2e_production_code(self):
        client = TestClient(startup(use_case=ProductionUseCase()))
        response = client.get("/items/987?q=this%20is%20the%20query")
        self.assertEqual(200, response.status_code)
        self.assertEqual(
            {"item_id": 987, "q": "this is the query", "use_case": "Production Code"},
            response.json()
        )

    def test_e2e_testable_code(self):
        client = TestClient(startup(TestableUseCase()))
        response = client.get("/items/987?q=this%20is%20the%20query")
        self.assertEqual(200, response.status_code)
        self.assertEqual(
            {"item_id": 987, "q": "this is the query", "use_case": "Test Code"},
            response.json()
        )
