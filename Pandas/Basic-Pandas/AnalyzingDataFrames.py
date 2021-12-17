'''
Melihat Data

Salah satu metode yang paling sering digunakan untuk
mendapatkan gambaran singkat tentang DataFrame, 
adalah head() metodenya.
'''

'''
The head()Metode mengembalikan header dan sejumlah 
tertentu dari baris, mulai dari atas.
'''
'mencetak 10 baris pertama DataFrame:'
import pandas as pd

df = pd.read_csv('csvFile/data.csv')

print(df.head(10))

'''
Catatan: jika jumlah baris tidak ditentukan, head()
metode ini akan mengembalikan 5 baris teratas.
'''
'Cetak 5 baris pertama DataFrame:'
print(df.head())

'''
Ada juga tail() metode untuk melihat baris terakhir dari DataFrame.

The tail()Metode mengembalikan header dan sejumlah tertentu
dari baris, mulai dari bawah.
'''
'Cetak 5 baris terakhir DataFrame'
print(df.tail())

'''
Info Tentang Data

Objek DataFrames memiliki metode yang disebut info(), 
yang memberi Anda lebih banyak informasi tentang kumpulan data.
'''
'Cetak informasi tentang data:'
print(df.info())

'''
Hasil Dijelaskan
Hasilnya memberi tahu kita bahwa ada 169 baris dan 4 kolom:
  RangeIndex: 169 entri, 0 hingga 168 
  kolom Data (total 4 kolom):
Dan nama setiap kolom, dengan tipe data:
   # Jenis Jumlah Kolom Bukan Null   
  --- ------ -------------- -----   
   0 Durasi 169 non-null int64   
   1 Pulse 169 non-null int64   
   2 Maxpulse 169 non-null int64   
   3 Kalori 164 non-null float64

'''

'''
Nilai Null
The info()M etode juga mengatakan kepada kita berapa banyak 
Non-Null nilai ada yang hadir di setiap kolom, dan di data 
kami set sepertinya ada 164 dari 169 nilai-nilai Non-Null 
dalam kolom "Kalori".

Artinya ada 5 baris tanpa nilai sama sekali, di kolom "Kalori", 
untuk alasan apa pun.

Nilai kosong, atau nilai Null, bisa berakibat buruk saat 
menganalisis data, dan Anda harus mempertimbangkan untuk 
menghapus baris dengan nilai kosong. Ini adalah langkah 
menuju apa yang disebut membersihkan data , dan Anda akan 
mempelajarinya lebih lanjut di bab berikutnya.
'''