'''
Apa itu DataFrame?

Pandas DataFrame adalah struktur data 2 dimensi, 
seperti array 2 dimensi, atau tabel dengan baris dan kolom.
'''
'Buat DataFrame Pandas sederhana:'
import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

# mengambil data dan memasukannya ke object dataframe
df = pd.DataFrame(data)
print(df) 

'''
Cari Baris
Seperti yang Anda lihat dari hasil di atas, 
DataFrame seperti tabel dengan baris dan kolom.

Panda menggunakan locatribut untuk mengembalikan 
satu atau lebih baris yang ditentukan
'''

'kembalikan baris 0:'
print(df.loc[0])

'Catatan: Contoh ini mengembalikan Seri Pandas'

'Kembalikan baris 0 dan 1:'
print(df.loc[[0,1]])

'Catatan: Saat menggunakan [], hasilnya adalah Pandas DataFrame .'


'''
Indeks Bernama
Dengan indexargumen, Anda dapat memberi nama indeks Anda sendiri.
'''

'Tambahkan daftar nama untuk memberi setiap baris nama:'
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

print(df) 

'''
Temukan Indeks Bernama
Gunakan indeks bernama dalam locatribut untuk mengembalikan baris 
yang ditentukan.'''

'mengembalikan ke "day2"'
print(df.loc["day2"])

'''
Muat File Ke dalam DataFrame
Jika kumpulan data Anda disimpan dalam file, 
Pandas dapat memuatnya ke dalam DataFrame.
'''

'Muat file yang dipisahkan koma (file CSV) ke dalam DataFrame:'
df = pd.read_csv('data.csv')
print(df)