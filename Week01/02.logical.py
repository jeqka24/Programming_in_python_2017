# Logical operations:
13 == 13
13 < 14
13 > 9
13 != 14

1 < 2 < 3

# bool(13) == True
# bool(0) == False
# bool("") == False
# and
# or
# not

x, y, z = True, False, True
result = x and y or z # -> True


# Type casting:
# Python evaluates both operands while it has to be done:
# 'or' evaluates until any true
# 'and' evaluates to last value
# 'not' evaluates at any case

x = 12
y = False

print(x or y == 12) # 12

z = "boom"

print(x and z) # boom
print(y or (x and z)) # boom
print(y or (z and x)) # 12

# Testing if year is leap
def is_leap_year(year):
    leap = (year % 4 == 0) and (year % 100 !=0 or year % 400 == 0)
    return leap

# import calendar
# print(calendar.isleap(year))