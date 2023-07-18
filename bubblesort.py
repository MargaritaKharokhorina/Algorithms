# Реализация сортиовки пузырьком с помощью циклов for 
from random import randint
 
n = 10
array1 = []
for i in range(n):
    array1.append(randint(1, 99))
print(array1)
 
 
for i in range(n-1):
    for j in range(n-i-1):
        if array1[j] > array1[j+1]:
            array1[j], array1[j+1] = array1[j+1], array1[j]
 
print(array1)

# С помощью циклов while
n = 10
array2 = []
for i in range(n):
    array2.append(randint(1, 99))
print(array2)
 
i = 0
while i < n - 1:
    j = 0
    while j < n - 1 - i:
        if array2[j] > array2[j+1]:
            array2[j], array2[j+1] = array2[j+1], array2[j]
        j += 1
    i += 1
 
print(array2)