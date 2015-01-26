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
        
        money_used_when_soldier_gone_text = ("You thowed money to beehive for "
        "good luck. Good luck then.")
        new_description = ("Pathway that looks like it hasn't been used in a "
        "while. Road is hiding under the sticks and rocks, bees flying aroung "
        "with their beehive on the tree. Soldier wasn't very happy with you"
        " trying to bribe him, careful now.")
        money_used_first_text = ("Soldier wasn't very happy with you trying to"
        " bribe him, careful now.")
        money_used_second_text = "Soldier is pissed off, you are going to jail"
        
        if self.soldier_gone:
            print money_used_when_soldier_gone_text
            return money_used_when_soldier_gone_text
        if counter == 2:
            self.description = new_description
            print money_used_first_text
            return money_used_first_text
        elif counter == 1:
            self.game.kill()
            print money_used_second_text
            return money_used_second_text
            
            
    def stick_used(self):
        """
        Using stick will scare off soldier and opens the way to castle
        """
        
        stick_used_first_text = ("You poked beehive and all bees are flying "
        "out. They start chasing soldier and he is running away.")
        stick_used_second_text = "Playing with the stick ha, good for you."
        new_description = ("Pathway that looks like it hasn't been used in a "
        "while. Road is hiding under the sticks and rocks, bees flying aroung "
        "with their beehive on the tree.")
        
        if self.soldier_gone:
            print stick_used_second_text
            return stick_used_second_text
        
        self.soldier_gone = True
        self.description = new_description
        self.game.get_map().add_exit(self,'west','Castle')
        print stick_used_first_text
        return stick_used_first_text
    
    def kill_by_bees(self):
        """
        Poking bees is never good idea.
        
        This happens when you use stick twice
        """
        
        kill_by_bees_text = ("You poked beehive again and bees are after you. "
        "There is too many of them !!!")
        
        self.game.kill()
        print kill_by_bees_text
        return kill_by_bees_text
