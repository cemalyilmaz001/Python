#!/usr/bin/python3
from scapy.all import *
import logging
import traceback
import sqlite3
import subprocess

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def drop_packet(source_ip):
    # İptables komutunu oluşturun
    iptables_cmd = f"sudo iptables -A INPUT -s {source_ip} -j DROP;sudo iptables-save"
    
    # Komutu çalıştırın
    subprocess.run(iptables_cmd, shell=True)

def paket_kayit(alarm,src,dst):
    drop_packet(str(src))

    # Veritabanı bağlantısını oluştur
    conn = sqlite3.connect('makina.db3')

    # Veriyi veritabanına kaydet
    try:
        conn.execute("INSERT INTO paket_analiz (alarm, src, dst) VALUES (?, ?, ?)", (alarm, src, dst))
        conn.commit()
    except sqlite3.IntegrityError:
        logging.exception("Hata mesajı:")
        traceback.print_exc()

    # Veritabanı bağlantısını kapat
    conn.close()

def alarm_paketini_yakala(paket):    
    try:
        # Alarm durumunu belirleyen bir koşul oluşturun
        if paket.haslayer(TCP):
            # TCP paketlerini yakala ve istediğiniz koşulu kontrol et
            if paket[TCP].flags == "F":
                src = paket[IP].src
                dst = paket[IP].dst
                paket_kayit("FIN bayrağı tespit edildi!",src,dst)
                print("ALARM: FIN bayrağı tespit edildi!")
                return None

            elif paket[TCP].flags & 0x0F != 0x02:  # Zararlı bir tarama olarak kabul edilebilecek TCP bayrakları
                src = paket[IP].src
                dst = paket[IP].dst
                paket_kayit("Zararlı TCP taraması tespit edildi!",src,dst)
                print("ALARM: Zararlı TCP taraması tespit edildi!")
                print("Kaynak IP: ",src)
                print("Hedef IP: ", dst)
                return None

        elif paket.haslayer(ARP):
            # ARP paketlerini yakala ve istediğiniz koşulu kontrol et
            if paket[ARP].op == 1:  # ARP isteği
                src = paket[IP].src
                dst = paket[IP].dst
                paket_kayit("ARP isteği tespit edildi!",src,dst)
                print("ALARM: ARP isteği tespit edildi!")
                return None
        elif paket.haslayer(TCP) and paket.getlayer(TCP).flags == "SA":
            # SYN-ACK (TCP ACK + TCP SYN) bayrağı tespit edildiğinde alarmı bas
            src = paket[IP].src
            dst = paket[IP].dst
            paket_kayit("Port taraması tespit edildi!",src,dst)
            print("ALARM: Port taraması tespit edildi!")
            print("Kaynak IP: ", src)
            print("Hedef IP: ", dst)
            print("Hedef Port: ", paket[TCP].dport)
        elif paket.haslayer(ICMP) and paket.getlayer(ICMP).type == 8:
            # ICMP Echo Request (Ping) paketi tespit edildiğinde alarmı bas
            src = paket[IP].src
            dst = paket[IP].dst
            paket_kayit("Ping taraması tespit edildi!",src,dst)
            print("ALARM: Ping taraması tespit edildi!")
            print("Kaynak IP: ", src)
            print("Hedef IP: ", dst)
            return None
        elif paket.haslayer(IP):
            if paket[IP].flags == 0x02:  # Zararlı bir tarama olarak kabul edilebilecek IP bayrakları
                src = paket[IP].src
                dst = paket[IP].dst
                paket_kayit("Zararlı IP taraması tespit edildi!",src,dst)
                print("ALARM: Zararlı IP taraması tespit edildi!")
                print("Kaynak IP: ", src)
                print("Hedef IP: ", dst)
                return None

        elif paket.haslayer(UDP):
            udp = paket[UDP]
            src = paket[IP].src
            dst = paket[IP].dst
            paket_kayit("Zararlı UDP taraması tespit edildi!",src,dst)
            print("ALARM: Zararlı UDP taraması tespit edildi!")
            print("Kaynak IP: ", src)
            print("Hedef IP: ", dst)
            return None

    except BaseException as a:
        logging.exception("Hata mesajı:")
        traceback.print_exc()

# Sniffer'ı başlat
sniff(prn=alarm_paketini_yakala, filter="ip or tcp or arp or udp", store=0)
