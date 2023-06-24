from scapy.all import *
import logging
import traceback

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def alarm_paketini_yakala(paket):    
    try:
        # Alarm durumunu belirleyen bir koşul oluşturun
        if paket.haslayer(TCP):
            # TCP paketlerini yakala ve istediğiniz koşulu kontrol et
            if paket[TCP].flags == "F":
                print("ALARM: FIN bayrağı tespit edildi!")
            elif paket[TCP].flags & 0x0F != 0x02:  # Zararlı bir tarama olarak kabul edilebilecek TCP bayrakları
                print("ALARM: Zararlı TCP taraması tespit edildi!")
                print("Kaynak IP: ", paket[IP].src)
                print("Hedef IP: ", paket[IP].dst)
        elif paket.haslayer(ARP):
            # ARP paketlerini yakala ve istediğiniz koşulu kontrol et
            if paket[ARP].op == 1:  # ARP isteği
                print("ALARM: ARP isteği tespit edildi!")
        elif paket.haslayer(TCP) and paket.getlayer(TCP).flags == "SA":
            # SYN-ACK (TCP ACK + TCP SYN) bayrağı tespit edildiğinde alarmı bas
            print("ALARM: Port taraması tespit edildi!")
            print("Kaynak IP: ", paket[IP].src)
            print("Hedef IP: ", paket[IP].dst)
            print("Hedef Port: ", paket[TCP].dport)
        elif paket.haslayer(ICMP) and paket.getlayer(ICMP).type == 8:
            # ICMP Echo Request (Ping) paketi tespit edildiğinde alarmı bas
            print("ALARM: Ping taraması tespit edildi!")
            print("Kaynak IP: ", paket[IP].src)
            print("Hedef IP: ", paket[IP].dst)
        elif paket.haslayer(IP):
            if paket[IP].flags == 0x02:  # Zararlı bir tarama olarak kabul edilebilecek IP bayrakları
                print("ALARM: Zararlı IP taraması tespit edildi!")
                print("Kaynak IP: ", paket[IP].src)
                print("Hedef IP: ", paket[IP].dst)
        elif paket.haslayer(UDP):
            udp = paket[UDP]
            print("ALARM: Zararlı UDP taraması tespit edildi!")
            print("Kaynak IP: ", paket[IP].src)
            print("Hedef IP: ", paket[IP].dst)
    except BaseException as a:
        logging.exception("Hata mesajı:")
        traceback.print_exc()

# Sniffer'ı başlat
sniff(prn=alarm_paketini_yakala, filter="ip or tcp or arp or udp", store=0)
