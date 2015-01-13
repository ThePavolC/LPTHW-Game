from room import Room

class Forrest(Room):
    """
    Starting room.
    """
    
    def __init__(self):
        self.name = "Forrest"
        self.description = ("Only pine trees around and darkness. Moon strugles to "
            "shines through the trees. You have no idea how you got "
            "here. Is that a pond there ?")
        self.items = []
