#!/usr/bin/env python3
from http.server import HTTPServer, BaseHTTPRequestHandler
from socketserver import ThreadingMixIn
import threading
import urllib
import json


class APIHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        message_parts = dict()
        message_parts['client_address'] = self.client_address
        message_parts['address_string'] = self.address_string()
        message_parts['command'] = self.command
        message_parts['path'] = self.path
        message_parts['realpath'] = parsed_path.path
        message_parts['query'] = parsed_path.query
        message_parts['request_version'] = self.request_version
        message_parts['server_version'] = self.server_version
        message_parts['sys_version'] = self.sys_version
        message_parts['protocol_version'] = self.protocol_version
        message_parts['thread_executed'] = threading.currentThread().getName()
        for name, value in sorted(self.headers.items()):
            message_parts[name] = value.rstrip()
        message = json.dumps(message_parts, indent=4)
        self.send_response(200)
        self.send_header('Content-Type',
                         'application/json; charset=utf-8')
        self.end_headers()
        self.wfile.write(message.encode('utf-8'))


class API_HTTPServer(ThreadingMixIn, HTTPServer):
    """ Mixing threads to improve """


def serve(address):
    print("Serving address:" + str(address))
    server = API_HTTPServer(address, APIHandler)
    server.serve_forever()


def main():
    serve(("0.0.0.0", 8080))


main()
