import textwrap

class Room(object):
    """
    Room object which other room inherit from
    """


    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.items = items

    def get_name(self):
        return self.name
        
    def print_description(self):
        description = "-- %s --\n" % self.name
        description += textwrap.fill(self.description, width=40, initial_indent='  ')
        print description
        return description

    def show(self):
        """
        Used with 'show' command
        """
        return self.print_description()

    def get_item(self, item_name):
        """
        Used when using objects
        """
        for item in self.items:
            if item.get_name() == item_name:
                return item
        else:
            print "The '%s' is not here." % item_name
            return None
    
    def leaving(self):
        """
        Exucete before leaving room
        """
        pass
        
    def entering(self):
        """
        Exucete after leaving room
        """
        pass
        
    def __str__(self):
        """
        Used in 'show' command when printing exits
        """
        return self.get_name()
