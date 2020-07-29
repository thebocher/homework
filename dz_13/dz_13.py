import socketserver

import json

from dz_logger import get_dz_logger

import logging



HTTP_PORT = 80

LOCALHOST = '127.0.0.1'
IP_ROUTER = '192.168.0.1' # 192.168.1.1

IP_HOST= '185.189.185.50'


# LOGGING_LEVEL = logging.DEBUG

# logging.basicConfig(level=LOGGING_LEVEL)

# dz_fmt = logging.Formatter(fmt='%(asctime)s - %(name)s - %(message)s')

# dz_handler = logging.Handler()
# dz_handler.setFormatter(dz_fmt)

# dz_logger = logging.getLogger('dz_13')
# dz_logger.addHandler(dz_handler)
# dz_logger.propagate = False

# dz_logger.debug('debug')

class ChatTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

class ChatRequestHandler(socketserver.StreamRequestHandler):
    users = {}

    def setup(self):
        user_name = None
        while True:
            if not user_name:
                json_data = {
                    'name': 'Server',
                    'message': 'Need to introduce yourself'
                }
                print('<server to client>:', self.to_json_and_add_end(json_data))
                self.request.send(self.to_json_and_add_end(json_data).encode(encoding='ascii'))

            user = self.from_json_del_end(self.request.recv(2048).decode())
            user_name = user['name']
            print('<client to server>:', self.to_json_and_add_end(user))

            if user_name in self.users:
                json_data = {
                    'name': 'Server',
                    'message': f'Name \'{user_name}\' is already taken. Choose another name.'
                }
                print('<server to client>:', self.to_json_and_add_end(json_data))
                self.request.send(self.to_json_and_add_end(json_data).encode(encoding='ascii'))
            else:
                json_data = {
                    'name': 'Server',
                    'message': f'Welcome to chat, {user_name}'
                }
                print('<server to client>:', self.to_json_and_add_end(json_data))
                self.request.send(self.to_json_and_add_end(json_data).encode(encoding='ascii'))
                self.users[user_name] = self.request
                break

    def handle(self):
        while True:                 # {"name": "Joe", "message": "hello", "to": "everyone"}<end>:
            user = self.request.recv(2048).decode()
            print('<client to server>:', user)
            user = self.from_json_del_end(user)

            if user['to']:
                print(f'<server to client {user["to"]}>:', self.to_json_and_add_end(user))
                self.server_to_client_private(user)
            elif not user['to']:
                self.server_to_all_clients(user)
            

    def server_to_client(self, data, *, client=None):
        if client:
            client.send(self.to_json_and_add_end(data).encode(encoding='ascii'))
        else:
            self.request.send(self.to_json_and_add_end(data).encode(encoding='ascii'))

    def server_to_all_clients(self, data):
        print(f'<server to all clients>:', self.to_json_and_add_end(data))
        for client in self.users:
            self.server_to_client(data, client=self.users[client])

    def server_to_client_private(self, user):
        to_user = user.get('to')
        private_message = {'name': user['name'], 'message': user['message']}
        client = self.users.get(to_user)
        self.server_to_client(private_message, client=client)

    def to_json_and_add_end(self, json_data):
        return json.dumps(json_data) + '<end>'
    
    def from_json_del_end(self, json_data):
        return json.loads(json_data[:-5])
    
    def finish(self):
        user_name = self.find_user(self.request)
        self.users.pop(user_name)

    def find_user(self, req):
        for key in self.users:
            if self.users[key] == req:
                return key
        return None
    

with ChatTCPServer((LOCALHOST, HTTP_PORT), ChatRequestHandler) as server:
    server.serve_forever()