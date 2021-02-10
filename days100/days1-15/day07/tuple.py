t = ('Jason', 38, True, 'Suzhou')
print(t)
print(t[0])
print(t[3])
for member in t:
    print(member)
# t[0] = 'Oreo'

person = list(t)
print(person)
person[0] = 'Lee'
person[1] = 25
print(person)

fruits_list = ['apple', 'orange', 'durian']
fruits_tuple = tuple(fruits_list)
print(fruits_tuple)
