#!/usr/bin/python3

"""Sets up a local server and feeds specific pages.

    Home page ('/') prints 'Hello, this is a simple API!'
    /data page prints a name, age, and city
    /info page prints a version and description of the server
    /status prints 'ok' as the response is 200

    Any other page prints 'Endpoint not found',
    as they have indeed not been set up.
"""

import http.server
import json

PORT = 8000

dataDict = {"name": "John", "age": 30, "city": "New York"}
j_dict = json.dumps(dataDict)
infoDict = {"version": "1.0",
            "description": "A simple API built with http.server"}
j_info = json.dumps(infoDict)


class ServerClass(http.server.BaseHTTPRequestHandler):
    """Handles various urls within a server.

    This subclass handles the information returned by
    several URLs: index ('/'), /data, /info, /status,
    with any other page printing a message tied to the 404 status.
    """
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b'Hello, this is a simple API!')
        elif self.path == '/data':
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(bytes(j_dict, "utf-8"))
        elif self.path == '/status':
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b'OK')
        elif self.path == '/info':
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(bytes(j_info, "utf-8"))
        else:
            self.send_response(404)
            self.send_header("COntent-type", "text/plain")
            self.end_headers()
            self.wfile.write(b'Endpoint not found')


with http.server.HTTPServer(("", PORT), ServerClass) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
