from room import Room

class Pond(Room):
    """
    Just pond room, not much going on here.
    """

    def __init__(self):
        self.name = "Pond"
        self.description = ("In the middle of forrest, little pond. Only sound"
        " of frogs and moon's reflection in the water.")
        self.items = []
