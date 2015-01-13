from item import Item

class Apple(Item):
    """
    Item is used in Cave to distract bear
    """


    def __init__(self,room):
        self.room = room
        super(Apple,self).__init__('apple')
        
    def use(self):
        self.room.use_apple()
