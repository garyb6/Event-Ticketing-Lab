import unittest
from src.event import Event 
from src.customer import Customer
from src.performer import Performer

class TestEvent(unittest.TestCase):
    def setUp(self):
        self.cartman = Customer ("Cartman", 20.00, "Chef")
        self.chef = Performer ("Chef")
        self.event = Event ("Cochella", 100, 10.00,[self.cartman], [self.chef])
        self.customer_list = [] 

    def test_event_has_name(self):
        self.assertEqual ("Cochella", self.event.name)
    
    def test_add_customer_to_customer_list(self):
        self.customer_list.append(self.cartman)
        self.assertEqual (1, len(self.customer_list))
    
#     @unittest.skip("delete")
#         def test_sell_ticket(self, customer):
# #         customer.can_afford() 
        
# # #check if customer has enough for ticket 
# #         #if True: 
# #             add customer to customer list
# #             add_money_to_revenue
# #             deduct_money_from_wall