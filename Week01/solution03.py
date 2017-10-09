import sys
# ax2+bx+c = 0
a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

d = b*b - 4*a*c
if d > 0:
    print(int((-b - d ** 0.5) / (2 * a)))
    print(int((-b + d ** 0.5) / (2 *a)))
elif d == 0:
    print(-b/(2*a))