from scapy.all import *

interfaceWlan = "wlan0"
interfaceEth0 = 'eth0'
filter = 'tcp port 80'
filter_icmp = "icmp"

def packet_callback(packet):
    print(packet.show())

def sniff_ICMP(packet):
    if packet[ICMP]:
        print("ICMP Paketi Yakalandı: {0}".format(packet[ICMP].summary()))

sniff(filter=filter, iface=interfaceEth0, prn=packet_callback)
#sniff(filter=filter_icmp, iface=interfaceW, prn=sniff_ICMP)
