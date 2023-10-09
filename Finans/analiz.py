import pandas as pd
import matplotlib.pyplot as plt

# CSV dosyasından verileri yükleme
data = pd.read_csv('enflasyon_verileri.csv')

# Tarih sütununu datetime tipine dönüştürme
data['Yıl'] = pd.to_datetime(data['Yıl'])

# Yıl sütunu eklemek
data['Yıl'] = data['Yıl'].dt.year

# Yıllara göre gruplama ve TÜFE Oranı ortalamasını hesaplama
mean_tufe_by_year = data.groupby('Yıl')['TÜFE Oranı'].mean()

# Grafik oluşturma
plt.plot(mean_tufe_by_year.index, mean_tufe_by_year.values)
plt.xlabel('Yıl')
plt.ylabel('TÜFE Oranı Ortalaması')
plt.title('Enflasyon TÜFE Oranları - Yıllara Göre')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()



