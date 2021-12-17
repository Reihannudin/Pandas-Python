'''
Sel Kosong
Sel kosong berpotensi memberikan hasil yang salah saat Anda menganalisis data.
'''
'''
Hapus Baris
Salah satu cara untuk menangani sel kosong adalah dengan menghapus baris yang 
berisi sel kosong.

Ini biasanya baik-baik saja, karena kumpulan data bisa sangat besar, 
dan menghapus beberapa baris tidak akan berdampak besar pada hasilnya.
'''

'Kembalikan Bingkai Data baru tanpa sel kosong:'
import pandas as pd

df = pd.read_csv('csvFile/dirtydata.csv')

dfdrop = df.dropna()

print(dfdrop.to_string)

'''
Catatan: Secara default, dropna()metode ini mengembalikan DataFrame baru , 
dan tidak akan mengubah aslinya.
'''

'Jika Anda ingin mengubah DataFrame asli, gunakan inplace = Trueargumen:'

'Hapus semua baris dengan nilai NULL:'

df = pd.read_csv('csvFile/data.csv')

dfdropIN = df.dropna(inplace=True)

print(df.to_string())
'''
Catatan: Sekarang, dropna(inplace = True) TIDAK akan mengembalikan DataFrame baru, 
tetapi akan menghapus semua baris yang berisi nilai NULL dari DataFrame asli.
'''

'''
Ganti Nilai Kosong

Cara lain untuk menangani sel kosong adalah dengan memasukkan nilai baru .

Dengan cara ini Anda tidak perlu menghapus seluruh baris hanya karena beberapa sel kosong.

The fillna()Metode memungkinkan kita untuk mengganti sel-sel kosong dengan nilai:
'''
'Ganti nilai NULL dengan angka 130:'
df = pd.read_csv('csvFile/data.csv')

df.fillna(130, inplace = True)

print(df.to_string())
'''
Ganti Hanya Untuk Kolom Tertentu

Contoh di atas menggantikan semua sel kosong di seluruh Bingkai Data.

Untuk hanya mengganti nilai kosong untuk satu kolom, tentukan nama kolom untuk DataFrame:
'''
df = pd.read_csv('csvFile/data.csv')

df["Calories"].fillna(130, inplace = True)

print(df.to_string())

'''
Ganti Menggunakan Mean, Median, atau Mode
'''
'''
Cara umum untuk mengganti sel kosong adalah dengan menghitung nilai mean, median, atau mode kolom.

Pandas menggunakan metode mean() median() and mode() untuk menghitung nilai masing-masing untuk kolom tertentu:
'''
'Hitung MEAN, dan ganti nilai kosong apa pun dengannya:'
x = df["Calories"].mean()

df["Calories"].fillna(x , inplace= True)

print(df.to_string())

'Mean = nilai rata-rata (jumlah semua nilai dibagi jumlah nilai).'


'Hitung MEDIAN, dan ganti nilai kosong apa pun dengannya:'
x = df["Calories"].median()

df["Calories"].fillna(x, inplace=True)

print(df.to_string())

'Median = nilai di tengah, setelah Anda mengurutkan semua nilai secara menaik.'

'Hitung MODE, dan ganti nilai kosong apa pun dengannya:'
x = df["Calories"].mode()[0]

df["Calories"].fillna(x, inplace= True)

print(df.to_string())

'Mode = Nilai yang paling sering muncul'