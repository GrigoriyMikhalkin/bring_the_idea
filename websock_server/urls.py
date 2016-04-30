from .handlers import *

routes = [
    (r"/comments/(?P<idea_id>[0-9]+)", CommentHandler),
]
