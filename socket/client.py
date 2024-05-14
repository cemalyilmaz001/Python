#!/usr/bin/python3
import socket

#
# Socket Örnekleri
# 
class Client():
    def __init__(self):
        super().__init__()
        self.host = "127.0.0.1"
        self.port = 50001
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def demo_socket_start(self):
        self.client_socket.connect((self.host,self.port))
    
    def demo_socket_stop(self):
        self.client_socket.close()
    
    def run_socket(self):
        self.demo_socket_start()
        messagess = input(">> ")
        while messagess.lower().strip() != "quit":
            self.client_socket.send(messagess.encode())
            data = self.client_socket.recv(1024).decode()
            print("Dönen Response: " + str(data))
            messagess = input(">> ")
        self.demo_socket_stop()

if __name__ == "__main__":
    soc = Client()
    soc.run_socket()
