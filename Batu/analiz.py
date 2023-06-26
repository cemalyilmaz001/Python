import pandas as pd
import matplotlib.pyplot as plt

# CSV dosyasından verileri yükleme
data = pd.read_csv('enflasyon_verileri.csv')

# Veri setini inceleme
print(data.head())  # Veri setinin ilk birkaç satırını görüntüleme

# Veri analizi
mean_tufe = data['TÜFE Oranı'].mean()  # TÜFE Oranı sütununun ortalamasını hesaplama
max_tufe = data['TÜFE Oranı'].max()    # TÜFE Oranı sütununun en yüksek değerini bulma
min_tufe = data['TÜFE Oranı'].min()    # TÜFE Oranı sütununun en düşük değerini bulma

# Grafik oluşturma
plt.plot(data['Aylar'], data['TÜFE Oranı'])
plt.xlabel('Aylar')
plt.ylabel('TÜFE Oranı')
plt.title('Enflasyon TÜFE Oranları')
plt.xticks(rotation=45)  # Ayların etiketlerini 45 derece döndürme
plt.grid(True)  # Izgara çizgilerini ekleme
plt.show()