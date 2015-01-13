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
        if self.apple_used:
            print "You are throwing rocks around, very good."
            return
        print ("You woke up bear by throwing rock at him. He is not happy. You "
        "are trying to run away, but he gots you and it's not pretty, for you.")
        self.game.kill()
        
    def use_apple(self):
        """
        Opens exit and get rid of the bear in room
        """
        if self.apple_used:
            print "Little bit bitten but still good apple, yummmy."
            return
        
        self.apple_used = True
        print "You threw apple out of cave and bear run after it."
        self.description = ("Very dark cave. It looks like it's rocks and some "
        "old apples lying around. Thank god no bears around.")
        self.game.get_map().add_exit(self,'east','Passage')
