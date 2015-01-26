from room import Room
from rock_item import Rock
from apple_item import Apple

class Cave(Room):
    """
    Room with the killing bear in it.
    """

    def __init__(self, game):
        self.name = "Cave"
        self.description = ("Very dark cave. It looks like it's rocks and some "
        "old apples lying around. Oh wait, is that a sleeping bear?")
        self.items = [Rock(self), Apple(self)]
        self.game = game
        self.apple_used = False
        
    def kill_by_bear(self):
        """
        Kills user when he uses rock on bear
        """
        
        apple_used_text = "You are throwing rocks around, very good."
        bear_up_text = ("You woke up bear by throwing rock at him. He is not happy. You "
        "are trying to run away, but he gots you and it's not pretty, for you.")
        
        if self.apple_used:
            print apple_used_text
            return apple_used_text
        
        print bear_up_text
        self.game.kill()
        return bear_up_text
        
    def use_apple(self):
        """
        Opens exit and get rid of the bear in room
        """
        
        apple_used1_text = "You threw apple out of cave and bear run after it."
        new_description = ("Very dark cave. It looks like it's rocks and some "
        "old apples lying around. Thank god no bears around.")
        apple_used2_text = "Little bit bitten but still good apple, yummmy."
        
        
        if self.apple_used:
            print apple_used2_text
            return apple_used2_text
        
        self.apple_used = True
        self.description = new_description
        self.game.get_map().add_exit(self,'east','Passage')
        print apple_used1_text
        return apple_used1_text
