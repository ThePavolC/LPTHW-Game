from item import Item

class Bed(Item):
    """
    Item is used in Castleto win the game
    """
    
    
    def __init__(self, room):
        self.room = room
        super(Bed,self).__init__('bed')
        
    def use(self):
        self.room.use_bed()
