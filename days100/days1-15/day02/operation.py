
# a = int(input('a = '))
# b = int(input('b = '))
# c = 1
# c += a
# c += b
#
# print('(%d) + (%d) = %d' % (a, b, c))
# print('(%d) // (%d) = %f' % (a, b, a // b))
# print('(%d) %% (%d) = %d' % (a, b, a % b))
# print('(%d) ** (%d) = %d' % (a, b, a ** b))

"""
Convert Fahrenheit to Celsius
"""
# f = float(input('Please input Fahrenheit: '))
# c = (f - 32) / 1.8
# print('%.1f Fahrenheit = %.1f Celsius' % (f, c))

"""
Calculate the circumference and area of a circle
"""
# r = float(input('Please input the radius of a circle: '))
# cir = 2 * 3.14 * r
# area = 3.14 * (r ** 2)
# print('circumference = %.2f' % cir)
# print('area = %.2f' % area)

"""
Enter the year, if it is a leap year, output True, otherwise output False
"""
year = int(input('Please input year: '))
is_leap = year % 4 == 0 and year % 100 != 0 or \
    year % 400 == 0
print(is_leap)
