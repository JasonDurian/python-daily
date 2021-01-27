
# username = input('Please input your username: ')
# password = input('Please input your password: ')
#
# if username == 'admin' and password == '123456':
#     print('Authentication successful')
# else:
#     print('Authentication failed')

"""
Evaluate the piecewise function

        3x - 5  (x > 1)
f(x) =  x + 2   (-1 <= x <= 1)
        5x + 3  (x < -1)
"""
# x = int(input("Please input the number 'x': "))
# y = int(input('Please input the number "y": '))
#
# if x > 1:
#     y = 3 * x - 5
# elif x < -1:
#     y = 5 * x + 3
# else:
#     y = x + 2
#
# print('f(x) = %d' % y)

"""
The imperial inch is interchanged with the metric centimeter
"""
value = float(input('Please input length: '))
unit = input('Please input unit: ')

if unit == 'in' or unit == 'inch':
    print('%.2f inch = %.2f centimeter' % (value, value * 2.54))
elif unit == 'cm' or unit == 'centimeter':
    print('%.2f centimeter = %.2f inch' % (value, value / 2.54))
else:
    print('Please input in/inch or cm/centimeter')

