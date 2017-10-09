empty_dict = {}

simple_dict = {
    "mutable" : ["list", "dict", "set"],
    "ummutable": ["tuple", "frozenset"],
}

for key in simple_dict:
    print(key, simple_dict[key])

for key, value in simple_dict.items():
    print(key, value)

# OrderedDict - preserves key in append order
from collections import OrderedDict

ordered = OrderedDict()

for number in range(10):
    ordered[number] = str(number)

for key in ordered:
    print(key)

zen = """
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""
zen_map = dict()
for word in zen.split():
    cleaned = word.strip(".,!-*").lower()
    if cleaned not in zen_map:
        zen_map[cleaned] = 0
    else:
        zen_map[cleaned] += 1
zen_items = zen_map.items()
import operator
word_count_item = sorted(zen_items, key=operator.itemgetter(1), reverse=True)
# Prints top-5
print(word_count_item[:5])

# The second way - batteries included
from collections import Counter
print(Counter(cleaned).most_common(5))
