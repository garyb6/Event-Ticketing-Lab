import unittest
from src.customer import Customer 

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer ("Cartman", 20.00, "Chef")

    def test_customer_has_name(self):
        self.assertEqual ("Cartman", self.customer.name)