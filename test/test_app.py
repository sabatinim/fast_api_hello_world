import unittest

from fastapi.testclient import TestClient

from app.main import app_controller, UseCase


class TestableUseCase(UseCase):
    def run(self):
        return "Test Code"


class TestApp(unittest.TestCase):

    def test_e2e_production_code(self):
        client = TestClient(app_controller())
        response = client.get("/items/987?q=this%20is%20the%20query")
        self.assertEqual(200, response.status_code)
        self.assertEqual(
            {"item_id": 987, "q": "this is the query", "use_case": "Production Code"},
            response.json()
        )

    def test_e2e_testable_code(self):
        client = TestClient(app_controller(use_case=TestableUseCase()))
        response = client.get("/items/987?q=this%20is%20the%20query")
        self.assertEqual(200, response.status_code)
        self.assertEqual(
            {"item_id": 987, "q": "this is the query", "use_case": "Test Code"},
            response.json()
        )
