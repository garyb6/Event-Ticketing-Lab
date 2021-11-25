import unittest
from src.performer import Performer 

class TestPerformer(unittest.TestCase):
    def setUp(self):
        self.performer = Performer ("Chef")

    def test_performer_has_name(self):
        self.assertEqual ("Chef", self.performer.name)