# Сортировка выбором

from random import randint
N = 10
arr = []
for i in range(N):
    arr.append(randint(1, 99))
print(arr)

i = 0
while i < N - 1:
    min = i
    j = i + 1
    while j < N:
        if arr[j] < arr[min]:
            min = j
        j += 1

    arr[i], arr[min] = arr[min], arr[i]
    i += 1
print(arr)





