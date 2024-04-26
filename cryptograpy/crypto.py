try:
	from cryptography.fernet import Fernet
	import hashlib
	import os, sys, time
except ModuleNotFoundError:
	start.library_install()

# Şifreleme İşlemleri
class Crypto:
	def __init__(self) -> None:
		super().__init__()
   
	def library_install(self):
		# Kütüphanelerin listesi
		libraries = [ 
		    "cryptography", "hashlib"
		]

		# Modül hatası veren kütüphanelerin yüklenmesi
		for lib in libraries:
		    try:
		        __import__(lib)
		    except ImportError:
		        os.system(f"pip3 install {lib}")

		print("Program 2 Saniye Sonra Devam Edicek ..")
		time.sleep(2)


	# python3 x.py -H admin -t md5 -r cryptography
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
	
	# python3 x.py -H 21232f297a57a5a743894a0e4a801fc3 -t md5 -r deciphering
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
