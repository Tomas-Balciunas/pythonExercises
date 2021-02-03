enter = int(input("Enter a number: "))

number = enter
arr = []

while number > 0:
    if enter % number == 0:
        arr.append(number)
    number -= 1

print(arr)
