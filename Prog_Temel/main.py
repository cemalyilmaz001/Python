#!/usr/bin/python3

# Recursive Function
# -1. Verilen bir sayıya kadar tek sayıların toplamını bulan Recursive fonksiyon oluşturunuz
def toplam_tek_sayilar(n):
    if n <= 0:
        return 0
    elif n % 2 == 1:
        return n + toplam_tek_sayilar(n - 2)
    else:
        return toplam_tek_sayilar(n - 1)

sayi = int(input("Verilen sayılara kadar olan tek sayıların toplamını göstericek: "))
toplam = toplam_tek_sayilar(sayi)
print("1'den {}'e kadar olan tek sayıların toplamı: {}".format(sayi, toplam))


# -2. Girilen sayıya kadar olan sayıları gösteren Recursive fonksiyon oluşturunuz
def sayiyakadargit(s):
    for i in range(1,int(s) + 1):
        print(i)

s = int(input("Girilen sayıya kadar giden prog: "))
sayiyakadargit(s)


# -3. Üst Alma işlemini ust(taban,us) gerçekleştiren Recursive fonksiyon oluşturunuz
def ust(taban, us):
    if us == 0:
        return 1
    elif us == 1:
        return taban
    elif us < 0:
        return 1 / ust(taban, -us)
    elif us % 2 == 0:
        return ust(taban, us // 2) ** 2
    else:
        return taban * ust(taban, us - 1)

taban = float(input("Taban değerini girin: "))
us = int(input("Üs değerini girin: "))

sonuc = ust(taban, us)
print("{} üzeri {} = {}".format(taban, us, sonuc))



# -4. Asal Sayı Kontrolünü gerçekleştiren Recursive fonksiyon oluşturunuz.
def asal_mi(n, k=None):
    if k is None:
        k = n // 2 

    if n <= 1:
        return False
    elif k == 1:
        return True
    elif n % k == 0:
        return False
    else:
        return asal_mi(n, k - 1)

sayi = int(input("Bir sayı girin: "))

if asal_mi(sayi):
    print("{} bir asal sayıdır.".format(sayi))
else:
    print("{} bir asal sayı değildir.".format(sayi))



# -5. Verilen sayının basamaklarındaki sayı toplamını yapan Recursive fonksiyon oluşturunuz.
def basamak_toplamı(sayi):
    if sayi < 10:
        return sayi
    else:
        return sayi % 10 + basamak_toplamı(sayi // 10)

sayi = int(input("Bir sayı girin: "))
toplam = basamak_toplamı(sayi)

print("Girilen sayının basamaklarındaki sayıların toplamı:", toplam)


# Overloading


# Örnek - 1
# Ortalama adında en az iki sayının ortlamasını bulan ve geri döndüren 3 metod oluşturunuz (Overloading)

def add(a=0, b=0, c=0):
    sayac = 0
    if a >= 1:
        sayac += 1

    if b >= 1:
        sayac += 1

    if c >= 1:
        sayac += 1

    return ((a + b + c) / int(sayac))

print(add(2, 3))     # Output: 2.5
print(add(2, 3, 4))  # Output: 3.0



















