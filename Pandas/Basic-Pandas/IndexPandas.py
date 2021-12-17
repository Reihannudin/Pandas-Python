'''
Perkenalan Panda

Apa itu Panda?
Pandas adalah pustaka Python yang digunakan untuk bekerja dengan kumpulan data.

Ini memiliki fungsi untuk menganalisis, membersihkan, menjelajahi, dan memanipulasi data.

Nama "Panda" memiliki referensi ke "Data Panel", dan "Analisis Data Python" dan dibuat oleh 
Wes McKinney pada tahun 2008.
'''
'''
Mengapa Menggunakan Panda?
Panda memungkinkan kita untuk menganalisis data besar dan 
membuat kesimpulan berdasarkan teori statistik.

Panda dapat membersihkan kumpulan data yang berantakan, dan membuatnya dapat dibaca dan relevan.

Data yang relevan sangat penting dalam ilmu data.
'''
'''
Ilmu Data: adalah cabang ilmu komputer tempat kami mempelajari cara menyimpan, menggunakan, 
dan menganalisis data untuk memperoleh informasi darinya.
'''

'''
Apa yang Panda Bisa Lakukan?
Pandas memberi Anda jawaban tentang data. Suka:

Apakah ada korelasi antara dua atau lebih kolom?
Apa itu nilai rata-rata?
Nilai maksimal?
Nilai minimal?
Panda juga dapat menghapus baris yang tidak relevan, atau berisi nilai yang salah, 
seperti nilai kosong atau NULL. Ini disebut membersihkan data.
'''

'''
Pemasangan Panda
Jika Anda sudah menginstal Python dan PIP pada suatu sistem, maka instalasi Pandas sangat mudah.

Instal menggunakan perintah ini:
'''
'pip install pandas'

'''
Impor Panda
Setelah Pandas diinstal, impor di aplikasi Anda dengan menambahkan importkata kunci:
'''
import pandas

'Sekarang Pandas diimpor dan siap digunakan.'

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pandas.DataFrame(mydataset)
print(myvar)


'''
Panda sebagai pd
Panda biasanya diimpor dengan pd alias.
'''

'alias: Dalam Python alias adalah nama alternatif untuk merujuk pada hal yang sama.'

'Buat alias dengan askata kunci saat mengimpor:'
import pandas as pd

'Sekarang paket Pandas dapat disebut sebagai pdalih-alih pandas.'

myvarpd = pd.DataFrame(mydataset)
print(myvarpd)

'''
Memeriksa Versi Panda
String versi disimpan di bawah __version__ atribut.
'''
print(pd.__version__)
