""" Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
*Пример:*
5
1 2 3 4 5
6
-> 5 """


import random
N = int(input("Введи количество элементов массива: "))
array = random.sample(range(1, 100), N)
print(array)
X = int(input("Введи опорное число: "))
new_array = list(map(lambda n: n-X, array))
abs_number = [abs(ele) for ele in new_array]
temp = min(abs_number)
res = [i for i, j in enumerate(abs_number) if j == temp]
number_index = int(*res)
print(array[number_index])
