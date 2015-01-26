class Item(object):
    """
    Item class which other items inherit from
    """
    

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def use(self):
        pass
