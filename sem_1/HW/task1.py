# n=650
# res = (n//100) + (n%100//10) + (n%10)
# print(res)

# n=32
# p = n/6
# # p = (n//3)//2
# s = p
# k = (p + s) * 2
#
# print(int(p), int(k), int(s))

# n = 385916
# a = 385916
# b = a//1000
# one = b//100
# two = (b//10) % 10
# three = b%10
# c = a%1000
# four = c//100
# five = (c//10) % 10
# six = c%10
# # print(five)
# if (one+two+three)==(four+five+six):
#     print ('Счастливый')
# else:
#     print ('Обычный')

a = int(input())
b = int(input())
c = int(input())
if c < a * b and ((c % a == 0) or (c % b == 0)):
    print('YES')
else:
    print('NO')

