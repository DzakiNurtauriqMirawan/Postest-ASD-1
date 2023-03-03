# SHELLSORT 

import os
os.system('cls')
from random import randint
def shellSort(array, n):
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval

            array[j] = temp
        interval //= 2

list = []
for i in range(10):
    batas_angka = randint(0,50)
    list.append(batas_angka)

print('Sebelum ShellSort:', list)

size = len(list)
shellSort(list, size)
print('hasil ShellSort:', list)
