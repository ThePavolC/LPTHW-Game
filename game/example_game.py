from map import Map
from commands import Parser
from forrest_room import Forrest
from pond_room import Pond
from pathway_room import Pathway
from cave_room import Cave
from passage_room import Passage
from castle_room import Castle
from engine import Engine

"""
Initializing engine and the map
"""
a_map = Map()
parser = Parser(a_map)
game = Engine(a_map, parser)

"""
Initializing rooms. Some rooms need reference to engine so they can kill/win
"""
forrest = Forrest()
pond = Pond()
pathway = Pathway(game)
cave = Cave(game)
passage = Passage(game)
castle = Castle(game)

"""
Adding all rooms to the map, with all exits at initial stage. Some exits are
modified while playing game.
"""
a_map.add_room(forrest,north=pond,east=None,south=None,west=None)
a_map.add_room(pond,north=None,east=cave,south=forrest,west=pathway)
a_map.add_room(pathway,north=None,east=pond,south=None,west=None)
a_map.add_room(cave,north=None,east=None,south=None,west=pond)
a_map.add_room(passage,north=None,east=None,south=None,west=cave)
a_map.add_room(castle,north=None,east=pathway,south=passage,west=None)

# starting room
a_map.set_current_room(forrest)
# starting the game
game.play()
