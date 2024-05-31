#!/usr/bin/python3


#
# Calisan
# 
class Calisan:
    def __init__(self, adSoyad, telefon, eposta):
        self.adSoyad = adSoyad
        self.telefon = telefon
        self.eposta = eposta

    def set(self):
        print(self.adSoyad)
        print(self.telefon)
        print(self.eposta)

    def giris(self):
        self.derseGir()

    def cikis(self):
        print("Çıkış Yapıldı")

    def yemekhane(self):
        print("Yemekhane")


class LabAsistani:
    def __init__(self):
        pass

    def lablaraGir(self):
        print("Labarotuvara Giriş Yapıldı")


class Asistan(LabAsistani):
    def __init__(self):
        super().__init__()
        self.ofisSaati = 1231
    
    def quizYap(self):
        pass    

class Akademisyen(Calisan):
    def __init__(self, adSoyad, telefon, eposta):
        super().__init__(adSoyad, telefon, eposta)
        self.bolum = "Bilişim Güvenliği"
        self.unvan = "SOC"

    def akadmsySet(self):
        print(self.adSoyad)
        print(self.telefon)
        print(self.eposta)

    def derseGir(self):
        print("hello World")


class OgrtmGorevlisi(Akademisyen):
    def __init__(self, adSoyad, telefon, eposta):
        super().__init__(adSoyad, telefon, eposta)
        self.kapiNo = 33

    def senatoToplanti(self):
        pass
    
    def sinavYap(self):
        pass

class Memur(Calisan):
    def __init__(self, adSoyad, telefon, eposta):
        super().__init__(adSoyad, telefon, eposta)
        self.departman = "Bilgi İşlem"
        self.mesai = "8.5"
        
    def calis(self):
        print(self.adSoyad)
        print(self.telefon)
        print(self.eposta)

class BilgiIslem(Memur):
    def __init__(self, adSoyad, telefon, eposta):
        super().__init__(adSoyad, telefon, eposta)
        self.gorev = ""

    def networkKurulum(self):
        pass

class GuvenlikGorevlisi(Memur):
    def __init__(self, adSoyad, telefon, eposta):
        super().__init__(adSoyad, telefon, eposta)
        self.belge = "xx11"

    def nobel(self):
        pass

if __name__ == "__main__":
    calis = Calisan("ASD SA", "034112333", "x@s.com")
    calis.set()
    print(30*"-")

    memur = Memur("Ahmet Kaya", "034112334", "y@x.com")
    print(memur.departman)
    print(memur.mesai)
    memur.calis()
    print(30*"-")

    akadmsyn = Akademisyen("Ayşe Demir", "034112335", "z@x.com")
    print(akadmsyn.bolum)
    print(akadmsyn.unvan)
    akadmsyn.akadmsySet()
    
