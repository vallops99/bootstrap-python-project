import unittest

from staticker_pkg.staticker import staticker
from randomizer_pkg.randomizer import randomizer

from src.main import main


class TestTool(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(
            main("Hello from bootstrap-python-project!"),
            "Hello from bootstrap-python-project!",
        )

    def test_workspace(self):
        self.assertEqual(
            staticker(),
            "Static string to show UV workspace!",
        )

    def test_randomizer(self):
        assert type(randomizer()) is float
