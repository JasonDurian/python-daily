import random

"""
Calculate the sum from 1 to 100
"""
# sumNum = 0
# for x in range(1, 101, 1):
#     sumNum += x
# print(sumNum)
# print(sum(range(101)))

"""
Number guessing game
"""
answer = random.randint(1, 100)
counter = 0
while True:
    counter += 1
    number = int(input('Please input your number: '))
    if number < answer:
        print('Bigger')
    elif number > answer:
        print('Smaller')
    else:
        print('Congratulations on your right answer!')
        break
print('You made %d guesses in total' % counter)
if counter > 7:
    print('Your IQ balance is obviously inadequate!')
