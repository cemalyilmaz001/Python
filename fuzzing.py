import requests
import os

def fuzzing01():
    pwd = "/home/dsadas/Masaüstü/"
    host = "https://0a3d0056036c85f581cdca03002b00b0.web-security-academy.net/filter?category="
    header={"Cookie": "security=low; PHPSESSID=34127381273dsajdjaslkdas812730812dasjdnajlksndjkla"}
    t = 1

    dosya = open(f"{str(pwd)}fuzzing.txt","r")
    icerik = dosya.read()
    dosya.close()

    os.system("clear")
    os.system("figlet injection")

    print(f"""

    Url: {str(host)}
    Payload: {str(pwd)}fuzzing.txt

    """)

    for i in icerik.split("\n"):
        print(i)
        t += 1
        url=f"{str(host)}"+str(i)
        sonuc = requests.get(url=url, headers=header)
        if "200" in str(sonuc.status_code):
            print(i)
            dosya = open(f"{str(pwd)}kayit/{str(t)}_respons.html","w")
            dosya.write(f"\n{str(sonuc.content)}")

        dosya.close()


def fuzzing02():
    dosya = open("/path/fuzzing.txt","r")
    icerik = dosya.read()
    dosya.close()
    header={"Cookie": "security=low; PHPSESSID=34127381273dsajdjaslkdas812730812dasjdnajlksndjkla"}
    for i in icerik.split("\n"):
        print(i)
        url="http://192.168.1.41"+str(i)
        sonuc = requests.get(url=url, headers=header)
        if "200" in str(sonuc.status_code):
            print("Dosya Veya Dizin Var",i)
        else:
            print("Dosya veya dizin yok",i)
