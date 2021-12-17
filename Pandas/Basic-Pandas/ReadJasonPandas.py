'''
Baca JSON
Kumpulan data besar sering disimpan, atau diekstraksi sebagai JSON.

JSON adalah teks biasa, tetapi memiliki format objek, 
dan terkenal di dunia pemrograman, termasuk Pandas.

Dalam contoh kita, kita akan menggunakan file JSON bernama 'data.json'.
'''

'Muat file JSON ke dalam DataFrame:'
import pandas as pd

df = pd.read_json('jsonFile/data.js')
print(df.to_string())
'Tip: gunakan to_string()untuk mencetak seluruh DataFrame.'
'Dictonary sebagai JSON'
'''
JSON = Dictonary Python

Objek JSON memiliki format yang sama dengan kamus Python.
'''

'''
Jika kode JSON Anda tidak ada dalam file, tetapi dalam Kamus Python, 
Anda dapat memuatnya ke dalam DataFrame secara langsung:
'''
'Muat Kamus Python ke dalam DataFrame:'

data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":300
  }
}

df = pd.DataFrame(data)

print(df) 

