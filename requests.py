
import requests
import os
import bs4

# Payload
# https://raw.githubusercontent.com/payloadbox/xxe-injection-payload-list/master/Intruder/xxe-injection-payload-list.txt.txt


# FUZZİNG
# https://raw.githubusercontent.com/kennyn510/wpa2-wordlists/master/PlainText/words.txt
# https://raw.githubusercontent.com/kennyn510/wpa2-wordlists/master/PlainText/baby.txt
# https://raw.githubusercontent.com/kennyn510/wpa2-wordlists/master/PlainText/cow.txt
# https://raw.githubusercontent.com/kennyn510/wpa2-wordlists/master/PlainText/cpanel.txt
# https://raw.githubusercontent.com/kennyn510/wpa2-wordlists/master/PlainText/creditcardpincodes.txt
# https://raw.githubusercontent.com/kennyn510/wpa2-wordlists/master/PlainText/default-routers.txt
# https://raw.githubusercontent.com/kennyn510/wpa2-wordlists/master/PlainText/languages.txt
# https://raw.githubusercontent.com/kennyn510/wpa2-wordlists/master/PlainText/linkedin.txt
# https://raw.githubusercontent.com/kennyn510/wpa2-wordlists/master/PlainText/logins.txt
# https://raw.githubusercontent.com/kennyn510/wpa2-wordlists/master/PlainText/mini.txt
# https://raw.githubusercontent.com/kennyn510/wpa2-wordlists/master/PlainText/numlist-9digits.txt
# https://raw.githubusercontent.com/kennyn510/wpa2-wordlists/master/PlainText/smalldict.txt

# https://raw.githubusercontent.com/kennyn510/wpa2-wordlists/master/Wordlists/Rockyou/0-9.txt
# https://raw.githubusercontent.com/kennyn510/wpa2-wordlists/master/Wordlists/Rockyou/A.txt
# https://raw.githubusercontent.com/kennyn510/wpa2-wordlists/master/Wordlists/Rockyou/B.txt
# https://raw.githubusercontent.com/kennyn510/wpa2-wordlists/master/Wordlists/Rockyou/C.txt
# https://raw.githubusercontent.com/kennyn510/wpa2-wordlists/master/Wordlists/Rockyou/D.txt
# https://raw.githubusercontent.com/kennyn510/wpa2-wordlists/master/Wordlists/Rockyou/E.txt
# https://raw.githubusercontent.com/kennyn510/wpa2-wordlists/master/Wordlists/Rockyou/F.txt
# https://raw.githubusercontent.com/kennyn510/wpa2-wordlists/master/Wordlists/Rockyou/G.txt
# https://raw.githubusercontent.com/kennyn510/wpa2-wordlists/master/Wordlists/Rockyou/H.txt
# https://raw.githubusercontent.com/kennyn510/wpa2-wordlists/master/Wordlists/Rockyou/I.txt
# https://raw.githubusercontent.com/kennyn510/wpa2-wordlists/master/Wordlists/Rockyou/J.txt
# https://raw.githubusercontent.com/kennyn510/wpa2-wordlists/master/Wordlists/Rockyou/K.txt
# https://raw.githubusercontent.com/kennyn510/wpa2-wordlists/master/Wordlists/Rockyou/L.txt
# https://raw.githubusercontent.com/kennyn510/wpa2-wordlists/master/Wordlists/Rockyou/M.txt
# https://raw.githubusercontent.com/kennyn510/wpa2-wordlists/master/Wordlists/Rockyou/N.txt
# https://raw.githubusercontent.com/kennyn510/wpa2-wordlists/master/Wordlists/Rockyou/O.txt
# https://raw.githubusercontent.com/kennyn510/wpa2-wordlists/master/Wordlists/Rockyou/P.txt
# https://raw.githubusercontent.com/kennyn510/wpa2-wordlists/master/Wordlists/Rockyou/Q.txt
# https://raw.githubusercontent.com/kennyn510/wpa2-wordlists/master/Wordlists/Rockyou/R.txt
# https://raw.githubusercontent.com/kennyn510/wpa2-wordlists/master/Wordlists/Rockyou/S.txt
# https://raw.githubusercontent.com/kennyn510/wpa2-wordlists/master/Wordlists/Rockyou/T.txt
# https://raw.githubusercontent.com/kennyn510/wpa2-wordlists/master/Wordlists/Rockyou/U.txt
# https://raw.githubusercontent.com/kennyn510/wpa2-wordlists/master/Wordlists/Rockyou/V.txt
# https://raw.githubusercontent.com/kennyn510/wpa2-wordlists/master/Wordlists/Rockyou/W.txt
# https://raw.githubusercontent.com/kennyn510/wpa2-wordlists/master/Wordlists/Rockyou/X.txt
# https://raw.githubusercontent.com/kennyn510/wpa2-wordlists/master/Wordlists/Rockyou/Y.txt
# https://raw.githubusercontent.com/kennyn510/wpa2-wordlists/master/Wordlists/Rockyou/Z.txt

# https://raw.githubusercontent.com/kennyn510/wpa2-wordlists/master/Wordlists/Ultimate2016/A.txt
# https://raw.githubusercontent.com/kennyn510/wpa2-wordlists/master/Wordlists/Ultimate2016/B.txt
# https://raw.githubusercontent.com/kennyn510/wpa2-wordlists/master/Wordlists/Ultimate2016/C.txt
# https://raw.githubusercontent.com/kennyn510/wpa2-wordlists/master/Wordlists/Ultimate2016/D.txt
# https://raw.githubusercontent.com/kennyn510/wpa2-wordlists/master/Wordlists/Ultimate2016/E.txt
# https://raw.githubusercontent.com/kennyn510/wpa2-wordlists/master/Wordlists/Ultimate2016/F.txt
# https://raw.githubusercontent.com/kennyn510/wpa2-wordlists/master/Wordlists/Ultimate2016/G.txt
# https://raw.githubusercontent.com/kennyn510/wpa2-wordlists/master/Wordlists/Ultimate2016/H.txt
# https://raw.githubusercontent.com/kennyn510/wpa2-wordlists/master/Wordlists/Ultimate2016/I.txt
# https://raw.githubusercontent.com/kennyn510/wpa2-wordlists/master/Wordlists/Ultimate2016/J.txt
# https://raw.githubusercontent.com/kennyn510/wpa2-wordlists/master/Wordlists/Ultimate2016/K.txt
# https://raw.githubusercontent.com/kennyn510/wpa2-wordlists/master/Wordlists/Ultimate2016/L.txt
# https://raw.githubusercontent.com/kennyn510/wpa2-wordlists/master/Wordlists/Ultimate2016/M.txt
# https://raw.githubusercontent.com/kennyn510/wpa2-wordlists/master/Wordlists/Ultimate2016/N.txt
# https://raw.githubusercontent.com/kennyn510/wpa2-wordlists/master/Wordlists/Ultimate2016/O.txt
# https://raw.githubusercontent.com/kennyn510/wpa2-wordlists/master/Wordlists/Ultimate2016/P.txt
# https://raw.githubusercontent.com/kennyn510/wpa2-wordlists/master/Wordlists/Ultimate2016/Q.txt
# https://raw.githubusercontent.com/kennyn510/wpa2-wordlists/master/Wordlists/Ultimate2016/R.txt
# https://raw.githubusercontent.com/kennyn510/wpa2-wordlists/master/Wordlists/Ultimate2016/S.txt
# https://raw.githubusercontent.com/kennyn510/wpa2-wordlists/master/Wordlists/Ultimate2016/T.txt
# https://raw.githubusercontent.com/kennyn510/wpa2-wordlists/master/Wordlists/Ultimate2016/U.txt
# https://raw.githubusercontent.com/kennyn510/wpa2-wordlists/master/Wordlists/Ultimate2016/V.txt
# https://raw.githubusercontent.com/kennyn510/wpa2-wordlists/master/Wordlists/Ultimate2016/W.txt
# https://raw.githubusercontent.com/kennyn510/wpa2-wordlists/master/Wordlists/Ultimate2016/X.txt
# https://raw.githubusercontent.com/kennyn510/wpa2-wordlists/master/Wordlists/Ultimate2016/Y.txt
# https://raw.githubusercontent.com/kennyn510/wpa2-wordlists/master/Wordlists/Ultimate2016/Z.txt



# İndirebilirsin
# Kendi Kodundan da deneyebilirsin
# curl https://raw.githubusercontent.com/kdjasdadada > A.txt


payloads = "https://raw.githubusercontent.com/cemalyilmaz001/Siber-Guvenlik/main/fuzzing-and-payloads/payloads/sqlmap_payload.txt"
fuzzing  = "https://raw.githubusercontent.com/kennyn510/wpa2-wordlists/master/PlainText/words.txt"
hedef    = "http://testphp.vulnweb.com/listproducts.php?cat="
pwd      = os.getcwd()

def scanner(datas, sayi):
    contents = requests.get(f"{str(datas)}")
    soup = bs4.BeautifulSoup(contents.content, "html.parser")
    files = open(f'{pwd}/depo/_nosave_{int(sayi)}_{int(len(contents.content))}.txt','w')
    # Requests upload
    files.write("URL         --> " + str(contents.url) + "\n")
    files.write("HEADERS     --> " + str(contents.headers) + "\n")
    files.write("STATUS      --> " + str(contents.status_code) + "\n\n")
    files.write(str(soup.prettify()))
    # File close
    files.close()

def file_save():
    if os.path.exists(f"{pwd}/nosave.txt"):
        pass
    else:
        # Payload Download
        contents = requests.get(f"{fuzzing}")
        soup = bs4.BeautifulSoup(contents.content, "html.parser")
        files = open('nosave.txt','w')
        files.write(str(soup.prettify()))
        files.close()
        
        fl = open(f"{pwd}/nosave.txt","r",encoding="utf-8")
        sayi = 0
        for i in fl.readlines():
            sayi += 1
            url = f"{hedef}" + i
            scanner(url, sayi)
        fl.close()

        os.remove(f"{pwd}/nosave.txt")


if __name__ == "__main__":
    file_save()