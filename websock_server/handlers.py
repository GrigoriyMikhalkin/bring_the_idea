from tornado.websocket import WebSocketHandler
from tornado.options import options
from tornado import gen


class CommentHandler(WebSocketHandler):
    def open(self,idea_id):
        self.idea_id = idea_id
        print("Websocket opened")
        self.application.add_subscriber(self.idea_id, self)

    def on_close(self):
        print("Websocket closed")
        self.application.remove_subscriber(self.idea_id, self)

    def on_message(self, message):
        if message == "NC":
            self.application.broadcast(message, channel=self.idea_id, sender=self)
        
    def check_origin(self, origin):
        return options.debug
