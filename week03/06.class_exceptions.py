# 1. how to raise
raise Exception("Ашипка!")
# 2. hierarchy:
#   BaseException:
#       SystemExit
#       KeyboardInterrupt
#       GeneratorExit
#       Exception:
#           StopIteration
#           AssertionError
#           AttributeError
#           LookupError:
#               IndexError
#               KeyError
#           OSError
#           SystemError
#           TypeError
#           ValueError
# 3. Usage (common):
while True:
    try:
        raw = input("Введите целое число:")
        number = int(raw)
        break

    # here we process only type conversion errors
    except ValueError:
        print("Некорректное значение!")
# 3a. Usage (multiple exception type handling):
while True:
    try:
        raw = input("Введите целое число:")
        number = int(raw)
        break

    except ValueError:
        print("Некорректное значение!")

    except KeyboardInterrupt:
        print("Выход из программы...")
        break

# 3b. Usage (multiple exception type handling, combining):
total_count = 100_000
while True:
    try:
        print(total_count)
        raw = input("Введите целое число:")
        number = int(raw)
        total_count /= number
        break

    except (ValueError, ZeroDivisionError):
        print("Некорректное значение!")
# 3c. Usage (parent class) - see
# 4. finally - use 'with _ as x:' or 'finally'

# 5. Accessing additional exception info:
try:
    with open("/file/not/found") as f:
        content = f.read()
except OSError as err:
    print(err.errno, err.strerror)

# 6. args attribute - ValueError(*args,**kwargs):
import os.path
filename = "/file/not/found"
try:
    if not os.path.exists(filename):
        raise ValueError("Файл не существует!", filename)
except ValueError as err:
    message, file = err.args[0], err.args[1]
    print(message, file)

# 7. Traceback
import traceback

try:
    with open("/file/not/found/") as f:
        content = f.read()
except OSError as err:
    trace = traceback.print_exc(limit=300)
    print(trace)

# 8. super()
try:
    raw = "o12"
    if not raw.isdigit():
        raise ValueError("Плохое число!", raw)
except ValueError as v:
    print("некорректное значение", v)
    raise
# ...or:

try:
    raw = "o12"
    if not raw.isdigit():
        raise ValueError("Плохое число!", raw)
except ValueError as v:
    print("Ошибка", v.args[0], v.args[1])
    raise TypeError("Ошибка") from v

# 9. assert
# assert True, "message" -> Noop
# assert False, "message" -> raise AssertionError("message")
# - Used mostly for developing
# python -O disables assertions

# 10. Performance - use timeit, Luke
