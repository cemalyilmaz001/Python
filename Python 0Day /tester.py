#!/usr/bin/python3

from curses import raw
from scapy.all import *
import sqlite3

# SQLite veritabanına bağlanın veya oluşturun
conn = sqlite3.connect('captured_packets.db')
cursor = conn.cursor()

# Tablo oluşturun (eğer daha önce oluşturulmadıysa)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS packets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        kaynak_ip TEXT,
        hedef_ip TEXT,
        packet_data TEXT
    )
''')
conn.commit()

def paket_kayit(kaynak_ip="None",hedef_ip="None",packet_data="None"):
    # Yakalanan paketi veritabanına ekleyin
    cursor.execute('''
        INSERT INTO packets (kaynak_ip, hedef_ip, packet_data)
        VALUES (?, ?, ?)
    ''', (kaynak_ip, hedef_ip, packet_data))
    conn.commit()

# Gelen paketleri yakalamak ve veritabanına eklemek için bir fonksiyon tanımlayın
def packet_callback(packet):
    if packet.haslayer(IP):
        kaynak_ip       = packet[IP].src 
        hedef_ip        = packet[IP].dst
        packet_data = packet.show(dump=True)  # Paketin detaylarını alın (döküm olarak)
        packet_data = packet_data.replace("'", "''")  # Tek tırnakları kaçının

    paket_kayit(str(kaynak_ip),str(hedef_ip),packet_data)
    

# Yakalamayı başlatın
sniff(filter="ip", prn=packet_callback)
