class Customer:
    def __init__(self, name, wallet, fav_performer):
        self.name = name
        self.wallet = wallet 
        self.fav_performer = fav_performer 

    def can_afford(self, ticket_price):
        if self.wallet >= ticket_price:
            return True 
        else: False 
    