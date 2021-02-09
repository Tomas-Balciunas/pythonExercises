a = [1, 1, 2, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []


def function():
    for i in a:
        b.append(i)
    return list(set(b))


print(function())
