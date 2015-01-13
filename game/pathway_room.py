from room import Room
from money_item import Money
from stick_item import Stick

class Pathway(Room):
    """
    Pathway with soldier and beehive.
    User needs to poke beehives so soldier will run away.
    """

    def __init__(self, game):
        self.name = "Pathway"
        self.description = ("Pathway that looks like it hasn't been used in a "
        "while. Road is hiding under the sticks and rocks, bees flying aroung "
        "with their beehive on the tree. At the end of the road you see soldier"
        " guarding the road. You have some money, but that might not help.")
        self.items = [Money(self),Stick(self)]
        self.game = game
        self.soldier_gone = False
        
    def money_used(self, counter):
        """
        If soldier is there and money are used twice then user is dead.
        """
        if self.soldier_gone:
            print "You thowed money to beehive for good luck. Good luck then."
            return
        if counter == 2:
            self.description = ("Pathway that looks like it hasn't been used in a "
            "while. Road is hiding under the sticks and rocks, bees flying aroung "
            "with their beehive on the tree. Soldier wasn't very happy with you"
            " trying to bribe him, careful now.")
            return "Soldier wasn't very happy with you trying to bribe him, careful now."
        elif counter == 1:
            self.game.kill()
            return "Soldier is pissed off, you are going to jail"
            
    def stick_used(self):
        """
        Using stick will scare off soldier and opens the way to castle
        """
        print ("You poked beehive and all bees are flying out. They start "
        "chasing soldier and he is running away.")
        self.soldier_gone = True
        self.description = ("Pathway that looks like it hasn't been used in a "
        "while. Road is hiding under the sticks and rocks, bees flying aroung "
        "with their beehive on the tree.")
        self.game.get_map().add_exit(self,'west','Castle')
    
    def kill_by_bees(self):
        """
        Poking bees is never good idea
        """
        print ("You poked beehive again and bees are after you. There is too "
        "many of them !!!")
        self.game.kill()
