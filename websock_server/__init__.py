from .urls import routes
from .config import *

from collections import defaultdict

from tornado.websocket import WebSocketClosedError
from tornado.options import options
from tornado.web import Application


class CommentApplication(Application):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.subscriptions = defaultdict(list) # channel : [ subscribers list ]

    def add_subscriber(self, channel, subscriber):
        self.subscriptions[channel].append(subscriber)

    def remove_subscriber(self, channel, subscriber):
        self.subscriptions[channel].remove(subscriber)

    def get_subscribers(self, channel):
        return self.subscriptions[channel]

    def broadcast(self, message, channel, sender):
        subscribers = self.get_subscribers(channel)
        for subscriber in subscribers:
            if subscriber != sender:
                try:
                    subscriber.write_message(message)
                except WebSocketClosedError:
                    self.remove_subscriber(channel, subscriber)


app = CommentApplication(routes, debug=options.debug)
