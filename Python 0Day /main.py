#!/usr/bin/python3
from scapy.all import *
import logging
import traceback
import sqlite3
import subprocess

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def drop_packet(source_ip):
    iptables_cmd = f"sudo iptables -A INPUT -s {source_ip} -j DROP;sudo iptables-save"
    subprocess.run(iptables_cmd, shell=True)

def paket_kayit(alarm,kaynak,hedef):
    # Veritabanı bağlantısını oluştur
    conn = sqlite3.connect('makina.db3')

    # Veriyi veritabanına kaydet
    try:
        conn.execute("INSERT INTO paket_analiz (alarm, kaynak, hedef) VALUES (?, ?, ?)", (alarm, kaynak, hedef))
        conn.commit()
    except sqlite3.IntegrityError:
        logging.exception("Hata mesajı:")
        traceback.print_exc()

    # Veritabanı bağlantısını kapat
    conn.close()

def alarm_paketini_yakala(paket):    
    try:
        # ARP Paketlerinin Tespiti
        if paket.haslayer(ARP):
            if paket[ARP].op == 1:  # ARP isteği
                paket_kayit("ARP isteği tespit edildi!",paket[IP].src,paket[IP].dst)
                print("ALARM: ARP isteği tespit edildi!")

        # Port Tarama Tespit
        elif paket.haslayer(TCP) and paket[TCP].flags == 2:  
            print("ALARM: Port taraması tespit edildi! Kaynak IP:", paket[IP].src, "Hedef Port:", paket[TCP].dport)
            paket_kayit(f"Port taraması tespit edildi! --> Port: {str(paket[TCP].dport)}",paket[IP].src, paket[IP].dst)

        # Ping Tarama Tespit
        elif paket.haslayer(ICMP) and paket.getlayer(ICMP).type == 8:
            paket_kayit("Ping taraması tespit edildi!",paket[IP].src,paket[IP].dst)
            print("ALARM: Ping taraması tespit edildi! Kaynak IP: " + paket[IP].src + " Hedef IP: " + paket[IP].dst)
    except BaseException as a:
        pass
        #logging.exception("Hata mesajı:")
        #traceback.print_exc()

# Sniffer'ı başlat
sniff(prn=alarm_paketini_yakala, filter="ip or tcp or arp or udp", store=0)
