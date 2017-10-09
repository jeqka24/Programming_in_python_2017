import sys

digit_string = sys.argv[1]

sum = 0
for i in digit_string:
    if i.isdigit():
        sum += int(i)
print(sum)