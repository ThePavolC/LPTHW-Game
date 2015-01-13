from item import Item

class Torch(Item):
    """
    Torch is used to burn down doors in Passage room and lead to castle.
    """


    def __init__(self,room):
        self.room = room
        super(Torch,self).__init__('torch')
        
    def use(self):
        self.room.use_torch()
