import unittest

from fastapi.testclient import TestClient
from app.main import app


class TestApp(unittest.TestCase):

    def setUp(self) -> None:
        self.client = TestClient(app)

    def test_read_root(self):
        response = self.client.get("/")
        self.assertEqual(200, response.status_code)
        self.assertEqual({"msg": "Hello World"}, response.json())

    def test_read_item(self):
        response = self.client.get("/items/987?q=this%20is%20the%20query")
        self.assertEqual(200, response.status_code)
        self.assertEqual({"item_id": 987, "q": "this is the query"}, response.json())
