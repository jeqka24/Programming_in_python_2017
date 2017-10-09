# Strings are immutable
#

example_string_1 = "Курс про Python на Coursera"
example_string_2 = 'Курс про "Python" на "Coursera"'
example_string_3 = "Курс про \"Python\" на \"Coursera\""

example_string_4 = "Файл на диске C:\\\\" # -> Файл на диске C:\\

# 'raw' strings
example_string_5 = r"Файл на диске C:\\" # -> Файл на диске C:\\

# multiline strings:
example_string_6 = "Perl - это тот язык, которые одинаково " \
    "выглядит как до, так и после RSA шифрования" \
    "(Keith Bostic)"

example_string_7 = """
Есть всего два типа языков программирования: те, на которые
люди всё время ругаются, и те, которые никто не использует.

Bjarne Stroustrup
"""

# string concatenation:
example_string_8 = "Hello " + "world!" # 3 memory allocations
example_string_9 = "I would never ask stupud questions! " * 100

# id() - a way to get adress in the memory

# Slices:
# [start:stop:step]
print(example_string_1[9:])     # Python на Coursera
print(example_string_1[9:15])   # Python
print(example_string_1[-8:])    # Coursera

print("0123456789"[::2]) # 02468
print("0123456789"[::-1]) # 987654321

# methods^
# 1. count(substr)
# 2. capitalize()
# 3. isdigit()

# Operators^
# 1. IN: a in b -> True if a in b
# for a in string: итерация по строке по одной букве

# String formatting / templating
template_1 = "%s - главное достоинство %s (%s)" % ("Лень", "программиста", "Larry Wall")
template_2 = "{} не лгут, но {} пользуются формулами. ({})".format("Цифры", "лжецы", "Robert A. Heilein")
template_3 = "{num} должно хватить для любых задач. {author}".format(num="640 kb", author="Bill Gates")

# Python 3.6+
subject = "оптимизация"
author = "Donald Knuth"
template_4 = f"Преждевременная {subject} - корень всех зол. ({author})"

num = 8
template_5 = f"Binary: {num:#b}"

num2 = 2/3
print(num2)
print(f"{num2:.3f}")

# User interaction
name = input("Введи своё имя:")

# Byte strings
byte_string_1 = b"Hello"
for b in byte_string_1:
    print(b)

# encoding str to bytes (utf-8 is default)
example_string_10 = "Привет"
byte_string_2 = example_string_10.encode("utf-8")
byte_string_3 = example_string_10.encode()

example_string_11 = byte_string_2.decode()

