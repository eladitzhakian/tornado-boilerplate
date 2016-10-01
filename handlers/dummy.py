from handlers.base import BaseRequestHandler


class DummyHandler(BaseRequestHandler):

    def get(self):
        self.render("index.html")

    def post(self):
        name = self.get_json_argument("name", "world")

        self.finish("Hello, {!s}".format(name))
