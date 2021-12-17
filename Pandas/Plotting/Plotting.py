'Plotting'
''''
Pandas menggunakan plot() metode ini untuk membuat diagram.

Kita dapat menggunakan Pyplot, sebuah submodul dari library 
Matplotlib untuk memvisualisasikan diagram di layar.

'''

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('csvFile/dataPlot.csv')

df.plot()

plt.show()

'''
Scatter Plot

Tentukan bahwa Anda menginginkan plot pencar dengan kind argumen:

kind = 'scatter'

Sebuah plot pencar membutuhkan sumbu x dan sumbu y.

Pada contoh di bawah ini kita akan menggunakan 
"Durasi" untuk sumbu x dan "Kalori" untuk sumbu y.

Sertakan argumen x dan y seperti ini:

x = 'Duration', y = 'Calories'
'''

df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')

plt.show()

'''
Sebuah plot pencar membutuhkan sumbu x dan sumbu y.

Pada contoh di bawah ini kita akan menggunakan "Durasi" 
untuk sumbu x dan "Kalori" untuk sumbu y.

Sertakan argumen x dan y seperti ini:
'''

'''
Mari kita buat scatterplot lain, di mana ada hubungan 
yang buruk antara kolom, seperti "Duration" dan "Maxpulse", 
dengan korelasi 0.009403:
'''

df.plot(kind = 'scatter', x = 'Duration', y = 'Maxpulse')

plt.show()


'''
Histogram

Gunakan kind argumen untuk menentukan bahwa Anda menginginkan histogram:

kind = 'hist'

Sebuah histogram hanya membutuhkan satu kolom.

Histogram menunjukkan frekuensi setiap interval, 
misalnya berapa banyak latihan yang berlangsung antara 50 dan 60 menit?

Pada contoh di bawah ini kita akan menggunakan kolom "Duration" 
untuk membuat histogram:
'''
df['Duration'].plot(kind = 'hist')

plt.show()

'''
Catatan: Histogram memberi tahu kita bahwa ada lebih dari 100 latihan yang berlangsung antara 50 dan 60 menit.
'''