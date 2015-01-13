class Engine(object):
    """
    Game engine.
    Reads the commands and checks the status of the player.
    """

    def __init__(self, a_map, parser):
        self.a_map = a_map
        self.parser = parser
        self.STATE = "playing"

    def play(self):
        self.print_intro()
        while True:
            if self.STATE == "killed":
                print ""
                print "Game Over"
                print ""
                break
            if self.STATE == "win":
                print ""
                print "You won! Congratulations"
                print ""
                break
            command = raw_input("> ")
            if command == "quit":
                break
            else:
                self.parser.parse(command)
    
    def kill(self):
        self.STATE = "killed"
    
    def win(self):
        self.STATE = "win"
    
    def get_map(self):
        return self.a_map
    
    def get_parser(self):
        return self.parser
    
    def get_state(self):
        return self.STATE
    
    def print_intro(self):
        print ""
        print "This is test game."
        print ""
        print "For help type 'help'"
        print ""
