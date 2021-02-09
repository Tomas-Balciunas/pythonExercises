a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = [nr1 and nr2 for nr1 in a for nr2 in b if nr1 == nr2]
print(list(set(c)))

