#!/usr/bin/python3

try:
	from googlesearch import search
	from colorama import Fore, Back, Style
	from urllib.parse import urlparse
	from bs4 import BeautifulSoup
	from fake_useragent import UserAgent
	import datetime
	import requests
	import colorama
	import os
	import sys
	import ipaddress
	import socket
	import whois
except ImportError:
	print("İndirme işlemleri devam etmekte ..")
 
colorama.init()

class ClassPentester(object):
	def __init__(self):
		super(ClassPentester, self).__init__()
		self.root = os.getcwd() + "/"
		os.chdir('../')
		self.root 			= os.getcwd() + "/"
		self.osint 			= self.root + 'SOMM/'
		self.usomTxt 		= self.root + "SODM/Depo/Data/usom.txt"
		self.dizin_sonuc    = self.root + "SODM/Depo/İnfo"
		self.dizin_home     = self.root + "SODM/Depo/Database/geckodriver"
		self.dizin_usom 	= self.root + "SODM/Depo/"
		self.dizin_info 	= self.root + "SODM/Depo/İnfo"


	def Decoration(self,output):
		print('\n', output), print('--' * 20)

	def UsomData(self):
		response = requests.get("https://www.usom.gov.tr/url-list.txt",verify=False)
		dosya = open("usom.txt","w")
		dosya.write(str(response.content))
		dosya.close()

	def Search(self,query="None"):
		if query == "None":
			query = input('Google Url Search: ')
		
		for j in search(query, tld="co.in", num=10, stop=200, pause=2):
			print(j)		

	def Get_ip(self,url):
		hostname = socket.gethostbyname(urlparse(url).hostname)
		print(Fore.GREEN)
		print('[*] {}'.format(hostname)) 
		print(Fore.WHITE)
		if hostname:
			return ipaddress.IPv4Address(hostname).is_private

	def Get_req(self,urls):
		private_ip = self.Get_ip(str(urls))
		if not private_ip:
			try:
				with requests.Session() as s:
					s.max_redirects = 5
					r = s.get(urls, timeout=5, stream=True)
				return {'url': urls, 'staus_code': r.status_code}
			except requests.exceptions.RequestException:
				return 'ERROR'
		return 'Private IP'

	def IpLocation(self,x):
		proxies = {
		    'http': 'socks5://127.0.0.1:9050',
		    'https': 'socks5://127.0.0.1:9050'
		}
		q = requests.get("https://ipinfo.io/"+x+"/json", proxies=proxies).json()
		for i in q:
			veri = q[i]
			i = i
			print(str(i) + ': ' + str(veri))
		#os.system(f"open https://www.google.com/maps/place/{str(q['loc'])}")

		
	def Remove_url_ends(self,url):
		final_url = url.split('//')[1].split('/')[0]
		return final_url

	def Remove_duplicates(self,arr):
		new_arr = []
		for i in arr:
			if i not in new_arr:
				new_arr.append(i)

		for i in range(len(new_arr)):
			print(f'[{i + 1}]', new_arr[i], sep='')

	def Get_url(self,parent_url):
		proxies = {
		    'http': 'socks5://127.0.0.1:9050',
		    'https': 'socks5://127.0.0.1:9050'
		}
		head = {"User-Agent" : UserAgent().random}
		re = requests.get(str(parent_url), headers=head, proxies=proxies)
		soup = BeautifulSoup(re.text, 'html.parser')
		return soup

	def Find_suburls(self,parent_url):
		url_list = []
		for link in self.Get_url(str(parent_url)).find_all('a'):
			try:
				if 'http' in link.get('href'):
					url_list.append(link.get('href'))
				else:
					# Step 3
					url_list.append(self.Remove_url_ends(parent_url) + link.get('href'))
			except:
				continue

		return url_list


	def Find_img(self,parent_url):
		self.Decoration('Images:')
		url_list = []
		for link in self.Get_url(parent_url).find_all('img'):
			url_list.append(link.get('src'))
		return self.Remove_duplicates(url_list)


	def Find_files(self,parent_url,suffix):
		self.Decoration('Files:')
		url_list = []
		for x in self.Find_suburls(parent_url):
			if suffix in x:
				print(x)
				url_list.append(x)

		if len(url_list) == 0:
			print("Couldn't find anything...")

	def All(self,query,search,ip):
		edit = str(query)
		edit = edit.split('//')
		url = str(edit[1]).split('/')
		os.system(f'cd {self.osint};./osint.py -link {str(query)}')
		os.system(f'cd {self.osint};./osint.py -dig {str(query)} ok')
		os.system(f'cd {self.osint};./osint.py -ip {str(query)}')
		os.system(f'cd {self.osint};./osint.py -search {str(search)}')
		os.system(f'cd {self.osint};./osint.py -lokasyon {str(ip)}')
		os.system(f'cd {self.osint};./osint.py -img {str(query)}')
		os.system(f'cd {self.osint};./osint.py -files {str(query)} .com')

	def Dig(self,url,sc):
		if sc == "mx":
			os.system(f"proxychains4 -q -f /etc/proxychains4.conf dig mx {url}")
		elif sc == "ns":
			os.system(f"proxychains4 -q -f /etc/proxychains4.conf dig ns {url}")
		elif sc == "ok":
			os.system(f"proxychains4 -q -f /etc/proxychains4.conf dig mx {url}")
			os.system(f"proxychains4 -q -f /etc/proxychains4.conf dig ns {url}")


def YardımMenüsü():
	os.system("figlet OSINT")
	print(f"""

	Osint 0.0.1
	-link         [https://x.com]         Site İçerisindeki Linkleri Getirir.
	-ip           [https://x.com]         İp Adresini Verir.
	-search       [anahtar kelimeler]     Url Adreslerinde Geçen Kelimeleri Getirir.
	-lokasyon     [81.212.2.47]           Bölge hakkında Bilgi Verir.
	-img          [https://x.com]         Sitedeki Resim Url Adreslerini Getirir.
	-files        [https://x.com] [.txt]  Sitede Bulunan Her Türlü Dosya Formatını Getirebilir.
	-dig          [x.com]  [ns-mx]        Mail ve DNS Kayıtlarını Getirir.

	./osint.py -all https://x.com/ aranacak-kelimeler 231231312

	-h, -help: help""")


try:
	if __name__ == "__main__":
		try:
			query1 = sys.argv[-1]
			query2 = sys.argv[2]
			query3 = sys.argv[3]
		except Exception:
			pass
		if str(query1) == "-help" or str(query1) == "-h":
			YardımMenüsü()
		c = ClassPentester()
		for i in range(1, len(sys.argv) - 1):
			if sys.argv[i] == "-ip":
				c.Decoration('IP:')
				c.Get_req(query1)
			elif sys.argv[i] == "-search":
				c.Decoration('Search:')
				c.Search(query1)
			elif sys.argv[i] == "-lokasyon":
				c.Decoration('Lokasyon:')
				c.IpLocation(query1)
			elif sys.argv[i] == "-link":
				c.Decoration('Links:')
				c.Remove_duplicates(c.Find_suburls(query1))
			elif sys.argv[i] == "-img":
				c.Find_img(query1)
			elif sys.argv[i] == "-files":
				c.Find_files(str(query2),str(query3))
			elif sys.argv[i] == "-dig":
				c.Dig(str(query2),str(query3))
			elif sys.argv[i] == "-all":
				c.All(query2,query3,query1)
except Exception as e:
	print(str(e))
