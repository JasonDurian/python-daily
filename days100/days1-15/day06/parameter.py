from random import randint


def roll_dice(n=2):
    total = 0
    for _ in range(n):
        total += randint(1, 6)
    return total


def add(a=0, b=0, c=0):
    return a + b + c


# print(roll_dice())
# print(roll_dice(1))
# print(add())
# print(add(1))
# print(add(1, 2))
# print(add(1, 2, 3))
# print(add(c=3, a=1, b=2))


def more_add(*args):
    total = 0
    for val in args:
        total += val
    return total


print(more_add())
print(more_add(1))
print(more_add(1, 2))
print(more_add(1, 2, 3))
print(more_add(1, 2, 3, 5, 7, 9))
