"""
Find the number of daffodils
"""
# for num in range(100, 1000):
#     low = num % 10
#     mid = num // 10 % 10
#     high = num // 100
#     if num == low ** 3 + mid ** 3 + high ** 3:
#         print(num)

"""
Inversion of a positive integer
"""
# num = int(input('num = '))
# reversed_num = 0
# while num > 0:
#     reversed_num = reversed_num * 10 + num % 10
#     num //= 10
# print(reversed_num)

"""
Hundreds of money and hundreds of chickens
"""
# for x in range(0, 21):
for x in range(0, 20):
    # for y in range(0, 34):
    for y in range(0, 33):
        z = 100 - x - y
        if 5 * x + 3 * y + z / 3 == 100:
            print('Cock: %d, Hen: %d, Chick: %d' % (x, y, z))
