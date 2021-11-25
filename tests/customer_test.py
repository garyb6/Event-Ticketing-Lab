import unittest
from src.customer import Customer 
from src.performer import Performer
from src.event import Event

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.cartman = Customer ("Cartman", 20.00, "Chef")
        self.chef = Performer ("Chef")
        self.event = Event ("Cochella", 100, 10.00,[self.cartman], [self.chef])

    def test_customer_has_name(self):
        self.assertEqual ("Cartman", self.cartman.name)
    
    def test_can_afford(self):
        self.assertEqual(True, self.cartman.can_afford(self.event.ticket_price))
