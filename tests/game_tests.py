from nose.tools import *
from game.map import Map
from game.commands import Parser
from game.forrest_room import Forrest
from game.pond_room import Pond
from game.pathway_room import Pathway
from game.cave_room import Cave
from game.passage_room import Passage
from game.castle_room import Castle
from game.engine import Engine

def test_win1():
    """
    Winning scenarion 1
    
    Going through cave and bear, then torching the door and to the castle
    """
    a_map = Map()
    parser = Parser(a_map)
    game = Engine(a_map, parser)
    forrest = Forrest()
    pond = Pond()
    pathway = Pathway(game)
    cave = Cave(game)
    passage = Passage(game)
    castle = Castle(game)
    
    a_map.add_room(forrest,north=pond,east=None,south=None,west=None)
    a_map.add_room(pond,north=None,east=cave,south=forrest,west=pathway)
    a_map.add_room(pathway,north=None,east=pond,south=None,west=None)
    a_map.add_room(cave,north=None,east=None,south=None,west=pond)
    a_map.add_room(passage,north=None,east=None,south=None,west=cave)
    a_map.add_room(castle,north=None,east=pathway,south=passage,west=None)
    a_map.set_current_room(forrest)
    
    assert_equal(game.get_state(), 'playing')

    win_commands = ['go north','go east','use apple','go east','use torch','go north','use bed']
    game.get_parser().run_commands(win_commands)
    
    assert_equal(game.get_state(), 'win')
    
def test_win2():
    """
    Winning scenarion 2
    
    Going through soldier and bees, then to the castle
    """
    a_map = Map()
    parser = Parser(a_map)
    game = Engine(a_map, parser)
    forrest = Forrest()
    pond = Pond()
    pathway = Pathway(game)
    cave = Cave(game)
    passage = Passage(game)
    castle = Castle(game)
    
    a_map.add_room(forrest,north=pond,east=None,south=None,west=None)
    a_map.add_room(pond,north=None,east=cave,south=forrest,west=pathway)
    a_map.add_room(pathway,north=None,east=pond,south=None,west=None)
    a_map.add_room(cave,north=None,east=None,south=None,west=pond)
    a_map.add_room(passage,north=None,east=None,south=None,west=cave)
    a_map.add_room(castle,north=None,east=pathway,south=passage,west=None)
    a_map.set_current_room(forrest)
    
    assert_equal(game.get_state(), 'playing')

    win_commands = ['go north','go west','use stick','go west','use bed']
    game.get_parser().run_commands(win_commands)
    
    assert_equal(game.get_state(), 'win')
    
def test_kill1():
    """
    Killing scenarion 1
    
    Going through cave and bear, then throwing rock at the bear
    """
    a_map = Map()
    parser = Parser(a_map)
    game = Engine(a_map, parser)
    forrest = Forrest()
    pond = Pond()
    pathway = Pathway(game)
    cave = Cave(game)
    passage = Passage(game)
    castle = Castle(game)
    
    a_map.add_room(forrest,north=pond,east=None,south=None,west=None)
    a_map.add_room(pond,north=None,east=cave,south=forrest,west=pathway)
    a_map.add_room(pathway,north=None,east=pond,south=None,west=None)
    a_map.add_room(cave,north=None,east=None,south=None,west=pond)
    a_map.add_room(passage,north=None,east=None,south=None,west=cave)
    a_map.add_room(castle,north=None,east=pathway,south=passage,west=None)
    a_map.set_current_room(forrest)
    
    assert_equal(game.get_state(), 'playing')

    win_commands = ['go north','go east','use rock']
    game.get_parser().run_commands(win_commands)
    
    assert_equal(game.get_state(), 'killed')
    
def test_kill2():
    """
    Killing scenarion 2
    
    Going through soldier and trying to bribe him, twice
    """
    a_map = Map()
    parser = Parser(a_map)
    game = Engine(a_map, parser)
    forrest = Forrest()
    pond = Pond()
    pathway = Pathway(game)
    cave = Cave(game)
    passage = Passage(game)
    castle = Castle(game)
    
    a_map.add_room(forrest,north=pond,east=None,south=None,west=None)
    a_map.add_room(pond,north=None,east=cave,south=forrest,west=pathway)
    a_map.add_room(pathway,north=None,east=pond,south=None,west=None)
    a_map.add_room(cave,north=None,east=None,south=None,west=pond)
    a_map.add_room(passage,north=None,east=None,south=None,west=cave)
    a_map.add_room(castle,north=None,east=pathway,south=passage,west=None)
    a_map.set_current_room(forrest)
    
    assert_equal(game.get_state(), 'playing')

    win_commands = ['go north','go west','use money','use money']
    game.get_parser().run_commands(win_commands)
    
    assert_equal(game.get_state(), 'killed')
    
def test_kill3():
    """
    Killing scenarion 3
    
    Going through soldier and bees, then poking bees twice
    """
    a_map = Map()
    parser = Parser(a_map)
    game = Engine(a_map, parser)
    forrest = Forrest()
    pond = Pond()
    pathway = Pathway(game)
    cave = Cave(game)
    passage = Passage(game)
    castle = Castle(game)
    
    a_map.add_room(forrest,north=pond,east=None,south=None,west=None)
    a_map.add_room(pond,north=None,east=cave,south=forrest,west=pathway)
    a_map.add_room(pathway,north=None,east=pond,south=None,west=None)
    a_map.add_room(cave,north=None,east=None,south=None,west=pond)
    a_map.add_room(passage,north=None,east=None,south=None,west=cave)
    a_map.add_room(castle,north=None,east=pathway,south=passage,west=None)
    a_map.set_current_room(forrest)
    
    assert_equal(game.get_state(), 'playing')

    win_commands = ['go north','go west','use stick','use stick']
    game.get_parser().run_commands(win_commands)
    
    assert_equal(game.get_state(), 'killed')
