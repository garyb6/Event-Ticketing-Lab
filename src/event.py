from tests import performer_test


class Event:
    def __init__(self, name, ticket_price, customer_list, performer_list):
        self.name = name
        self.ticket_price = ticket_price 
        self.customer_list = customer_list 
        self.performer_list = performer_list
        self.revenue = 0 