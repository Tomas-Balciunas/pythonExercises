input = input()
input = str(input.lower())
check = input[::-1]
if input == check:
    print("palindrome")
else:
    print("not a palindrome")