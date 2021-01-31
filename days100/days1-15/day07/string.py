# Basic Usage
s1 = '\'hello, world!\''
s2 = '\n\\hello, world!\\\n'
print(s1, s2)

s1 = '\141\142\143\x61\x62\x63'
s2 = r'\u9a86\u660a'
print(s1, s2)

# print(char(1))
# print(chr(1))
print(0b100)

# Find & Slice
s1 = 'hello\t' * 3
print(s1)
s2 = 'world'
s1 += s2
print(s1)
print('ll' in s1)
print('good' in s1)

str2 = 'abc123456'
print(str2[2])
print(str2[2:6])
print(str2[2:])
print(str2[2::2])
print(str2[1:6:2])
print(str2[::-1])
print(str2[-3:-1])

# Dispose
str1 = 'hello, world!'
print(len(str1))
print(str1.capitalize())
print(str1.title())
print(str1.upper())
print(str1.find('or'))
print(str1.find('and'))
# print(str1.index('or'))
# print(str1.index('and'))
print(str1.startswith('He'))
print(str1.startswith('he'))
print(str1.endswith('!'))
print(str1.center(50, '*'))
print(str1.rjust(50, ' '))
print(str2.isdigit())
print(str2.isalpha())
print(str2.isalnum())
str3 = ' jasondurianvan@gmail.com '
print(str3.strip())

a, b = 5, 10
print('%d * %d = %d' % (a, b, a * b))
print('{0} * {1} = {2}'.format(a, b, a * b))
print(f'{a} * {b} = {a * b}')  # after python 3.6
