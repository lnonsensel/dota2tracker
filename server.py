from http.server import BaseHTTPRequestHandler, HTTPServer
from json import loads as json_loads



class MyServer(HTTPServer):

    def init_state(self):
        self.last_state = None
        self.handlers = []
        self.on_ability_cast = []
        self.on_exit = []

    def handle_state(self, state):
        for handler in self.handlers:
            handler(self.last_state, state)

class MyRequestHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        length = int(self.headers['Content-Length'])
        body = self.rfile.read(length).decode('utf-8')
        state = json_loads(body)
        self.send_header('Content-type', 'text/html')
        self.send_response(200)
        self.end_headers()
        self.server.handle_state(state)
        self.server.last_state = state

    def log_message(self, format, *args):
        return

class Server():
    
    def __init__(self, ip='127.0.0.1', port=5000):
        self.ip = ip
        self.port = port
        self.server = MyServer((ip, port), MyRequestHandler)
        self.server.init_state()

    def start(self):

        print(f"GSI server listening on {self.ip}:{self.port} - CTRL+C to stop")
        if len(self.server.handlers) == 0 and len(self.server.on_ability_cast) == 0:
            print("Warning: no handlers were added, nothing will happen")
        try:
            self.server.serve_forever()
        except (KeyboardInterrupt, SystemExit):
            pass
        self.server.server_close()
        print("Server stopped.")

    def on_update(self, func):

        self.server.handlers.append(func)



