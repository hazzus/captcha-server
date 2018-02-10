from http.server import BaseHTTPRequestHandler, HTTPServer
import time
from captcha import *


class HttpProcessor(BaseHTTPRequestHandler):
    __request_time = {}
    __captcha_codes = {}

    def do_GET(self):
        client = self.client_address[0]
        self.__request_time[client] = time.time()
        new_captcha = captcha()
        self.__captcha_codes[client] = new_captcha.get_code()
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        self.wfile.write(self.__captcha_codes[client].encode())

    def do_POST(self):
        income_time = time.time()
        client = self.client_address[0]
        if (income_time - self.__request_time[client]) > 100000:
            self.send_response(408)
        else:
            client_code = self.rfile.read(len(self.__captcha_codes[client]))
            print('Client insert: ' + client_code.decode())
            print('Expected: ' + self.__captcha_codes[client])
            self.send_response(200)
            if client_code != self.__captcha_codes[client]:
                self.send_header('content-type', 'text/html')
                self.end_headers()
                self.wfile.write('Bad captcha'.encode('UTF-8'))
            else:
                self.send_header('content-type', 'text/html')
                self.end_headers()
                self.wfile.write('Good, access granted')


serv = HTTPServer(('localhost', 8080), HttpProcessor)
serv.serve_forever()
