import unittest
from src.main import main


class TestHello(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(
            main("Hello from bootstrap-python-project!"),
            "Hello from bootstrap-python-project!",
        )
