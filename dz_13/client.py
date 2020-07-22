import socket

import json

import threading

from time import sleep


CONNECTION = ('127.0.0.1', 80)

socket_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0) # TCP,      UDP - SOCK_DGRAM
connection = socket_.connect(CONNECTION)
name = None

def to_json_and_add_end(json_data):
    return json.dumps(json_data) + '<end>'

def from_json_del_end(json_data):
    return json.loads(json_data[:-5])

while True:
    recv = from_json_del_end(socket_.recv(2048).decode())
    print(f'\r{recv}')
    
    if recv['message'].startswith('Welcome to chat'):
        break
    elif recv['message'].startswith(f'Name'):
        name = None
    
    if not name:
        while not name:
            print(f'Your name: ', end='')
            name = input()
            if name:
                break
        data = {'name': name, 'message': ''}
        socket_.send(to_json_and_add_end(data).encode(encoding='ascii'))


def wait_for_message():
    while True:
        message = input().strip()
        json_info = {
            "name": name,
            "message": ' '.join(message[5:].split()[1:]) if message.startswith('user:') else message,
            "to": message[5:].split()[0] if message.startswith('user:') else ''
        }
        socket_.send(to_json_and_add_end(json_info).encode(encoding='ascii'))

thread = threading.Thread(target=wait_for_message, daemon=True)
thread.start()
while True:
    recv = from_json_del_end(socket_.recv(2048).decode())
    print(f'\r{recv}\nYour message: ', end='')
    

socket_.close()