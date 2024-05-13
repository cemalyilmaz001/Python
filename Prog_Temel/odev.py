#!/usr/bin/python3

class LabAsistani(object):
    def __init__(self):
        pass

    def lablaraGir(self):
        pass


class Asistan(LabAsistani):
    def __init__(self):
        self.ofisSaati = 1231
    
    def quizYap(self):
        pass    

class OgrtmGorevlisi(Asistan):
    def __init__(self):
        self.kapiNo = 33

    def senatoToplanti(self):
        pass
    
    def sinavYap(self):
        pass



# --
# 
class Akademisyen(OgrtmGorevlisi):
    def __init__(self):
        self.bolum = "Bilişim Güvenliği"
        self.ünvan = "SOC"

    def derseGir(self):
        print("hello World")




class Bilgiİslem(Akademisyen):
    def __init__(self):
        self.gorev = ""

    def networkKurulum(self):
        pass


class GuvenlkGorevlisi(Bilgiİslem):
    def __init__(self):
        self.belge = ""

    def nobel(self):
        pass

# --
# 
class Memur(GuvenlkGorevlisi):
    def __init__(self):
        self.departman = ""
        self.mesai = ""
    
    def calis(self):
        pass
    




# 1
# 
class Calisan(Memur):
    def __init__(self):
        self.adSoyad = "dasd das"
        self.telefon = 5555555555
        self.eposta  = "c@gmail.com" 

    def giris(self):
        self.derseGir()
    
    def cikis(self):
        pass
    
    def yemekhane(self):
        pass



if __name__ == "__main__":
    xx = Calisan()
    xx.giris()
