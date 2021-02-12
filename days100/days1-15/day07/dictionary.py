scores = {'Jason': 99, 'Oreo': 97, 'Shunko': 80}
print(scores)
items1 = dict(one=1, two=2, three=3, four=4)
print(items1)
items2 = dict(zip(['a', 'b', 'c'], '123'))
print(items2)
items3 = {num: num ** 2 for num in range(1, 10)}
print(items3)

print(scores['Jason'])
for key in scores:
    print(f'{key}: {scores[key]}')
scores['Oreo'] = 88
scores['Jack'] = 89
scores.update(Wang=70)
print(scores)
if 'Henry' in scores:
    print(scores['Henry'])
print(scores.get('Henry'))
print(scores.get('Henry', 66))
print(scores)
print(scores.popitem())
print(scores)
print(scores.pop('Jason', 80))
print(scores)
scores.clear()
print(scores)
