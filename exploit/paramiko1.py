
try:
	import paramiko
	
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect("192.168.1.41",username="typhoon",password="789456123")
	stdin, stdout, stderr = ssh.exec_command("uname -a")
	print(stdout.read())
except:
	pass