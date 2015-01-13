from room import Room
from bed_item import Bed

class Castle(Room):
    """
    Final room with only bed in it. Winning pretty much at this stage.
    """

    def __init__(self, game):
        self.game = game
        self.name = "Castle"
        self.description = ("It looks like an old castle, but it looks familiar."
        "Your eyes are getting weaker and all you see is bed, hurry up!")
        self.items = [Bed(self)]
        
    def use_bed(self):
        print ("You are laying down to bed, which still feels warm. You close "
        "your eyes and suddenly you realize that you have been sleeping the "
        "whole time and it all was just a dream.")
        self.game.win()
