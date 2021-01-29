s1 = '\'hello, world!\''
s2 = '\n\\hello, world!\\\n'
print(s1, s2)

s1 = '\141\142\143\x61\x62\x63'
s2 = r'\u9a86\u660a'
print(s1, s2)

# print(char(1))
# print(chr(1))
print(0b100)


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
