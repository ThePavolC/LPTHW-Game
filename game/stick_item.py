from item import Item

class Stick(Item):
    """
    Stick is used to poke beehive and scare off soldier. Don't use it too much
    bees will go after user.
    """


    def __init__(self,room):
        self.room = room
        super(Stick,self).__init__('stick')
        self.use_counter = 1
        
    def use(self):
        if self.use_counter == 0:
            self.room.kill_by_bees()
        else:
            self.room.stick_used()
            self.use_counter -= 1
