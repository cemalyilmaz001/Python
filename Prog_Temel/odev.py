#!/usr/bin/python3


#
# Calisan
# 
class Calisan():
    def __init__(self):
        super().__init__()
        self.adSoyad = "Cemal YILMAZ"
        self.telefon = 5523213213
        self.eposta  = "x@yaani.com" 

    def giris(self):
        self.derseGir()
    
    def cikis(self):
        pass
    
    def yemekhane(self):
        pass



#
# Akademisyen
#
class LabAsistani():
    def __init__(self):
        super().__init__()
        pass

    def lablaraGir(self):
        pass


class Asistan(LabAsistani):
    def __init__(self):
        super().__init__()
        self.ofisSaati = 1231
    
    def quizYap(self):
        pass    

class OgrtmGorevlisi(Akademisyen):
    def __init__(self):
        super().__init__()
        self.kapiNo = 33

    def senatoToplanti(self):
        pass
    
    def sinavYap(self):
        pass

class Akademisyen(Calisan):
    def __init__(self):
        super().__init__()
        self.bolum = "Bilişim Güvenliği"
        self.ünvan = "SOC"

    def derseGir(self):
        print("hello World")



#
# Memur
#
class Bilgiİslem(Memur):
    def __init__(self):
        super().__init__()
        self.gorev = ""

    def networkKurulum(self):
        pass


class GuvenlkGorevlisi(Memur):
    def __init__(self):
        super().__init__()
        self.belge = "xx11"

    def nobel(self):
        pass


class Memur(Calisan):
    def __init__(self):
        super().__init__()
        self.departman = "Bilgi İşlem"
        self.mesai     = "8.5"
    
    def calis(self):
        print(self.adSoyad)


if __name__ == "__main__":
    memur = Memur()
    print(memur.departman)
    print(memur.mesai)
    memur.calis()

    akadmsyn = Akademisyen()
    print(akadmsyn.bolum)
    print(akadmsyn.ünvan)



