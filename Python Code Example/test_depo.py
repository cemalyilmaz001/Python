#!/usr/bin/python3

# sudo watch -n 2 "tcpdump -nnn -t -c 200 | cut -f 1,2,3,4 -d '.' | sort | uniq -c | sort -nr | head -n 20 | grep  'IP' >> abc.txt"

from subprocess import Popen, PIPE
import datetime
import requests
import os
import sys
from time import sleep
import sqlite3
from cryptography.fernet import Fernet
import sqlite3
import os
from sqlite3 import OperationalError
from bs4 import BeautifulSoup
import curses
import psutil
import time
import requests
import re


class _aksipi_():
    def __init__(self):
        self.pwd      = os.getcwd() + '/'
        self.usom     = 'https://www.usom.gov.tr/url-list.txt'
        self.gün      = datetime.datetime.now().day
        self.ay       = datetime.datetime.now().month
        self.yıl      = datetime.datetime.now().year

        self.db       = sqlite3.connect(f'{str(self.pwd)}genel/data.db3')
        self.dbm      = self.db.cursor()

        self.tarih = self.dbm.execute(f"""SELECT * FROM tarih""")
        self.record = self.tarih.fetchall()
        
        for row in self.record:
            if int(self.gün) != int(row[0]):
                self.dbm.execute("DELETE FROM tarih WHERE gün = ?",(f'{int(row[0])}',))
                self.db.commit()
                self.dbm.execute(f"""INSERT INTO tarih VALUES ("{int(self.gün)}", "{int(self.ay)}", "{int(self.yıl)}")""")
                os.system(f'echo " " > {str(self.pwd)}genel/abc.txt')
                self.response = requests.get(f'{self.usom}',verify=False)
                self.dsy      = open(f'{str(self.pwd)}genel/usom.txt','w')
                self.dsy.write(str(self.response.content))
                self.dsy.close()
            
            self.db.commit()
        
        self.usomcheck = open(f'{str(self.pwd)}genel/usom.txt','r')
        self.usomicrk  = self.usomcheck.read()
        self.usomcheck.close()
        self.dosya    = open(f'{str(self.pwd)}genel/abc.txt','r')
        self.icerik   = self.dosya.read()
        self.dosya.close()

    def Usom_IP_Check(self,url):
        if str(url) in self.usomicrk:
            Popen(['xterm', '-e', f'echo "\nİP ADRES: \t{str(url)}";echo "\n\nUSOM İP KONTROL: ZARARLI";\n\necho " ";sleep 1000;'], stdin=PIPE)
            return "İP ADRESİ ZARARLI !"
        else:
            return "İP ADRESİ TEMİZ :)"

    def Main(self):
        for i in self.icerik.split("\n"): 
            try:
                t = 0 
                data = i.split()

                self.dbm.execute(f"""SELECT * FROM yıldız WHERE ip = '{str(data[2])}'""")
                if self.dbm.fetchall():
                    t += 1
                
                if t == 0:
                    self.dbm.execute(f"""INSERT INTO yıldız VALUES ("{str(data[2])}", "{self.Usom_IP_Check(str(data[2]))}")""")
            except BaseException:
                pass
        
        self.db.commit()
        self.db.close()

class Demo():
    def __init__(self):
        self.cwd = os.getcwd() + "/"

    def keys(self):
        # Rastgele anahtar oluşturma
        key = Fernet.generate_key()
        # Veritabanına bağlanma
        conn = sqlite3.connect(f'{self.cwd}veritabani.db3')
        # Bir cursor oluşturma
        cursor = conn.cursor()
        # Keys değerini veritabanına ekleme
        cursor.execute("INSERT INTO secret (keys) VALUES (?)", (f'{str(key)}',))
        # Bağlantıyı kaydetme ve kapatma
        conn.commit()
        conn.close()

    def hava(self):
        # Hava Durumu
        mgm = "https://www.mgm.gov.tr/tahmin/gunluk-tahmin.aspx"  
        response = requests.get(mgm)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            tablo = soup.find_all("h4")
            t = 0
            data = []
            for row in tablo:
                t += 1
                if t == 3:
                    data.append(row.text.strip())

        d = ""
        b = "'"
    
    def linux(self):
        # CPU Kullanımı
        cpu_percent = psutil.cpu_percent(interval=1)
        # Bellek Kullanımı
        memory = psutil.virtual_memory()
        memory_percent = memory.percent
        # Disk Kullanımı
        disk = psutil.disk_usage("/")
        disk_percent = disk.percent
    
    def ekonomi(self):
        # Ekonomi Verileri
        url = "https://www.ekonomim.com/"
        response = requests.get(url)
        t = 0
        y = 0
        name = []
        vall = []
        tot  = []
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            
            for borsa in soup.find_all("span", {"class": "name"}):
                t += 1
                if t >= 6:
                    pass
                else:
                    name.append(borsa.text.strip())

            for valls in soup.find_all("span", {"class": "val"}):
                y += 1
                if y >= 6:
                    pass
                else:
                    vall.append(valls.text.strip())

            for b,v in zip(name,vall):
                d = f"{b}: {v}"
                tot.append(d)

    # {str(data).strip("[]").replace(b,d)} {os.getlogin()}  
    # CPU Usage (%): {cpu_percent}  Memory Usage (%): {memory_percent}  Disk Usage (%): {disk_percent} 
    # Uygulama UİD: {os.getuid()} - {os.getpid()} 
    # Ekonomi {str(tot).strip("[]").replace(b,d)}
     


if __name__ == "__main__":
    l = _aksipi_()
    l.Main()
    
