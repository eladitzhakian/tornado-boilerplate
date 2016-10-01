import httplib
from tornado.escape import json_decode
from tornado.web import RequestHandler, HTTPError


class BaseRequestHandler(RequestHandler):

    _DEFAULT_JSON_ARG = []

    def load_json_arguments(self):
        try:
            self.request.json_arguments = json_decode(self.request.body)
        except ValueError:
            raise HTTPError(httplib.BAD_REQUEST, "Could not decode JSON body")

    def get_json_argument(self, name, default=_DEFAULT_JSON_ARG):
        if not hasattr(self.request, 'json_arguments'):
            self.load_json_arguments()

        if name not in self.request.json_arguments and default is self._DEFAULT_JSON_ARG:
            raise HTTPError(httplib.BAD_REQUEST, "Missing argument '{!s}'".format(name))

        return self.request.json_arguments.get(name, default)
