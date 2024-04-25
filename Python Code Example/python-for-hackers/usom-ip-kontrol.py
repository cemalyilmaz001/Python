from tkinter import *
import datetime
import requests

def zararli_ip_verisi_usom_cek():
    response = requests.get("https://www.usom.gov.tr/url-list.txt",verify=False)
    dosya = open("usom.txt","w")
    dosya.write(str(response.content))
    dosya.close()

def kontrol_et():
    dosya = open("usom.txt","r")
    icerik = dosya.read()
    dosya.close()
    ip = entry1.get()
    bugun=datetime.datetime.now()
    if str(ip) in icerik:
        dosya=open("log.txt","a")
        yazi=str(ip)+" zararlı\nTarih:"+str(bugun)+"\n"
        dosya.write(yazi)
        dosya.close()
        v.set("IP Zararlidir")
    else:
        dosya=open("log.txt","a")
        yazi=str(ip)+" zararli degil\nTarih:"+str(bugun)+"\n"
        dosya.write(yazi)
        dosya.close()
        v.set("IP Zararli değildir")

#zararli_ip_verisi_usom_cek()

try:
    if __name__ == "__main__":
        top=Tk()
        top.title("USOM İP KONTROL")
        top.geometry("600x160")
	
        B = Button(top, text="Kontrol Et",command=kontrol_et)
        B.place(x=50,y=50)
        B.pack()

        label1=Label(top, text="Kontrol edilicek ip adresini giriniz: ")
        label1.place(x=50,y=80)
        label1.pack()

        entry1=Entry(top)
        entry1.place(x=50,y=90)
        entry1.pack()

        v = StringVar()

        entry2=Entry(top,textvariable=v)
        entry2.place(x=50,y=100)
        entry2.pack()

        top.mainloop()
    else:
        pass
except:
    pass
