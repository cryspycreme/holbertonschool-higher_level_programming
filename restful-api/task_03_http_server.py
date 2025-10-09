#!/usr/bin/python3

from http.server import HTTPServer, BaseHTTPRequestHandler
import json

HOST = "localhost"
PORT = 8000

# define subclass that extends from BaseHTTPRequestHandler
class Handler(BaseHTTPRequestHandler):
    # define custom method to handle how we respond to GET requests
    def do_GET(self):
        # if user visits /data end point, return JSON:
            if self.path == "/data":
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
                status = "OK"
                json_status = json.dumps(status).encode("utf-8")
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(json_status)
        # user visits root (/) endpoint
            elif self.path == "/":
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write("Hello, this is a simple API!".encode("utf-8"))
            else:
                 json_error = json.dumps("Error 404: Not Found").encode("utf-8")
                 self.send_response(404)
                 self.send_header("Content-type", "text/html")
                 self.end_headers()
                 self.wfile.write(json_error.encode("utf-8"))
            
server = HTTPServer((HOST, PORT), Handler)
server.serve_forever()
