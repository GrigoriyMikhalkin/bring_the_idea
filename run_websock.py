import logging
import signal
import time

from websock_server import app

from tornado.options import options, parse_command_line
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop


def shutdown(server):
    ioloop = IOLoop.current()
    logging.info("Stopping server.")
    server.stop()

    def finalize():
        ioloop.stop()
        logging.info("Stopped.")

    ioloop.add_timeout(time.time()+1, finalize)


if __name__ == "__main__":
    parse_command_line()
    server = HTTPServer(app)
    server.listen(options.port)
    signal.signal(signal.SIGINT, lambda sig, frame: shutdown(server))
    logging.info('Starting server on localhost:{}'.format(options.port))
    IOLoop.current().start()
