#!/usr/bin/python3

# sudo watch -n 2 "tcpdump -nnn -t -c 200 | cut -f 1,2,3,4 -d '.' | sort | uniq -c | sort -nr | head -n 20 | grep  'IP' >> abc.txt"

from subprocess import Popen, PIPE
import datetime
import requests
import os
import sys
from time import sleep
import sqlite3

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

if __name__ == "__main__":
    l = _aksipi_()
    l.Main()
    