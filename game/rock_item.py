from item import Item

class Rock(Item):
    """
    Rock item can be used to kill the bear, but bear will kill user.
    """


    def __init__(self,room):
        self.room = room
        super(Rock,self).__init__('rock')
        
    def use(self):
        self.room.kill_by_bear()
