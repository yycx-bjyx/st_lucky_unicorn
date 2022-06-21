num = 0
while True:
    try:
        num = float(input("Type in an integer"))
        num = float(num)
        total = num * 5
        print("{} times five equal to" "{}" .format(num, total))
        break
    except ValueError:
        print("this is not a valid number")


name = ""
while name.lower() != "xxx":
    name = input("who are you?")
    print(name)

print()
# for a blank space / line when run the code
print("we are done")
