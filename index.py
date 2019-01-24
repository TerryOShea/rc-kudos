from http.server import BaseHTTPRequestHandler
from kudos import Kudos

import zulip
import time
import re


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        k = Kudos()
        k.get_messages()
        self.end_headers()
        return

