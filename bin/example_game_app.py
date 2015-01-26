import web
from game import example_game

urls = (
    '/game', 'Game',
    '/', 'Index',
)

app = web.application(urls, globals())

if web.config.get('_session') is None:
    store = web.session.DiskStore('sessions')
    session = web.session.Session(app, store,
                                    initializer={'room': None})
    web.config._session = session
else:
    session = web.config._session

render = web.template.render('templates/', base='layout')

class Index(object):
    def GET(self):
        session.room = example_game.a_map.get_current_room()
        web.seeother("/game")

    def POST(self):
        return "Index POST"

class Game(object):
    def GET(self):
        state = example_game.game.get_state()
        if state == "playing":
            room = example_game.a_map.get_current_room()
            room_object = example_game.a_map.find_room_object(room)
            return render.show_room(room=room,state=state,room_object=room_object)
        elif state == "killed":
            return render.you_died()
        else:
            return "You won"

    def POST(self):
        form = web.input(action=None)

        if session.room and form.action:
            example_game.game.get_parser().parse(form.action)
            session.room = example_game.a_map.get_current_room()

        web.seeother("/game")

if __name__ == "__main__":
    app.run()
