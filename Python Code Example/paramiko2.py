try:
	import paramiko

	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect("192.168.1.41",username="typhoon",password="789456123")
	stdin, stdout, stderr = ssh.exec_command("cat /etc/passwd") # netstat -plnt
	for i in (stdout.read().decode('ascii').split("\n")):
		try:
			if 0 == int((str(i).split(":")[2])):
				print("uid sıfır olan kullanıcı: ",str(i).split(":")[0])
		except:
			pass
except:
	pass