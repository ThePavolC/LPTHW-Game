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
        """
        Use torch to burn wooden door so you can get into castle
        """
        
        torch_used1_text = "You burned down locked wooden doors. What kind of security is that?"
        torch_used2_text = "Doors are already burned, ashes are still warm."
        new_description = ("It looks like there is a trap door above you, and "
        "after you burned them there is only hole in the wall.")
        
        if self.torch_used:
            print torch_used2_text
            return torch_used2_text
        
        self.torch_used = True
        self.description = new_description
        self.game.get_map().add_exit(self,'north','Castle')
        print torch_used1_text
        return torch_used1_text
