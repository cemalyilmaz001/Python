#!/usr/bin/python

import os, optparse, socket
from timeit import default_timer as timer
from datetime import timedelta
from colorama import Fore, Back, Style, init
from threading import *

class Scanner:
    def __init__(self):
        self.start = timer()
        init(autoreset=True)

    def PortScannerIslem(self, host,port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if sock.connect_ex((host,port)):
            print(Fore.RED +"[*]"+ Style.RESET_ALL + f" Port {port} Kapalı")
        else:
            print(Fore.YELLOW +"\n[*]"+ Style.RESET_ALL + f" Port {port} Açık")
        sock.close()            

    def PortScanner(self, host,port):
        for pt in port:
            t = Thread(target=self.PortScannerIslem, args=(host,int(pt)))
            t.start()

    def run(self):
        parser = optparse.OptionParser('Program Kullanımı: ' + '-H <HEDEF-HOST> -p <HEDEF-PORT>')
        parser.add_option('-H', dest='host', type='string', help='Hedef Host')
        parser.add_option('-p', dest='port', type='string', help='Hedef Port')
        (options, args) = parser.parse_args()
        host = options.host
        port = str(options.port).split(',')
        if (host == None) | (port == None):
            print(parser.usage)
            exit(0)
        self.PortScanner(host,port)

if __name__ == "__main__":
    q = Scanner()
    q.run()
