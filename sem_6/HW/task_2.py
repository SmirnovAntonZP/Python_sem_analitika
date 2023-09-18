'''Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
(т.е. не меньше заданного минимума и не больше заданного максимума)
Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
Вывод: [1, 9, 13, 14, 19]'''
import random

list_1 = []
list_2 = []
min = int(input('Vvedite  minimalnoe znachenie: '))
max = int(input('Vvedite maximalnoe znachenie: '))


for i in range(10):
    list_1.append(random.randint(-20, 20))
print(f' начальный список {list_1}')
for i in range(len(list_1)):
    if min <= list_1[i] <= max:
        list_2.append(i)
print(*list_2, sep=',')
#print(f'индексы элементов принадлежащих диапозону: {res}')

# for i in range(len(lst_1)):end='
#     if list_1[i] >= min and list_1[i] <= max:
#         list_2.append(i)
# print(list_2)
# или

