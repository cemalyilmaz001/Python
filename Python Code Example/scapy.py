from scapy.all import *

interfaceWlan = "wlan0"
interfaceEth0 = 'eth0'

# Filtreleme kriterleri
filter = 'tcp port 80'
filter_criteria = "tcp and ip host 192.168.1.1"
filter_icmp = "icmp"

target_ip = "192.168.1.100" # Engellenecek hedef IP adresi

# Paket yakalama fonksiyonu
def packet_callback(packet):
    print(packet.show())

def sniff_ICMP(packet):
    if packet[ICMP]:
        print("ICMP Paketi Yakalandı: {0}".format(packet[ICMP].summary()))
        
def packet_capture(packet):
    if packet.haslayer(TCP) and packet.haslayer(IP) and packet[IP].src == '192.168.1.1':
        print(packet.summary())

def packet_callback(packet):
    # Paket içeriğini analiz etmek için callback fonksiyonu
    if packet[TCP].payload:
        command = packet[TCP].payload.decode("utf-8", errors="ignore").strip()
        # Komut içeriğinde tehlikeli kelime varsa paketi engelle
        if "rm -rf" in command:
            print(f"[!] Zararlı Komut Tespit Edildi: {command}")
            packet.drop()
            
def block_packet(packet):
    if packet.haslayer(IP) and packet[IP].dst == target_ip:
        print(f"[+] Engellenen paket: {packet.summary()}")
        return

# Ağ trafiğini dinlemek için sniff fonksiyonu kullanılır
sniff(filter="tcp", prn=packet_callback, store=0)
#sniff(filter="ip", prn=block_packet)
#sniff(prn=packet_capture, filter=filter_criteria)
#sniff(filter=filter, iface=interfaceEth0, prn=packet_callback)
#sniff(filter=filter_icmp, iface=interfaceW, prn=sniff_ICMP)
