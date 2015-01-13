from item import Item

class Money(Item):
    """
    Item used to bribe soldier in Pathway
    """

    def __init__(self,room):
        self.room = room
        super(Money,self).__init__('money')
        self.use_counter = 2
        
    def use(self):
        """
        When money used twice then it will kill user
        """
        if self.use_counter == 2:
            print self.room.money_used(self.use_counter)
            self.use_counter -= 1
        elif self.use_counter == 1:
            print self.room.money_used(self.use_counter)
