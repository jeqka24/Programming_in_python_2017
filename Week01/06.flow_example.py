import random
num = random.randint(0,101)

userinput = 0

while userinput!=num:
    userinput=input("Введите загаданное число:")
    if not userinput or userinput == "exit":
        break
    if not(userinput.isdigit()):
        continue
    if num > int(userinput):
        print("Загаданное число больше!")
    elif num < int(userinput):
        print ("Загаданное число меньше!")
    else:
        print("Соершенно верно!")
        break