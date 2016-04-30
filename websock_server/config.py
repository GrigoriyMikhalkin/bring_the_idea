from tornado.options import define

define("debug", default=False, type=bool, help="Debug mode")
define("port", default=8888, type=int, help="Server port")
define("allowed_host", default="localhost:8000", help="Allowed host")
