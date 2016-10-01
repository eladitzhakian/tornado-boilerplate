import tornado.httpserver
import tornado.ioloop
import tornado.wsgi
import settings
import logging
from logging.handlers import WatchedFileHandler
from handlers.dummy import DummyHandler


def configure_logging():
    logging.basicConfig(format=settings.LOG_FORMAT, level=settings.LOG_LEVEL)
    handler = WatchedFileHandler(filename=settings.LOG_FILENAME)
    handler.setFormatter(logging.Formatter(fmt=settings.LOG_FORMAT))
    logging.getLogger().addHandler(handler)


def create_app():
    handlers = [(r"/dummy", DummyHandler)]

    return tornado.wsgi.WSGIApplication(handlers, **settings.TORNADO_SETTINGS)


def main():
    configure_logging()
    app = create_app()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(settings.PORT, address="0.0.0.0")

    logging.info("Tornado server listening on port {!s}".format(settings.PORT))
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
