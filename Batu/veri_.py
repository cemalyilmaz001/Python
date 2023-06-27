import requests
from bs4 import BeautifulSoup
import csv

# TCMB Enflasyon Verileri sayfasının URL'si
url = 'https://www.tcmb.gov.tr/wps/wcm/connect/TR/TCMB+TR/Main+Menu/Istatistikler/Enflasyon+Verileri'

# Sayfayı istek yaparak çekme
response = requests.get(url)

# BeautifulSoup ile HTML'i ayrıştırma
soup = BeautifulSoup(response.content, 'html.parser')

# Tablo verilerini bulma
table = soup.find('table')
table_body = table.find('tbody')
rows = table_body.find_all('tr')

# Verileri CSV dosyasına yazma
with open('enflasyon_verileri.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Yıl', 'Aylar', 'TÜFE Oranı'])
    
    for row in rows:
        columns = row.find_all('td')
        data = [column.text.strip() for column in columns]
        writer.writerow(data)

print("Veriler başarıyla kaydedildi.")
