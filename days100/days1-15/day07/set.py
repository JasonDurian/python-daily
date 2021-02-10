set1 = {1, 2, 3, 4, 5}
print(set1)
print('Length =', len(set1))
set2 = set(range(1, 10))
print(set1, set2)
set3 = {num for num in range(2, 11) if num % 3 == 0 or num % 5 == 0}
print(set3)

set1.add(4)
set1.add(5)
set1.update([11, 12])
set1.discard(5)
if 4 in set1:
    set1.remove(4)
print(set1)
print(set3.pop())
print(set3)

set1 = {1, 2, 3, 4, 5, 11, 12}
set2 = set(range(1, 10))
print(set1, set2)
print(set1 & set2)
# print(set1.intersection(set2))
print(set1 | set2)
# print(set1.union(set2))
print(set1 - set2)
# print(set1.difference(set2))
print(set1 ^ set2)
# print(set1.symmetric_difference(set2))

print(set2 <= set1)
# print(set2.issubset(set1))
print(set1 >= set2)
# print(set1.issuperset(set2))
