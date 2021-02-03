a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []

enter = int(input("Enter a number: "))

for i in range(len(a)):
    if a[i] < enter:
        b.append(a[i])

print(b)
