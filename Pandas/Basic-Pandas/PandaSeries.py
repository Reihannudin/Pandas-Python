'Pandas Series'

'''
Apa itu Seri?
Seri Pandas seperti kolom dalam tabel.

Ini adalah array satu dimensi yang menyimpan data jenis apa pun.
'''
'Buat Seri Pandas Sederhan dari List'
import pandas as pd

a = [1,7,2]

myvar = pd.Series(a)

print(myvar)


'''
Label
Jika tidak ada lagi yang ditentukan, nilai diberi label dengan nomor indeksnya. 
Nilai pertama memiliki indeks 0, nilai kedua memiliki indeks 1 dll.

Label ini dapat digunakan untuk mengakses nilai tertentu.
'''
print(myvar[1])

'''
Buat Label
Dengan indexargumen, Anda dapat memberi nama label Anda sendiri.
'''
'Buat Label '
b = [1,7,2]

myvar = pd.Series(b , index = ["x", "y", "z"])
print(myvar)

'Setelah membuat label, Anda dapat mengakses item dengan merujuk ke label.'

'Kembalikan nilai "y":'
print(myvar["y"])

'''
Objek Kunci/Nilai sebagai Seri
Anda juga dapat menggunakan objek kunci/nilai, seperti kamus, saat membuat Seri.
'''
'Buat Seri Pandas sederhana dari kamus:'
calories = {"day1":420,"day2": 380, "day3" :390}
myvar = pd.Series(calories)
print(myvar)

'Catatan: Kunci Dictonary menjadi label.'

'''
Untuk memilih hanya beberapa item dalam kamus, gunakan index argumen dan tentukan 
hanya item yang ingin Anda sertakan dalam Seri.
'''
'Buat Seri hanya menggunakan data dari "hari1" dan "hari2":'
myvar = pd.Series(calories, index=["day1", "day2"])
print(myvar)


'Dataframe'
''''
Kumpulan data di Panda biasanya berupa tabel multidimensi, 
yang disebut DataFrames.

Seri seperti kolom, DataFrame adalah seluruh tabel.
'''
'Buat DataFrame dari dua Seri:'
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

myvar = pd.DataFrame(data)

print(myvar)