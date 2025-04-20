import pandas as pd
import matplotlib.pyplot as plt

# STEP 1: Baca data dari file CSV
data = pd.read_csv('penjualan.csv')

# STEP 2: Bersihkan data
data['produk'] = data['produk'].str.lower().str.title()

# STEP 3: Hitung total penjualan per produk
total_penjualan = data.groupby('produk')['jumlah'].sum().reset_index()

# STEP 4: Simpan data hasil ke file baru
total_penjualan.to_csv('total_penjualan_bersih.csv', index=False)

# STEP 5: Visualisasi data
plt.figure(figsize=(8,5))
plt.bar(total_penjualan['produk'], total_penjualan['jumlah'], color='green')
plt.title('Total Penjualan per Produk')
plt.xlabel('Produk')
plt.ylabel('Jumlah Terjual')
plt.xticks(rotation=30)
plt.tight_layout()

# Simpan grafik ke file
plt.savefig('grafik_penjualan.png')
plt.show()
