from geopy.geocoders import Nominatim

def adresi_bul(adres):
    # Nominatim objesini oluştur
    geolocator = Nominatim(user_agent="adres_bulucu")
    
    # Adresi sorgula
    konum = geolocator.geocode(adres)
    
    if konum:
        print("Girilen adresin koordinatları:")
        print("Enlem:", konum.latitude)
        print("Boylam:", konum.longitude)
    else:
        print("Adres bulunamadı.")

if __name__ == "__main__":
    girilen_adres = input("Adres veya konum bilgisini girin: ")
    adresi_bul(girilen_adres)
