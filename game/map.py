class Map(object):
    """
    Map describing whole world with all rooms and exits
    """


    def __init__(self):
        # list of room objects, which is room and it's exits
        self.rooms = []
        self.current_room = None
    
    def add_room(self,room,north=None,east=None,south=None,west=None):
        """
        Add new room object, i.e room and exits
        """
        self.rooms.append({
            'room' : room,
            'north' : north,
            'east' : east,
            'south' : south,
            'west' : west
        })
    
    def add_exit(self,room,exit,exit_room_name):
        """
        Add exit to current room.
        Used when some object is used and it opens new way
        """
        room_object = self.find_room_object(room)
        exit_room = None
        for r in self.rooms:
            if r.get('room').get_name() == exit_room_name:
                exit_room = r.get('room')
        room_object[exit] = exit_room
    
    def set_current_room(self, room):
        """
        Set starting room.
        Could be used for teleportation
        """
        new_room = self.find_room_object(room)
        if new_room:
            self.current_room = new_room
        else:
            print "Room doesnt exist"
    
    def get_current_room(self):
        if self.current_room:
            return self.current_room.get('room')
        else:
            print "No current room is set"
            return None
    
    def get_exit(self, exit):
        """
        Get exit room by exit name
        """
        return self.find_room_object(self.get_current_room()).get(exit)
    
    def print_current_room_exits(self):
        """
        Print used with 'show' command
        """
        room_object = self.find_room_object(self.get_current_room())
        print "-- Exits --"
        print "\tNorth:", room_object.get('north')
        print "\tEast:", room_object.get('east')
        print "\tSouth:", room_object.get('south')
        print "\tWest:", room_object.get('west')
    
    def find_room_object(self, room):
        """
        Find room object by it's room
        """
        for room_object in self.rooms:
            existing_room = room_object.get('room')
            if room == existing_room:
                return room_object
    
    def change_room(self, next_room):
        """
        Go to next room from the list.
        Else statement is probably irrelevant there.
        There is also call for leaving/exiting methods which is not used.
        """
        found_room = self.find_room_object(next_room)
        if found_room:
            self.current_room.get('room').leaving()
            self.current_room = found_room
            found_room.get('room').entering()
        else:
            print ("Cant go to next room, the room '%s' doesnt exists" 
                % next_room)
