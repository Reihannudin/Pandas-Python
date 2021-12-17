'''
Fixing Wrong Data
'''
'''
Data yang salah
"Data salah" tidak harus "sel kosong" atau "format salah", 
bisa saja salah, seperti jika seseorang mendaftarkan "199" dan bukan "1,99".

Terkadang Anda dapat menemukan data yang salah dengan melihat kumpulan data, 
karena Anda memiliki ekspektasi tentang apa yang seharusnya terjadi.

Jika Anda melihat kumpulan data kami, Anda dapat melihat bahwa di baris 7, 
durasinya adalah 450, tetapi untuk semua baris lainnya durasinya antara 30 dan 60.

Tidak harus salah, tetapi dengan mempertimbangkan bahwa ini adalah kumpulan data 
sesi latihan seseorang, kami menyimpulkan dengan fakta bahwa orang ini tidak berolahraga dalam 450 menit.
'''
''''
      Durasi Tanggal Pulse Maxpulse Kalori 
  0 60 '2020/12/01' 110 130 409.1 
  1 60 '2020/12/02' 117 145 479.0 
  2 60 '2020/12/03' 103 135 340.0 
  3 45 '2020/12/04' 109 175 282.4 
  4 45 '2020/12/05' 117 148 406.0 
  5 60 '2020/12/06' 102 127 300.0 
  6 60 '2020/12/07' 110 136 374.0 
  7 450 '2020/12/08' 104 134 253.3 
  8 30 '2020/12/09' 109 133 195.1 
  9 60 '2020/12/10' 98 124 269.0 
  10 60 '2020/12/11' 103 147 329.3
  11 60 '2020/12/12' 100 120 250.7 
  12 60 '2020/12/12' 100 120 250.7 
  13 60 '2020/12/13' 106 128 345.3 
  14 60 '2020/12/14' 104 132 379.3 
  15 60 '2020/12/15' 98 123 275.0 
  16 60 '2020/12/16' 98 120 215.2 
  17 60 '2020/12/17' 100 120 300.0 
  18 45 '2020/12/18' 90 112 NaN 
  19 60 '2020 /12/19' 103 123 323.0 
  20 45 '2020/12/20' 97 125 243.0 
  21 60 '2020/12/21' 108 131 364.2 
  22 45 NaN 100 119 282.0
  23 60 '2020/12/23' 130 101 300.0 
  24 45 '2020/12/24' 105 132 246.0 
  25 60 '2020/12/25' 102 126 334.5 
  26 60 20201226 100 120 250.0 
  27 60 '2020/12/27 ' 92 118 241.0 
  28 60 '2020/12/28' 103 132 NaN 
  29 60 '2020/12/29' 100 132 280.0 
  30 60 '2020/12/30' 102 129 380.3 
  31 60 '2020/12/31' 92 115 243.0

'''
'Bagaimana kita bisa memperbaiki nilai yang salah, seperti yang untuk "Durasi" di baris 7?'

'''
Mengganti Nilai
Salah satu cara untuk memperbaiki nilai yang salah adalah dengan menggantinya dengan yang lain.

Dalam contoh kita, kemungkinan besar salah ketik, dan nilainya harus "45" bukan "450", dan kita
bisa memasukkan "45" di baris 7:
'''

'Tetapkan "Durasi" = 45 di baris 7:'
import pandas as pd

df = pd.read_csv('csvFile/dirtydata.csv')

df.loc[7, 'Duration'] = 45

print(df.to_string())

'''
Untuk kumpulan data kecil, Anda mungkin dapat mengganti data yang salah satu per satu, 
tetapi tidak untuk kumpulan data besar.

Untuk mengganti data yang salah untuk kumpulan data yang lebih besar, Anda dapat membuat beberapa aturan, 
misalnya menetapkan beberapa batasan untuk nilai legal, dan mengganti nilai apa pun yang berada di luar batasan.
'''

'''
Ulangi semua nilai di kolom "Durasi".

Jika nilainya lebih tinggi dari 120, atur ke 120:
'''
for x in df.index:
    if df.loc[x, 'Duration']> 120:
        df.loc[x,'Duration'] = 120

print(df.to_string())

'''
Menghapus Baris
Cara lain untuk menangani data yang salah adalah dengan menghapus baris yang berisi data yang salah.

Dengan cara ini Anda tidak perlu mencari tahu apa yang harus diganti, dan ada kemungkinan Anda tidak 
membutuhkan mereka untuk melakukan analisis Anda.
'''

'Hapus baris dengan "Durasi" lebih tinggi dari 120:'
for x in df.index:
    if df.loc[x, 'Duration'] > 120:
        df.drop(x, inplace= True)

print(df.to_string())