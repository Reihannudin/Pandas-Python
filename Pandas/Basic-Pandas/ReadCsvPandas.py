'''
Baca File CSV
Cara sederhana untuk menyimpan kumpulan data besar 
adalah dengan menggunakan file CSV (file yang dipisahkan koma).

File CSV berisi teks biasa dan merupakan format yang dikenal 
baik yang dapat dibaca oleh semua orang termasuk Panda.

Dalam contoh kita, kita akan menggunakan file CSV yang disebut 'data.csv'.
'''

'Muat CSV ke dalam DataFrame:'
import pandas as pd

df = pd.read_csv('csvFile/data.csv')

print(df.to_string())
'Tip: gunakan to_string()untuk mencetak seluruh DataFrame.'

'''
Jika Anda memiliki DataFrame besar dengan banyak baris, 
Pandas hanya akan mengembalikan 5 baris pertama, dan 5 baris terakhir:
'''

'Cetak DataFrame tanpa to_string() metode:'
print(df)

'''
max_rows
Jumlah baris yang dikembalikan ditentukan dalam pengaturan opsi Pandas.

Anda dapat memeriksa baris maksimum sistem Anda dengan 
pd.options.display.max_rows statement.
'''
'Periksa jumlah baris yang dikembalikan maksimum:'
print(pd.options.display.max_rows)

'''
Di sistem saya jumlahnya adalah 60, yang berarti bahwa jika DataFrame 
berisi lebih dari 60 baris, print(df)pernyataan tersebut hanya akan 
mengembalikan header dan 5 baris pertama dan terakhir.

Anda dapat mengubah jumlah baris maksimum dengan pernyataan yang sama.
'''

'Tingkatkan jumlah baris maksimum untuk menampilkan seluruh DataFrame:'

pd.options.display.max_rows = 9999

df = pd.read_csv('csvFile/data.csv')

print(df) 