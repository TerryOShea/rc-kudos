from http.server import BaseHTTPRequestHandler
from kudos import Kudos

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        k = Kudos()
        k.get_messages()
        self.end_headers()
        self.wfile.write(str("Hello from Python on Now 2.0!").encode())
        return
