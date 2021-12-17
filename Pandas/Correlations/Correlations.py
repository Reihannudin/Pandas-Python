'''
Menemukan Hubungan
Aspek hebat dari modul Pandas adalah corr()metodenya.

The corr()metode menghitung hubungan antara masing-masing 
kolom dalam kumpulan data Anda.

Contoh di halaman ini menggunakan file CSV yang disebut: 'data.csv'.
'''

import pandas as pd

df = pd.read_csv('csvFile/dataCor.csv')

print(df.corr())

'Catatan: The corr() Metode mengabaikan "tidak numerik" kolom.'

''''
Hasil Dijelaskan
Hasil dari corr() metode tersebut adalah tabel dengan banyak angka
yang merepresentasikan seberapa baik hubungan antara dua kolom.

Jumlahnya bervariasi dari -1 hingga 1.

1 berarti ada hubungan 1 banding 1 (korelasi sempurna), dan untuk kumpulan data ini, 
setiap kali nilai naik di kolom pertama, nilai lainnya juga naik.

0,9 juga merupakan hubungan yang baik, dan jika Anda meningkatkan satu nilai, 
nilai lainnya mungkin juga akan meningkat.

-0,9 akan sama baiknya dengan 0,9, tetapi jika Anda meningkatkan satu nilai, 
yang lain mungkin akan turun.

0.2 berarti BUKAN hubungan yang baik, artinya jika salah satu nilai naik 
tidak berarti nilai yang lain akan naik.
'''

'''
Apa itu korelasi yang baik? Itu tergantung pada penggunaannya, 
tetapi saya pikir aman untuk mengatakan Anda harus memiliki setidaknya 0.6 atau (-0.6) 
untuk menyebutnya korelasi yang baik.
'''

'''
Korelasi Sempurna:
Kita dapat melihat bahwa "Durasi" dan "Durasi" mendapat nomor 1.000000, yang masuk akal, 
setiap kolom selalu memiliki hubungan yang sempurna dengan dirinya sendiri.
'''

'''
Korelasi yang baik:
"Durasi" dan "Kalori" memiliki 0.922721 korelasi, yang merupakan korelasi yang sangat baik, 
dan kami dapat memprediksi bahwa semakin lama Anda berolahraga, semakin banyak kalori yang Anda bakar, 
dan sebaliknya: jika Anda membakar banyak kalori, Anda mungkin sudah lama bekerja.
'''

'''
Korelasi Buruk:
“Duration” dan “Maxpulse” memiliki 0.009403korelasi, yang merupakan korelasi yang sangat buruk, 
artinya kita tidak dapat memprediksi denyut nadi maksimal hanya dengan melihat durasi latihan, 
dan sebaliknya.
'''