# list of commands used in game
COMMANDS = {
    'GO' : ['go','run','walk'],
    'SHOW' : 'show',
    'HELP' : 'help',
    'USE' : 'use'
}

class Parser(object):
    """
    Parses commands and calls correct methods in objects
    """
    
    
    def __init__(self, a_map):
        self.a_map = a_map
        
    def parse(self, command):
        """
        Compare imput command with command in our command list

        'Go' implementation shows possibility to use different words
        to do same command.
        """
        command_list = command.strip().lower().split(' ')
        if command_list[0] in COMMANDS['GO']:
            self.go(command_list)
        elif command_list[0] == COMMANDS['SHOW']:
            self.show()
        elif command_list[0] == COMMANDS['HELP']:
            self.help()
        elif command_list[0] == COMMANDS['USE']:
            self.use(command_list)
        else:
            print "Command '%s' not recognized." % command
            return None
        
    def go(self, command_list):
        """
        Changes room to one of the rooms from exits
        """
        if len(command_list) > 1:
            direction = command_list[1]
            if direction in ['north','south','east','west']:
                next_room = self.a_map.get_exit(direction)
                if next_room:
                    self.a_map.change_room(next_room)
                    return next_room
                else:
                    print "You can't go there"
            else:
                print "To use 'go', type 'go <direction>'"
        else:
            print "To use 'go', type 'go <direction>'"
        return None
                    
    def show(self):
        """
        Prints out room description and exits
        """
        self.a_map.get_current_room().show()
        self.a_map.print_current_room_exits()
        
    def help(self):
        """
        List of commands
        """
        print "Commands:"
        for c in COMMANDS:
            print "\t%s" % COMMANDS[c]
        return COMMANDS

    def use(self, command_list):
        """
        Use item in current room
        """
        if len(command_list) > 1:
            item_name = command_list[1]
            item = self.a_map.get_current_room().get_item(item_name)
            if item:
                item.use()
        return None
    
    def run_commands(self, commands_list):
        """
        To test game I just pass it list of winning/killing commands
        """
        for command in commands_list:
            self.parse(command)
