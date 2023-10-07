import socket
import time
from pyfiglet import Figlet
from CONFIG import *

def main():
    print('Creating server...')
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)

    server.bind((HOST, PORT))
    server.setblocking(0)
    server.listen(1)

    global user 
    user = None
    print(f'Server is ready! {server.getsockname()}')
    while True:

        try: 
            user, adress = server.accept()
            user.setblocking(0)
            print('User connected: '+str(adress[0]))
        except:
            pass

        if user != None:
            command = input('cmd > ')
            try:
                user.send(command.encode())
            except:
                print('Something went wrong...')
                user = None

        time.sleep(0.01)

if __name__ == '__main__':
    print(Figlet(font='speed').renderText('CMDRunner'))
    main()