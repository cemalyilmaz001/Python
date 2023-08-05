#!/usr/bin/python3
from scapy.all import *
import logging
import traceback
import sqlite3
import datetime

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def paket_kayit(alarm,kaynak,hedef):
    # Veritabanı bağlantısını oluştur
    conn  = sqlite3.connect('makina.db3')
    tarih = datetime.datetime.now()
    saat = datetime.datetime.now().hour
    dakika = datetime.datetime.now().minute
    saniye = datetime.datetime.now().second
    trh = str(tarih.day) + "/" + str(tarih.month) + "/" + str(tarih.year)
    st = str(saat) + ":" + str(dakika) + ":" + str(saniye)
    # Veriyi veritabanına kaydet
    try:
        conn.execute('''CREATE TABLE IF NOT EXISTS paket_analiz (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                alarm TEXT NOT NULL,
                kaynak TEXT NOT NULL,
                hedef TEXT NOT NULL,
                tarih TEXT NOT NULL,
                saat TEXT NOT NULL)''')

        conn.execute("INSERT INTO paket_analiz (alarm, kaynak, hedef,tarih,saat) VALUES (?, ?, ?, ?, ?)", (alarm, kaynak, hedef,trh,st))
        conn.commit()
    except sqlite3.IntegrityError:
        logging.exception("Hata mesajı:")
        traceback.print_exc()

    # Veritabanı bağlantısını kapat
    conn.close()

def network_paketini_yakala(paket):    
    try:
        # ARP Paketlerinin Tespiti
        if paket.haslayer(Ether):
            if paket.haslayer(ARP) and paket[ARP].op == 2:  
                if paket[ARP].hwdst != paket[Ether].src:  
                    paket_kayit("ARP spoofing tespit edildi!", paket[Ether].src, paket[Ether].dst)
                    print("ALARM: Zararlı ARP spoofing tespit edildi!")
                    return

        # Port Tarama Tespit
        if paket.haslayer(TCP) and paket[TCP].flags == 2:
            if str(paket[TCP].dport) != "443":
                print("ALARM: Port taraması tespit edildi! Kaynak IP:", paket[IP].src, "Hedef:", paket[IP].dst)
                paket_kayit(f"Port taraması tespit edildi! --> Port: {str(paket[TCP].dport)}",paket[IP].src, paket[IP].dst)
                os.system(f"sudo iptables -A INPUT -p tcp --dport {str(paket[TCP].dport)} -j DROP;sudo iptables-save")

        # Ping Tarama Tespit
        if paket.haslayer(ICMP) and paket.getlayer(ICMP).type == 8:
            print("ALARM: Ping taraması tespit edildi! Kaynak IP: " + paket[IP].src + " Hedef IP: " + paket[IP].dst)
            paket_kayit("Ping taraması tespit edildi!",paket[IP].src,paket[IP].dst)

        if paket.haslayer(TCP) and paket.haslayer(Raw):
            if paket[TCP].dport == 80 or paket[TCP].sport == 80:  # HTTP trafiği
                http_payload = paket[Raw].load.decode(errors='ignore')
                if "pwd" in http_payload:
                    print("ALARM: Zararlı HTTP isteği tespit edildi!")

            # Zararlı ağ hareketlerini tespit etme işlemleri burada yapılır
            if paket.haslayer(TCP):
                # TCP paketleri üzerinde analiz yapabilirsiniz
                if paket[TCP].flags == "FPU":
                    print("ALARM: Zararlı TCP hareketi tespit edildi!")
                    


    except BaseException as a:
        logging.exception("Hata mesajı:")
        traceback.print_exc()


# Sniffer'ı başlat  
sniff(prn=network_paketini_yakala, filter="ip or tcp or arp or udp", store=0)
