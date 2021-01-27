"""
Implement combination
Like C(m, n)
"""
m = int(input('m = '))
n = int(input('n = '))


def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result


# fm = 1
# for num in range(1, m + 1):
#     fm *= num
# fn = 1
# for num in range(1, n + 1):
#     fn *= num
# fm_n = 1
# for num in range(1, m - n + 1):
#     fm_n *= num
# print(fm // fn // fm_n)
print(factorial(m) // factorial(n) // factorial(m - n))
