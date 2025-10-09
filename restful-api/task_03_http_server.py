#!/usr/bin/python3
"""
Developing a simple API using Python
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import json

# define subclass that extends from BaseHTTPRequestHandler
class Handler(BaseHTTPRequestHandler):
    # define custom method to handle how we respond to GET requests
    def do_GET(self):
            # if user visits root (/) endpoint (OK)
            if self.path == "/":
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write("Hello, this is a simple API!".encode("utf-8"))
            # if user visits /data end point, return JSON (ok)
            elif self.path == "/data":
                # create Python dict data set
                person = {"name": "John", "age": 30, "city": "New York"}
                # serialize data to json string
                json_person = json.dumps(person).encode("utf-8")
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(json_person)
            # if user visits /status end point:
            elif self.path == "/status":
                self.send_response(200)
                self.send_header("Content-type", "text/plain")
                self.end_headers()
                message = "OK"
                self.wfile.write(message.encode("utf-8"))
            else:
                 self.send_response(404)
                 self.send_header("Content-type", "text/plain")
                 self.end_headers()
                 message = "Endpoint not found"
                 self.wfile.write(message)
    
def run_server():
    HOST = "localhost"
    PORT = 8000
    server_address = (HOST, PORT)
    server = HTTPServer(server_address, Handler)

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
        server.server_close()

if __name__ == '__main__':
    run_server()