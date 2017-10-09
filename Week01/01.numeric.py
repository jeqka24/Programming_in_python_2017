# Integer

n1 = 12

repr(type(n1)) == "<class 'int'>"

# Float

n2 = 14.0

# Complex

n3 = 13 + 2j

n3.real == 13
n3.imag == 2

n4 = n3.conjugate()

# Fixed numbers:
# import decimal

# Rational numbers:
# import fractions

print(10 / 2 == 5.0) # int OP int| -> float
print(10 // 3 == 3)  # int OP int -> int

# BitOps:
# OR:  x | y
# XOR: x ^ y
# AND: x & y
# SHL: x << 3
# SHR: x >> 1
# NOT: ~x

# no import sqrt from math
x1, y1 = 0, 0
x2, y2 = 3, 4
distance = ((x2-x1)**2+(y2-y1)**2)**0.5

# swaping
a = 100
b = 200
a, b = b, a

# immutable objects:
x = y = 0
x += 1
print(x,y)
1 0

# mutable objects:
x = y = []
x.append(1)
x.append(2)
print(x,y)
# [1,2][1,2]
