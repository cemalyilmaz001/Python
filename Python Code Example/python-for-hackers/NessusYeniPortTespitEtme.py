import requests
import subprocess
import datetime
import sqlite3

çikti=subprocess.check_output("ls",shell=True)
if not "port.db" in str(çikti):
    conn = sqlite3.connect("port.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE portlar (port text, ip text, zaman text)''')
    c.close()

header={"X-ApiKeys": "accessKey=423jnhjdkan32kjnj23nj423njnj32n423n4kjnj23nj42n3423; secretkey=j3nb24jkndjksanjk32nj234n;"}
url="https://127.0.0.1:8834/scans"
sonuc=requests.get(url=url,headers=header,verify=False)

for i in sonuc.json()['scans']:
    scan_id=i['id']
    url="https://127.0.0.1:8834/scans"+str(scan_id)
    tarama = requests.get(url=url, headers=header, verify=False)
    for j in tarama.json()['scans']:
        try:
            host_id=j['host_id']
            url="https://127.0.0.1:8834/scans"+str(scan_id)+"/hosts/"+str(host_id)+"/plugings/11219"
            IP=requests.get(url=url, headers=header, verify=False)
            for k in IP.json()['outputs']:
                port=list(k['ports'].keys())[0]
                IP=j['hostname']
                conn = sqlite3.connect("port.db")
                c = conn.cursor()
                çikti=c.execute('select * from portlar where port=? and ip=?', (port,IP))
                port_sayisi=len(çikti.fetchall())
                conn.close()
                if port_sayisi<1:
                    print("Yeni port: ", port," IP:",IP)
                    conn=sqlite3.connect('port.db')
                    c = conn.cursor()
                    c.execute('INSERT INTO portlar VALUES (?,?,?)',(port,IP,str(datetime.datetime.now())))
                    conn.commit()
                    conn.close()
        except:
            pass
