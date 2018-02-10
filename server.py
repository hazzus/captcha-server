from http.server import BaseHTTPRequestHandler, HTTPServer
import time
from captcha import *
import os


class HttpProcessor(BaseHTTPRequestHandler):
    __request_time = {}
    __captcha_codes = {}

    def do_GET(self):
        client = self.client_address[0]
        self.__request_time[client] = time.time()
        new_captcha = captcha()
        file = 'captcha' + str(client) + '.png'
        new_captcha.get_image().save(file)
        self.__captcha_codes[client] = new_captcha.get_code()
        self.send_response(200)
        self.send_header('content-type', 'image/png')
        self.end_headers()
        self.wfile.write(self.load_binary(file))
        os.remove(file)

    def do_POST(self):
        income_time = time.time()
        client = self.client_address[0]
        if (income_time - self.__request_time[client]) > 1:
            self.send_response(408)
            self.send_header('content-type', 'text/html')
            self.end_headers()
            self.wfile.write('Out of time'.encode())
        else:
            client_code = self.rfile.read(len(self.__captcha_codes[client])).decode()
            print('Client insert: ' + client_code)
            print('Expected: ' + self.__captcha_codes[client])
            self.send_response(200)
            if client_code != self.__captcha_codes[client]:
                self.send_header('content-type', 'text/html')
                self.end_headers()
                self.wfile.write('Bad captcha'.encode())
            else:
                self.send_header('content-type', 'text/html')
                self.end_headers()
                self.wfile.write('Good, access granted'.encode())

    @staticmethod
    def load_binary(file):
        with open(file, 'rb') as file:
            return file.read()


serv = HTTPServer(('localhost', 8080), HttpProcessor)
serv.serve_forever()
