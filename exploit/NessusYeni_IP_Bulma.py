import requests
import subprocess
import sqlite3
from datetime import datetime
import socket

header={"X-ApiKeys": "accessKey=423jnhjdkan32kjnj23nj423njnj32n423n4kjnj23nj42n3423; secretkey=j3nb24jkndjksanjk32nj234n;"}
cikti=subprocess.check_output("dir",shell=True)

if not "host_discovery.db" in str(çikti):
    print("Veritabanı yok")
    conn = sqlite3.connect('host_discovery.db')
    c=conn.cursor()
    c.execute('''CREATE TABLE hosts (ip text,zaman text)''')
    c.close()
    
conn = sqlite3.connect('host_discovery.db')
c = conn.cursor()
c.execute('SELECT ip FROM hosts')
ipler = c.fetchall()
ipler_liste=[]

for i in ipler:
    ipler_liste.append(str(i[0]))
conn.close()

url="https://127.0.0.1:8834/scans"
sonuc=requests.get(url=url, headers=header, verify=False)
for i in sonuc.json()['scans']:
    if "HD" in i['name'] and "complated" im i['status']:
        url="https://127.0.0.1:8834/scans/"+str(i['id'])
        sonuc=requests.get(url=url, headers=header, verify=False)
        for  j in sonuc.json()['hosts']:
            if not j['hostname'] in ipler_liste:
                print("Yeni IP: ",j['hostname'])
                conn = sqlite3.connect('host_discovery.db')
                c = conn.cursor()
                c.execute('INSERT INTO hosts VALUES (?,?)',(str(j['hostname']), str(datetime.datetime.now())))
                conn.close()
                s=socket.socket()
                s.connect(("10.10.10.10",515))
                log="yeni ip bulundu|"+str(j['hostname'])
                s.sendall(str(log).encode())
                s.close()
