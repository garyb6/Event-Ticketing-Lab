import unittest
from src.event import Event 
from src.customer import Customer
from src.performer import Performer

class TestEvent(unittest.TestCase):
    def setUp(self):
        self.cartman = Customer ("Cartman", 20.00, "Chef")
        self.chef = Performer ("Chef")
        self.event = Event ("Cochella", 100, 10.00,[self.cartman], [self.chef])

    def test_event_has_name(self):
        self.assertEqual ("Cochella", self.event.name)
    
    def test_sell_ticket(self, customer):
        pass 
