# Дано натуральное число. Требуется определить, является ли год с данным номером високосным.
# Если год является високосным, то выведите YES, иначе выведите NO.
# Напомним, что в соответствии с григорианским календарем, год является високосным,
# если его номер кратен 4, но не кратен 100, а также если он кратен 400.
# Input: 2016
# Output: YES

x = int(input("vvedite god: "))
# if (x % 4 == 0 and x % 100 != 0) or (x % 400 == 0):
#     print("yes")
# else:
#     print('no')

print("YES" if (x % 400 == 0) or (x % 4 == 0 and not x % 100 == 0) else 'NO')