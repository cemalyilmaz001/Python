#!/usr/bin/python3

import datetime
import requests
import os
import sys
import sqlite3
from cryptography.fernet import Fernet
from bs4 import BeautifulSoup
import time


class mains_():
    def __init__(self):
        self.cwd      = os.getcwd() + "/"

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

        for n in name:
            print(n)

        for v in vall:
            print(v)

        for t in tot:
            print(t)
     


if __name__ == "__main__":
    l = mains_()
    l.ekonomi()
    
