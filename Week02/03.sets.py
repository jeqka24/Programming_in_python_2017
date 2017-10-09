# Sets
# Treat them as dicts without values

empty_set = {}

number_set = set(range(10))
number_set_2 = {1, 2, 3, 3, 4, 5, 6, 11}

if 3 in number_set == True

odd_set = set(range(1,10,2))
even_set = set(range(0,10,2))

# operations^
# | union
# & intersect
# - difference
# ^ xor set
# .add(key)
# .remove(key)

# frozenset() = no .add/.remove methods

# Task:

import random
random_set = set()

while True:
    new_number = random.randint(1,10)
    if new_number in random:
        break
    random_set.add(new_number)

print(len(random_set)+1)

# SEE ALSO:
# 1. https://docs.python.org/3/library/stdtypes.html
# 2. https://docs.python.org/3/tutorial/datastructures.html
# 3. https://en.wikipedia.org/wiki/Hash_table