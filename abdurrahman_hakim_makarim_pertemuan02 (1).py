# -*- coding: utf-8 -*-
"""Abdurrahman Hakim Makarim-Pertemuan02.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1QyJsanppol7ER-3xbQWcviwBXZVgGESj
"""

import numpy as np

# list untuk variabel a dan b
a = [1, 2, 3]
b = [4, 5, 6]

array1 = np.array(a)
array2 = np.array(b)

result = array1 + array2
print(result)

print(sum(result))

import numpy as np

# list untuk variabel a dan b
a = [1, 2, 3]
b = [4, 5, 6]

print(sum(result))

def totallist(list1, list2):
    total = 0
    for i in list1:
        total += i
    for i in list2:
        total += i
    return total

jumlah = totallist(a,b)
print(jumlah)

def totallist(jumlah):
    total = 0
    for i in jumlah:
        total += i
    return total

add_a_b = totallist(result)
print(add_a_b)

import numpy as np
# array nilai murid
nilaisiswa = np.array([85, 55, 40, 90])
print(nilaisiswa[0])
print(nilaisiswa[1])
print(nilaisiswa[2])
print(nilaisiswa[3])

#array dimulai dari 0 sampai angka terakhir misal 7, maka 0-6 (0 anggap satu)

print("Hello World")
print("nama saya (isi nama)")
print("nim saya (isi nim)")

Nama = input ("nama saya  ")
Nim = (input ("nim saya  "))
print ("nama saya ",   Nama)
print ("nim saya ",   Nim)

nama = 'Ilham'
usia = 13
print ('nama saya', nama, 'usia saya', usia)

a = input(" angka1  ")
b = input(" angka2  ")

if a > b:
    print(a, "lebih besar dari", b)
else:
    print(a, "lebih kecil dari", b)

def getFirst(urutanangka):
  return(urutanangka[0])

getFirst([1, 2, 3])

def getLast(urutanangka):
  return(urutanangka[5])
  getLast([1,2,3,4,5,6,7,8,9])

getLast([1,2,3,4,5,6,7,8,9])

def getlast2(list):
    size = len(list)
    print(f"Size: {size}")
    return list[size-1]

getlast2([1,2,3,4,5,6])

def getsum(listangkaku):
  sum = 0
  for row in listangkaku:
    for item in row:
      sum += item
  return sum

getsum([[1,2,3]])

def gettimes(listangkaku):
  times = 1
  for item in listangkaku:
      times *= item
  return times

gettimes([2,3])