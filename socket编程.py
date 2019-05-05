# chatserver

import logging
import socket
import threading
import datetime


logging.basicConfig(level=logging.INFO,format='%(asctime)s %(thread)d %(message)s')


class ChatServer:
    def __init__(self,ip='127.0.0.1',port=9999):
        self.sock = socket.socket()
        self.addr = (ip,port)
        self.clients = {}
        self.event = threading.Event()

    def start(self):
        self.sock.bind(self.addr)
        self.sock.listen()
#         accept会阻塞主线程，所以开一个新线程
        threading.Thread(target=self.accept).start()

    def accept(self):
        while not self.event.is_set():
            sock,client = self.sock.accept()

            self.clients[client] = sock
            threading.Thread(target=self.recv,args=(sock,client),name='recv').start()

    def recv(self,sock,client):
        while not self.event.is_set():
            try:
                data = sock.recv(1024)
            except Exception as e:
                logging.error(e)
                data = 'quit'
            msg = data.decode().strip()
            if msg == 'quit':
                self.clients.pop(client)
                sock.close()
                logging.info('{}quits'.format(client))
                break
            msg = '{:%Y/%m/%d %H:%M:%S}{}:{}\n{}\n'.format(datetime.datetime.now(),*client,data.decode())
            logging.info(msg)
            msg = msg.encode()
            for s in self.clients.values():
                s.send(msg)


    def stop(self):
        for s in self.clients.values():
            s.close()
        self.sock.close()
        self.event.set()


def main():
    cs = ChatServer()
    cs.start()
    while True:
        cmd = input('>>').strip()
        if cmd == 'quit':
            cs.stop()
            threading.Event().wait(3)
            break
        logging.info(threading.enumerate())


if __name__ == "__main__":
    main()









