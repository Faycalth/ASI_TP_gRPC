from random import randint

class GameManager:
    def __init__(self):
        self.user_manager = UserManager()
        self.card_manager = CardManager()
        self.room_list = []
        self.transaction_list = [] 
    
    def get_card_list(self):
        return self.card_manager.get_card_list()

    def get_user_list(self):
        return self.user_manager.get_user_list()

    def get_user_info(self):
        user = self.user_manager.user_list[0]
        return user
    
    def buy_card(self, card_id):
        if 0 <= int(card_id) < len(self.card_manager.get_card_list()):
            return self.card_manager.buy_card(card_id, self.get_user_info().name)
        
    def sell_card(self, card_id):
        if 0 <= int(card_id) < len(self.card_manager.get_card_list()):
            return self.card_manager.sell_card(card_id)
  
class UserManager:
    def __init__(self):
        self.user_list = []
        for i in range(5):
            self.user_list.append(User(i, "name_"+str(i), "connected"))    
    
    def get_user_list(self):
        ret = ""
        for u in self.user_list:
            ret += str(u) + "\n"
        return ret

class User:
    def __init__(self, id, name, status):
        self.id = id
        self.name = name
        self.status = status
    
    def __str__(self):
        return "User : id=" + str(self.id) + ", name=" + str(self.name) + ", status=" + str(self.status)


class CardManager:
    def __init__(self):
        self.card_list = [Card(i, "name_"+str(i), "type_"+str(i), randint(1,99), None) for i in range(10)]
    
    def get_card_list(self):
        ret = ""
        for c in self.card_list:
            ret += str(c) + "\n"
        return ret
    
    def get_card_by_id(self, id):
        for c in self.card_list:
            if c.id == int(id):
                return c 

    def buy_card(self, card_id, user_name):
        self.get_card_by_id(card_id).owner = user_name
        return "Vous avez acheté la carte " + card_id

    def sell_card(self, card_id):
        self.get_card_by_id(card_id).owner = None
        return "Vous avez vendu la carte " + card_id

class Card:
    def __init__(self, id, name, type, price, owner):
        self.id = id
        self.name = name
        self.type = type
        self.price = price
        self.owner = owner
    
    def __str__(self):
        return "Card : id=" + str(self.id) + ", name=" + str(self.name) + ", type=" + str(self.type) + ", price=" + str(self.price) + ", owner = " + str(self.owner)