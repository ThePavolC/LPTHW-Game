from room import Room
from torch_item import Torch

class Passage(Room):
    """
    Room with torch and wooden door in it
    """

    def __init__(self, game):
        self.name = "Passage"
        self.description = ("It looks like there is a trap door above you but "
        "it's locked. You have no keys on you and there is nothing around. "
        "Thank god there is this little torch otherwise you couldn't see a thing")
        self.items = [Torch(self)]
        self.game = game
        self.torch_used = False
        
    def use_torch(self):
        if self.torch_used:
            print "Doors are already burned, ashes are still warm."
            return
        
        self.torch_used = True
        print "You burned down locked wooden doors. What kind of security is that?"
        self.description = ("It looks like there is a trap door above you, and "
        "after you burned them there is only whole in the wall.")
        self.game.get_map().add_exit(self,'north','Castle')
