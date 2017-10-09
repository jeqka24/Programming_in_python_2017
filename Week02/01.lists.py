# lists:

# 1. Empty:


empty_list = []

# ocnstucts from iterable
ten_list = list(range(1, 11))
ten_list[11] = "eleven" # error

# 2. operations
# enumerate(["alpha","beta","gamma"])
# list.append("item")
# numbers = [4, 17, 19, 9, 2, 6, 10, 13]
# sum(numbers) -> 80
# min(numbers) -> 2
# max(numbers) -> 19

# 3. Sorting

# Data:
import random

numbers = []
for _ in range(10):
    numbers.append(random.randint(1, 20))

print(numbers)
# Sorting (create sorted copy)
print(sorted(numbers))
# Does not change original list
print(numbers)

#
numbers.sort()
print(numbers)

# Reverse sorted:
print(sorted(numbers, reverse=True))

numbers.sort(reverse=True)
print(numbers)

# iterable
rev = list(reversed(numbers))

# 4. Tuple
empty_tuple = ()
one_element_tuple = (1,) # , is a must

# Hashable - could be keys in dicts
a = hash(empty_tuple)

import statistics

print(statistics.median(numbers))