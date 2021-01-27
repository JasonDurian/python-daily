import module1 as m1
import module2 as m2
import module3
import divisor_multiple as dm

# m1.foo()
# m2.foo()
a = int(input('Please input x: '))
b = int(input('Please input y: '))
print(dm.gcd(a, b))
print(dm.lcm(a, b))
