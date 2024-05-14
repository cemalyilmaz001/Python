#!/usr/bin/python3
import socket
import subprocess

#
# Socket Örnekleri
# 
class Server():
    def __init__(self):
        super().__init__()
        self.host = "127.0.0.1"
        self.port = 50001
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def demo_socket_stop(self):
        self.server_socket.close()
    
    def run_socket_server(self):
        self.server_socket.bind((self.host,self.port))
        self.server_socket.listen()
        conn, addr = self.server_socket.accept()
        print("Connect from: " + str(addr))
        while True:
            data = conn.recv(1024).decode()
            print(data)
            result = subprocess.run(data, stdout=subprocess.PIPE, shell=True)
            if (result.stdout.decode() != ""):
                response_data = result.stdout
            else:
                response_data = ("command execute").encode()
            conn.send(response_data)
        self.demo_socket_stop()

if __name__ == "__main__":
    soc = Server()
    soc.run_socket_server()
